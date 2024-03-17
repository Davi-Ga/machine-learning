from utils.extractor import Extractor
from utils.saver import Saver
from settings import EXTRACTED_PATH

if __name__ == "__main__":
    extractor = Extractor()
    info,pages=extractor.extract_info()
    saver = Saver('data/processos/Processo_0021280-49.2017.5.04.0663.pdf', EXTRACTED_PATH)
    saver.save_selected_pages(pages)
    print(info)
    print("\nPáginas: ",pages)
    