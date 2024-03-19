import os
import glob
import pytesseract
import csv
from dotenv import load_dotenv

load_dotenv("./.env")

CUTED_PATH = os.getenv("CUTED_PATH")


class Labelling:

    def __init__(
        self,
        path=CUTED_PATH,
        search_texts=[
            "ACORDAO",
            "DESPACHO",
            "SENTENCA",
            "NOTIFICACAO",
            "NOTIFICAGAO",
            "NOTI FICACAO",
            "NOTIFICAGCAO",
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
            "ALVARA",
            "CALCULO",
            "Imposto",
            "Calculo",
            "REQUISICAO",
            "RELATORIO",
        ],
        output_folder="data/labelled",
    ):
        self.path = path
        self.output_folder = output_folder
        self.search_texts = search_texts
        self.search_texts_to_replace = ["NOTIFICAGAO", "INTIMAGAO", "CITAGAO"]

        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)

    def create(self):
        ignore_images = set()
        filename = f"{self.output_folder}/labelled_data.csv"
        file_exists = os.path.isfile(filename)

        with open(filename, "a", newline="") as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(["Image_Path", "Label"])

            for image in sorted(glob.glob(os.path.join(self.path, "*.png"))):
                if image in ignore_images:
                    continue
                print(f"{image}")
                data = pytesseract.image_to_string(image)
                found = False
                for search_text in self.search_texts:
                    if search_text in data:
                        if search_text == "Calculo":
                            search_text = search_text.replace("C", "c")
                            search_text = search_text.upper()
                        if search_text == "INTI MACAO" or search_text == "NOTI FICACAO":
                            search_text = search_text.replace(" ", "")
                        if search_text in self.search_texts_to_replace:
                            search_text = search_text.replace("G", "C")
                        if search_text == "NOTIFICAGCAO":
                            search_text = search_text.replace("G", "")
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
