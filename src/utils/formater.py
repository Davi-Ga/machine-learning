import os
import re
import glob
import PyPDF2


class Formater:

    def __init__(self, path="data/processos"):
        """Initialize the Formater with a default path to PDF files."""
        self.path = path

    def extract_from_pdf(self, pattern):
        results = []
        for data in glob.glob(os.path.join(self.path, "*.pdf")):
            
            try:
                with open(data, "rb") as file:
                    reader = PyPDF2.PdfReader(file)
                    for i, page in enumerate(reader.pages, start=1):
                        lines = page.extract_text().split("\n")
                        for line in lines:
                            if re.search(pattern, line):
                                results.append((line, i))
            except (FileNotFoundError, IOError) as e:
                print(f"Error reading file {data}: {e}")
        print(results)
        return results

