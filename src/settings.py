from dotenv import load_dotenv
import os

load_dotenv('./.env')

CUTED_PATH = os.getenv('CUTED_PATH')
EXTRACTED_PATH = os.getenv('EXTRACTED_PATH')
PROCESS_SAVE_PATH = os.getenv('PROCESS_SAVE_PATH')