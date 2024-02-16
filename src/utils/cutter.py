import os
import glob
from aspose.pdf import Document, License, Rectangle
import os


os.environ["DOTNET_SYSTEM_GLOBALIZATION_INVARIANT"] = "1"


class Cutter:
    
    def __init__(self, path='data/processos', output_folder='data/cuted'):
        """Initialize the Cutter with a default path to PDF files."""
        self.path = path
        self.output_folder = output_folder
        
        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)

    def cut_pdf(self):
        for data in glob.glob(os.path.join(self.path, '*.pdf')):
            try:
                # Load the PDF document
                doc = Document(data)

                # Get the first page
                page = doc.pages[0]

                # Define a rectangle for the part you want to cut
                rectangle = Rectangle(0, 0, 100, 100)  # Adjust these values as needed

                # Create a PNG image of the part of the page inside the rectangle
                image = page.get_image(rectangle)

                # Save the image to the output directory
                image_path = os.path.join(self.output_path, f'{os.path.basename(data)}.png')
                image.save(image_path)

            except (FileNotFoundError, IOError) as e:
                print(f"Error reading file {data}: {e}")
                
if __name__ == "__main__":
    cutter = Cutter()
    cutter.cut_pdf()
    print('Corte das páginas concluído.')