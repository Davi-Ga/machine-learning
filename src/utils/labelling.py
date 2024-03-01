import os
import glob
import pytesseract
import csv

class Labelling:
    
    def __init__(self, path='data/tests', search_texts=["ACORDAO"], output_folder='data/labelled'):
        self.path = path
        self.output_folder = output_folder
        self.search_texts = search_texts
        
        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)

    def create(self):
        with open(f'{self.output_folder}/labelled_data.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Image_Path", "Label"])
            
            for image in glob.glob(os.path.join(self.path, '*.png')):
                data = pytesseract.image_to_string(image)
                
                for search_text in self.search_texts:
                    if search_text in data:
                        writer.writerow([image, search_text])
                            
if __name__ == "__main__":
    labelling = Labelling()
    labelling.create()
    print('Identificação das páginas concluída.')