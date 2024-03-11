import os
import glob
from pdf2image import convert_from_path
import pytesseract

class Cutter:
    
    def __init__(self, path='data/extracted/process1', search_text="PODER", output_folder='data/cuted/process1'):
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

                # Get the size of the image
                width, height = image.size

                # Define the amount to crop
                crop_amount = 400

                # Define the bounding box for the crop
                left = 0
                top = 0
                right = width
                bottom = height - crop_amount

                # Crop the image to the bounding box
                cropped_image = image.crop((left, top, right, bottom))

                # Save the image to the output directory
                image_path = os.path.join(self.output_folder, f'{os.path.basename(pdf_path.replace(".pdf",""))}.png')
                cropped_image.save(image_path)
                
            except (FileNotFoundError, IOError) as e:
                print(f"Error reading file {pdf_path}: {e}")
                
if __name__ == "__main__":
    cutter = Cutter()
    cutter.cut_pdf()
    print('Corte das páginas concluído.')