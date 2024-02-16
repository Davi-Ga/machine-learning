from utils.extractor import Extractor
from utils.saver import Saver

if __name__ == "__main__":
    extractor = Extractor()
    info,pages=extractor.extract_info()
    saver = Saver('data/processos/Processo_0020641-26.2020.5.04.0663.pdf', 'data/extracted')
    saver.save_selected_pages(pages)
    print(info)
    print("\nPáginas: ",pages)
    