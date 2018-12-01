import cv2
import requests
import numpy as np


username = "jarde"
password = "invisy"
url_with_auth = f"http://{username}:{password}@140.193.201.45:8080/shot.jpg"
url = f"http://140.193.201.45:8080/shot.jpg"


class WebFeed():
    def get_feed(self):
        while True:
            img_response = requests.get(url)
            img_array = np.array(bytearray(img_response.content), dtype=np.uint8)
            if img_array is not None:
                img = cv2.imdecode(img_array, -1)
                cv2.imshow("Invisy", img)

            if cv2.waitKey(1) == 27:
                break