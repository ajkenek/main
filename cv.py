import cv2
import numpy as np
import requests


def count_people(img):
    if img is None:
        return None

    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    (rects, weights) = hog.detectMultiScale(
        img,
        winStride=(4, 4),
        padding=(8, 8),
        scale=1.05
    )
    return len(rects)


def process_local_file(path: str):
    img = cv2.imread(path)
    return count_people(img)


def process_url(url: str):
    try:
        response = requests.get(url, timeout=10)
        image_array = np.asarray(bytearray(response.content), dtype=np.uint8)
        img = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

        return count_people(img)
    except Exception as e:
        print(f"Błąd pobierania URL: {e}")
        return None


def process_uploaded(file_bytes: bytes):
    try:
        nparr = np.frombuffer(file_bytes, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        return count_people(img)
    except Exception:
        return None
