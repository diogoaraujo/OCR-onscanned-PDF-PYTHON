import glob
from PIL import Image
import pytesseract as pt

pt.pytesseract.tesseract_cmd = r'C:\Users\araujo\AppData\Local\tesseract.exe'
images = glob.glob("./rotating/*.jpg")
for image in images:
    img = Image.open(image)
    data = pt.image_to_string(img, lang='eng', config='--psm 6')
    print(data,file=open('extract-text.txt',"a"))
