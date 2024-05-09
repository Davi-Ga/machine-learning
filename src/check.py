import tensorflow as tf
from PIL import Image
import numpy as np
from utils.extractor import Extractor
from utils.saver import Saver
from settings import EXTRACTED_PATH, PROCESS_SAVE_PATH, CUTED_PATH
from features.labelling import Labelling
from features.cutter import Cutter
import os
from keras.preprocessing.image import load_img, img_to_array

batch_size = 32
img_height = 180
img_width = 180


def load_model():
    model = tf.keras.models.load_model("model.keras")
    return model


def load_images_from_folder(folder="data/extracted"):
    images = []
    for filename in os.listdir(folder):
        if filename.endswith(('.bmp', '.gif', '.jpeg', '.jpg', '.png')):
            img = load_img(os.path.join(folder, filename), target_size=(img_height, img_width))
            img = img_to_array(img)
            img = np.expand_dims(img, axis=0) 
            img = img/255.  # Normalize to [0,1]
            images.append(img)
    return images


def predict(model, image):
    prediction = model.predict(image)
    return prediction


def extract_pdf():
    extractor = Extractor()
    info, pages = extractor.extract_info()
    saver = Saver(PROCESS_SAVE_PATH, EXTRACTED_PATH)
    saver.save_selected_pages(pages)
    cutter = Cutter()
    cutter.cut_pdf()

def main():
    # extract_pdf()
    model = load_model()
    dataset = load_images_from_folder()
    for image_batch in dataset:
        predictions = model.predict(image_batch)
        predicted_labels = np.argmax(predictions, axis=1)
        print(predicted_labels)
        
if __name__ == "__main__":
    main()