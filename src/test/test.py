import os
import re
import glob
import PyPDF2
import nltk
from nltk.corpus import stopwords
from collections import defaultdict

def extract_from_pdf(pattern, path='data/processos'):
    results = []
    for data in glob.glob(os.path.join(path, '*.pdf')):
        with open(data, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for i, page in enumerate(reader.pages, start=1):
                lines = page.extract_text().split('\n')
                for line in lines:
                    if re.search(pattern, line):
                        results.append((line, i))
    return results

def get_process_number():
    return extract_from_pdf(r'\b(\d{7}-\d{2}\.\d{4}\.\d{1}\.\d{2}\.\d{4})')

def get_claimant():
    return extract_from_pdf(r'RECLAMANTE: (\w+)')

def extract_info():
    process_nums = get_process_number()
    claimants = get_claimant()
    info = defaultdict(list)
    print('Iniciando extração de informações...')
    for (process_num, process_page), (claimant, claimant_page) in zip(process_nums, claimants):
        info[process_num].append((claimant, claimant_page))
    return info

print(extract_info())

