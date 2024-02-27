import os
import glob
from pdf2image import convert_from_path
import pytesseract

class Cutter:
    
    def __init__(self, path='data/extracted', search_text="PODER", output_folder='data/cuted'):
        """Initialize the Cutter with a default path to PDF files."""
        self.path = path
        self.output_folder = output_folder
        self.search_text = search_text
        
        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)

    def cut_pdf(self):
        for pdf_path in glob.glob(os.path.join(self.path, '*.pdf')):
            try:
                print(f"Processing file {pdf_path}")
                # Convert the PDF to image
                images = convert_from_path(pdf_path)

                # Get the first page as image
                image = images[0]

                # Use pytesseract to get the data of the image
                data = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT)

                # Search for the text in the data
                search_text_list = self.search_text.split()
                for i in range(len(data["text"])):
                    if data["text"][i] == search_text_list[0] and data["text"][i:i+len(search_text_list)] == search_text_list:
                        # Get the bounding box of the text element
                        left = min(data["left"][i:i+len(search_text_list)]) - 260
                        top = min(data["top"][i:i+len(search_text_list)]) - 40
                        right = max([data["left"][j] + data["width"][j] for j in range(i, i+len(search_text_list))]) + 1262
                        bottom = max([data["top"][j] + data["height"][j] for j in range(i, i+len(search_text_list))]) + 102

                        # Crop the image to the bounding box
                        cropped_image = image.crop((left, top, right, bottom))

                        # Save the image to the output directory
                        image_path = os.path.join(self.output_folder, f'{os.path.basename(pdf_path)}.png')
                        cropped_image.save(image_path)

            except (FileNotFoundError, IOError) as e:
                print(f"Error reading file {data}: {e}")
                
if __name__ == "__main__":
    cutter = Cutter()
    cutter.cut_pdf()
    print('Corte das páginas concluído.')