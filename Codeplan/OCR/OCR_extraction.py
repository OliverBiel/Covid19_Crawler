from PIL import Image
import pytesseract


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

print(pytesseract.image_to_string(Image.open('image.png'), lang='eng'))
print("+==========================================================+")
print(pytesseract.image_to_string('image2.png'))