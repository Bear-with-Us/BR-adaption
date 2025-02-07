import PyPDF2

def fetch_text(path):

    with open(path, 'rb') as pdf:
        reader = PyPDF2.PdfReader(pdf, strict=False)
        fetched_txt = []

        for page in reader.pages:
            txt = page.extract_text()
            fetched_txt.append(txt)
    return fetched_txt




if '__main__' == __name__:

    txt = fetch_text('UnderstandingDeepLearning_11_21_24_C.pdf')
    for word in txt:
        print(word)