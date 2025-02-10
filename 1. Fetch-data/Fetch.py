import PyPDF2
import fitz
import os
from PIL import Image
def fetch_text(path: str) -> [str]:
    with open(path, 'rb') as pdf:
        reader = PyPDF2.PdfReader(pdf, strict=False)
        fetched_txt = []
        for page in reader.pages:
            txt = page.extract_text()
            fetched_txt.append(txt)
    return fetched_txt

def fetch_image(path: str):
    file = fitz.open(path)
    #Compute the number pages in the pdf
    page_counts = len(file)

    return 0
if '__main__' == __name__:
    #txt = fetch_text('UnderstandingDeepLearning_11_21_24_C.pdf')
    imgs = fetch_image('UnderstandingDeepLearning_11_21_24_C.pdf')
    """for word in txt:
        print(word)"""
