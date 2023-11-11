import pdf2image
import pytesseract
import sys

from pytesseract import Output

PDF_PATH = "crm.pdf"
LANGUAGES = "eng+rus"
DPI = 900
POPPLER_PATH = r"C:\Program Files\Poppler\Library\bin"
TESSERACT_PATH = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

try:
    images = pdf2image.convert_from_path(PDF_PATH, DPI, poppler_path=POPPLER_PATH)
except FileNotFoundError:
    print(f"File {PDF_PATH} does not exist. Please check the file path and try again.")
    sys.exit()

pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH

for image in images:
    parsed_dict = pytesseract.image_to_data(image, lang=LANGUAGES, output_type=Output.DICT)

    text = ' '.join(parsed_dict["text"])
    while '  ' in text:
        text = text.replace('  ', ' ')

    for element in text.split(' '):
        if '-' in element and '/' in element and len(element) == 24:
            print(element)
            sys.exit()
