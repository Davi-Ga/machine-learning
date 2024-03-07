import os
import glob
import pytesseract
import csv


class Labelling:

    def __init__(
        self,
        path="data/cuted",
        search_texts=[
            "ACORDAO",
            "DESPACHO",
            "SENTENCA",
            "NOTIFICACAO",
            "NOTIFICAGAO",
            "CERTIDAO",
            "INTIMACAO",
            "INTIMAGAO",
            "INTI MACAO",
            "Consulta",
            "ATA DE AUDIENCIA",
            "CITACAO",
            "CITAGAO",
            "CONCILIACAO",
            "TERMO",
            "CONSULTA",
            "DECISAO",
            "MANDADO",
            "AVALIACAO",
        ],
        output_folder="data/labelled",
    ):
        self.path = path
        self.output_folder = output_folder
        self.search_texts = search_texts

        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)

    def create(self):
        ignore_images = set()
        with open(f"{self.output_folder}/labelled_data.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Image_Path", "Label"])

            for image in sorted(glob.glob(os.path.join(self.path, "*.png"))):
                if image in ignore_images:
                    continue
                print(f"{image}")
                data = pytesseract.image_to_string(image)
                found = False
                for search_text in self.search_texts:
                    if search_text in data:
                        if search_text == "INTI MACAO":
                            search_text = search_text.replace(" ", "")
                        if search_text == "NOTIFICAGAO" or search_text == "INTIMAGAO" or search_text == "CITAGAO":
                            search_text = search_text.replace("G", "C")
                        writer.writerow([image, search_text])
                        ignore_images.add(image)
                        found = True
                        break

                if not found:
                    writer.writerow([image, ""])


if __name__ == "__main__":
    labelling = Labelling()
    labelling.create()
    print("Identificação das páginas concluída.")
