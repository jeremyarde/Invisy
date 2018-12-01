import time
from tkinter import Label

import cv2
import requests
import numpy as np
import urllib3
from PIL import ImageGrab, Image, ImageTk
from urllib3.packages.six import StringIO
import PIL

username = "jarde"
password = "invisy"
url_with_auth = f"http://{username}:{password}@140.193.201.45:8080/shot.jpg"
url = f"http://140.193.201.45:8080/shot.jpg"


class WebFeed:
    @staticmethod
    def get_image():
        img_response = requests.get(url)
        img_array = np.array(bytearray(img_response.content), dtype=np.uint8)
        if img_array is not None:
            img = cv2.imdecode(img_array, -1)
            return img



    @staticmethod
    def get_feed():
        while True:
            img_response = requests.get(url)
            img_array = np.array(bytearray(img_response.content), dtype=np.uint8)
            if img_array is not None:
                img = cv2.imdecode(img_array, -1)
                cv2.imshow("Invisy", img)

            if cv2.waitKey(1) == 27:
                break

    @staticmethod
    def get_feed_single_image():
        img_response = requests.get(url)
        img_array = np.array(bytearray(img_response.content), dtype=np.uint8)
        img = Image.fromarray(img_response)
        # img = cv2.imdecode(img_array, -1)
        return img

    @staticmethod
    def get_screen_capture():
        last_time = time.time()
        while (True):
            screen = ImageGrab.grab(bbox=(50, 50, 800, 640))
            return screen
            # print('Loop took {} seconds', format(time.time() - last_time))
            # cv2.imshow("test", np.array(screen))
            # last_time = time.time()
            # if cv2.waitKey(25) & 0xFF == ord('q'):
            #     cv2.destroyAllWindows()
            #     break




# WebFeed.get_feed_single_image()
# WebFeed.get_feed_constant()
# WebFeed.get_feed()