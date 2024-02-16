from PIL import Image
import pytesseract
from pdf2image import convert_from_path
import re
import os
MARGIN = 10

def crop_pdf(file_path, search_text, output_dir):
    # Check if the input file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")

    # Convert the PDF to images
    images = convert_from_path(file_path)

    cropped_images = []
    for i, image in enumerate(images):
        # Use Tesseract to extract text and its bounding box
        data = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT)

        search_text_list = search_text.split()
        for i in range(len(data["text"])):
            if data["text"][i] == search_text_list[0] and data["text"][i:i+len(search_text_list)] == search_text_list:
                # Get the bounding box of the text element
                left = min(data["left"][i:i+len(search_text_list)]) + 1024
                top = min(data["top"][i:i+len(search_text_list)]) - MARGIN
                right = max([data["left"][j] + data["width"][j] for j in range(i, i+len(search_text_list))]) + 1024
                bottom = max([data["top"][j] + data["height"][j] for j in range(i, i+len(search_text_list))]) + 1024

                # Crop the image to the bounding box and append it to the list
                cropped_image = image.crop((left, top, right, bottom))
                cropped_images.append(cropped_image)

    # Save the cropped images to the output directory
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for i, image in enumerate(cropped_images):
        image.save(os.path.join(output_dir, f"cropped_image_{i}.png"))

    return cropped_images


if __name__ == "__main__":
    cropped_images = crop_pdf(
        "data/01-Sentença_modelo.pdf", "PODER", "output"
    )