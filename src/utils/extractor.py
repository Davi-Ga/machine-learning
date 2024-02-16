from collections import defaultdict
from .formater import Formater


class Extractor:
    def __init__(self):
        self.formater = Formater()
        self.info = defaultdict(list)
        print("Iniciando extração de informações...")

    def __str__(self):
        """Return a string representation of the extracted information."""
        return "\n".join(f"{k}: {v}" for k, v in self.info.items())

    def get_process_number(self):
        """Extract process numbers from PDF files."""
        return self.formater.extract_from_pdf(
            r"\b(\d{7}-\d{2}\.\d{4}\.\d{1}\.\d{2}\.\d{4})"
        )

    def get_claimant(self):
        """Extract claimants from PDF files."""
        return self.formater.extract_from_pdf(r"(?:RECLAMANTE|AUTOR): (\w+)")

    def extract_info(self):
        """Extract process numbers and claimants from PDF files."""
        process_nums = self.get_process_number()
        claimants = self.get_claimant()
        info = defaultdict(list)
        pages= []
        print('Iniciando extração de informações...')
        for (process_num, process_page), (claimant, claimant_page) in zip(process_nums, claimants):
            info[process_num].append((claimant, claimant_page))
            pages.append(claimant_page)
        return info,list(dict.fromkeys(pages))