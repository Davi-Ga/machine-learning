import os
import PyPDF2
import shutil

class Saver:
    def __init__(self, pdf_file, output_folder):
        self.pdf_file = pdf_file
        self.output_folder = output_folder
        self.reader = PyPDF2.PdfReader(self.pdf_file)

    def _is_page_number_valid(self, page_num):
        return 1 <= page_num <= len(self.reader.pages)

    def _save_page_as_pdf(self, page_nums):
        writer = PyPDF2.PdfWriter()  # Create a new PdfWriter instance for each page
        for page_num in page_nums:
            print(page_num)
            if self._is_page_number_valid(page_num):
                writer.add_page(self.reader.pages[page_num - 1])
        output_file = f"{self.output_folder}/group_{page_nums[0]}_to_{page_nums[-1]}.pdf"
        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)
        with open(output_file, 'wb') as output_pdf:
            writer.write(output_pdf)
        print('-----------------------------')
        print(f"Saved pages {page_nums} to {output_file}")
        
    def create_and_expand_groups(self, pages):
        groups = []
        for i in range(len(pages)):
            group = [pages[i]]
            if i != len(pages) - 1 and pages[i+1] != pages[i] + 1:
                group.extend(range(pages[i] + 1, pages[i+1]))
            groups.append(group)
        print("Grupos de páginas:",groups)
        return groups

    def save_selected_pages(self, pages):
        for group in self.create_and_expand_groups(pages):
            self._save_page_as_pdf(group)