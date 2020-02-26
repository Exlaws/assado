import pytesseract
from PIL import Image

pytesseract .pytesseract.tesseract_cdm = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

img = Image.open('image.jpg')
text = pytesseract.image_to_string(img)
print(text)
