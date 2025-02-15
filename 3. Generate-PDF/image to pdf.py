from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from PIL import Image
# Import Pillow to get image size

def insert_image_into_pdf(image, output, x, y, s):

    """
    :param image: Path to the image to insert.
    :param output: Name of the output PDF file.
    :param x: X-coordinate for the image.
    :param y: Y-coordinate for the image.
    :param s: Scale factor
    :return:
    """

    img = Image.open(image)
    o_w, o_h = img.size
    # Original width and height of image

    n_w = int(o_w * s)
    n_h = int(o_h * s)
    # New width and height after applying scale factor

    c = canvas.Canvas(output, pagesize=letter)
    # Create a PDF canvas

    c.drawImage(image, x, y, width=n_w, height=n_h)
    #Draw image at (x,y) with specified Height and Weight

    c.save()
    print(f"PDF has generated")

if __name__ == "__main__":
    #Test
    x = 0  # X position (left)
    y = 0  # Y position (bottom)
    s = 0.2 # 20% of the original size
    image = "image.jpg"  # Change to your image file
    output = "output.pdf"  # Output PDF filename
    insert_image_into_pdf(image, output, x, y, s)
