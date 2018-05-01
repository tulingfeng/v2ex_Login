import pytesseract
from PIL import Image
'''
旨在采用tesseract ocr来识别验证码
'''
# pytesseract.pytesseract.tesseract_cmd = 'D:/Program Files (x86)/Tesseract-OCR/tesseract'
image=Image.open("captcha.jpg")
image=image.convert("L")
# 获得指定磁盘位置的图片可以用类似：img=Image.open(r'C:\Users\libanggeng\Pictures\idcard\id_card.jpg')
print(image)
result=pytesseract.image_to_string(image,lang='chi_sim')
print(result)
