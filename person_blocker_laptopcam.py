import os
import sys
import argparse
import numpy as np
import coco
import utils
import requests
import model as modellib
from classes import get_class_names, InferenceConfig
from ast import literal_eval as make_tuple
import imageio
import visualize
from imutils.video import VideoStream
from imutils.video import FPS
import numpy as np
import argparse
import imutils
import time
import cv2


def create_noisy_color(image, color):
    color_mask = np.full(shape=(image.shape[0], image.shape[1], 3),
                         fill_value=color)

    noise = np.random.normal(0, 25, (image.shape[0], image.shape[1]))
    noise = np.repeat(np.expand_dims(noise, axis=2), repeats=3, axis=2)
    mask_noise = np.clip(color_mask + noise, 0., 255.)
    return mask_noise


# Helper function to allow both RGB triplet + hex CL input

def string_to_rgb_triplet(triplet):

    if '#' in triplet:
        # http://stackoverflow.com/a/4296727
        triplet = triplet.lstrip('#')
        _NUMERALS = '0123456789abcdefABCDEF'
        _HEXDEC = {v: int(v, 16)
                   for v in (x + y for x in _NUMERALS for y in _NUMERALS)}
        return (_HEXDEC[triplet[0:2]], _HEXDEC[triplet[2:4]],
                _HEXDEC[triplet[4:6]])

    else:
        # https://stackoverflow.com/a/9763133
        triplet = make_tuple(triplet)
        return triplet
    return 0

def person_blocker(args):

    # Required to load model, but otherwise unused
    ROOT_DIR = os.getcwd()
    COCO_MODEL_PATH = args.model or os.path.join(ROOT_DIR, "mask_rcnn_coco.h5")

    MODEL_DIR = os.path.join(ROOT_DIR, "logs")  # Required to load model

    if not os.path.exists(COCO_MODEL_PATH):
        utils.download_trained_weights(COCO_MODEL_PATH)

    # Load model and config
    config = InferenceConfig()
    model = modellib.MaskRCNN(mode="inference",
                              model_dir=MODEL_DIR, config=config)
    model.load_weights(COCO_MODEL_PATH, by_name=True)

    print("[INFO] starting video stream...")
    vs = VideoStream(src=0).start()
    time.sleep(2.0)
    fps = FPS().start()


    while True:
        frame = vs.read()
        frame = imutils.resize(frame, width=1000)
        image = imageio.imread(frame)
        results = model.detect([image], verbose=0)
        r = results[0]

    # if args.labeled:
        # position_ids = ['[{}]'.format(x)
        #                 for x in range(r['class_ids'].shape[0])]
        # visualize.display_instances(img, r['rois'],
        #                             r['masks'], r['class_ids'],
        #                             get_class_names(), position_ids)
    #     sys.exit()

        # Filter masks to only the selected objects
        objects = np.array(args.objects)

        # Object IDs:
        if np.all(np.chararray.isnumeric(objects)):
            object_indices = objects.astype(int)
        # Types of objects:
        else:
            selected_class_ids = np.flatnonzero(np.in1d(get_class_names(),
                                                        objects))
            object_indices = np.flatnonzero(
                np.in1d(r['class_ids'], selected_class_ids))

        mask_selected = np.sum(r['masks'][:, :, object_indices], axis=2) if len(object_indices) > 0 else None

        # Replace object masks with noise
        # mask_color = string_to_rgb_triplet(args.color)
        image_masked = img.copy()
        # noisy_color = create_noisy_color(image, mask_color)
        noisy_color = create_noisy_color(img, (208, 130, 238))
        if mask_selected is not None:
            image_masked[mask_selected > 0] = noisy_color[mask_selected > 0]    

        image_masked = imutils.resize(image_masked, width=1500)
        cv2.imshow("Frame", image_masked)
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break

        update the FPS counter
        fps.update()

    fps.stop()
    print("[INFO] elapsed time: {:.2f}".format(fps.elapsed()))
    print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

    do a bit of cleanup
    cv2.destroyAllWindows()
    vs.stop()
    exit()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Person Blocker - Automatically "block" people '
                    'in images using a neural network.')
    parser.add_argument('-i', '--image',  help='Image file name.',
                        required=False)
    parser.add_argument(
        '-m', '--model',  help='path to COCO model', default=None)
    parser.add_argument('-o',
                        '--objects', nargs='+',
                        help='object(s)/object ID(s) to block. ' +
                        'Use the -names flag to print a list of ' +
                        'valid objects',
                        default='person')
    parser.add_argument('-c',
                        '--color', nargs='?', default='(255, 255, 255)',
                        help='color of the "block"')
    parser.add_argument('-l',
                        '--labeled', dest='labeled',
                        action='store_true',
                        help='generate labeled image instead')
    parser.add_argument('-n',
                        '--names', dest='names',
                        action='store_true',
                        help='prints class names and exits.')
    parser.set_defaults(labeled=False, names=False)
    args = parser.parse_args()

    if args.names:
        print(get_class_names())
        sys.exit()

    person_blocker(args)
