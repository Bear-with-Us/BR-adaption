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


def fetch_image(path: str, folder: str) -> None:
    file = fitz.open(path)
    # Compute the number pages in the pdf
    page_counts = len(file)
    image_list = []
    for page_num in range(page_counts):
        content = file[page_num]
        image_list.extend(content.get_images())
    # [(reference number, , width, height, , color space)]
    if len(image_list) == 0:
        raise ValueError('No Image found')
    for index, image in enumerate(image_list, start=1):
        ref_num = image[0]
        # Extract image
        base_img = file.extract_image(ref_num)

        img_byte = base_img['image']
        # Store image extension/format
        img_format = base_img['ext']
        # Generate image file name
        img_name = str(index) + '.' + img_format
        with open(os.path.join(f"{folder}/", img_name), 'wb') as image_file:
            image_file.write(img_byte)
            image_file.close()
    return 0


if '__main__' == __name__:
    txt = fetch_text('UnderstandingDeepLearning_11_21_24_C.pdf')
    fetch_image('UnderstandingDeepLearning_11_21_24_C.pdf', 'images')
    for word in txt:
        print(word)
