import os
import PyPDF2

class Saver:
    def __init__(self, pdf_file, output_folder):
        self.pdf_file = pdf_file
        self.output_folder = output_folder
        self.reader = PyPDF2.PdfReader(self.pdf_file)

    def _is_page_number_valid(self, page_num):
        return 1 <= page_num <= len(self.reader.pages)

    def _save_page_as_pdf(self, page_num):
        writer = PyPDF2.PdfWriter()  # Create a new PdfWriter instance for each page
        writer.add_page(self.reader.pages[page_num - 1])
        output_file = f"{self.output_folder}/page_{page_num}.pdf"
        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)
        with open(output_file, 'wb') as output_pdf:
            writer.write(output_pdf)

    def save_selected_pages(self, pages):
        for page_num in pages:
            if not self._is_page_number_valid(page_num):
                print(f"Page number {page_num} is not valid.")
                continue
            self._save_page_as_pdf(page_num)