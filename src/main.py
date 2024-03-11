from utils.extractor import Extractor
from utils.saver import Saver

if __name__ == "__main__":
    extractor = Extractor()
    info,pages=extractor.extract_info()
    saver = Saver('data/processos/Processo_0021099-48.2017.5.04.0663.pdf', 'data/extracted/process1')
    saver.save_selected_pages(pages)
    print(info)
    print("\nPáginas: ",pages)
    