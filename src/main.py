from utils.extractor import Extractor
from utils.saver import Saver
from settings import EXTRACTED_PATH,PROCESS_SAVE_PATH

if __name__ == "__main__":
    extractor = Extractor()
    info,pages=extractor.extract_info()
    saver = Saver(PROCESS_SAVE_PATH, EXTRACTED_PATH)
    saver.save_selected_pages(pages)
    print(info)
    print("\nPáginas: ",pages)
    