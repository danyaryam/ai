import tensorflow as tf
import tensorflow_hub as hub
from PIL import Image, ImageDraw, ImageFont, ImageColor
import numpy as np
import matplotlib.pyplot as plt
import time
import os
import re
import requests
import cv2

# Definisikan model yang ingin kita gunakan
ALL_MODELS = {
    "Faster R-CNN w/ ResNet50 v1": "https://www.kaggle.com/models/tensorflow/faster-rcnn-resnet-v1/TensorFlow2/faster-rcnn-resnet101-v1-1024x1024/1",
    "Faster R-CNN w/ Inception ResNet v2": "https://www.kaggle.com/models/tensorflow/faster-rcnn-inception-resnet-v2/tensorFlow2/1024x1024/1",
}

# Definisikan url untuk label dari dataset
URL_LABEL = "https://raw.githubusercontent.com/tensorflow/models/master/research/object_detection/data/mscoco_label_map.pbtxt"
# Mendapatkan file dari url dan simpan dalam suatu path
PATH_TO_LABELS = tf.keras.utils.get_file(
    origin=URL_LABEL, fname="mscoco_label_map.pbtxt"
)

print(PATH_TO_LABELS)


# Fungsi untuk load file label dan mapping
def load_label_map(path_label):
    label_map = {}
    with open(path_label, "r") as f:
        label_text = f.read()

    # Mencari semua blok 'item' dalam file
    items = re.findall(r"item\s?{(.*?)}", label_text, re.DOTALL)

    # Menelusuri setiap id dan nama atau label objek pada blok item yang ditemukan
    for block in items:
        id_match = re.search(r"id:\s*(\d+)", block)
        name_match = re.search(r'display_name:\s*"([^"]+)"', block)

        # Jika kedua elemen (id dan nama) ditemukan, masukkan ke dalam label_map
        if id_match and name_match:
            item_id = int(id_match.group(1))
            display_name = name_match.group(1)
            label_map[item_id] = display_name

    print(f"Total {len(label_map)} kelas ditemukan.")

    return label_map
