import pytesseract
from PIL import Image

for i in range(0, 9):
    img = Image.open(f"DataForOCR/{i}.jpeg")
    pytesseract.pytesseract.tesseract_cmd = r"Tesseract-OCR\tesseract.exe"

    text = pytesseract.image_to_string(img, lang="rus")
    print(text.strip())

    with open(f'DataForOCR/{i}.jpeg', 'a', encoding='utf-8') as f:
        f.write(text.strip()+"\n")

        text = pytesseract.image_to_string(img)
        print(text)

        with open('passport.cv2', 'a', encoding='UTF-8') as f:
            f.write(text+"\n")




    # import pytesseract
    # from PIL import Image
    #
    # img = Image.open("DataForOCR/1.jpeg")
    # pytesseract.pytesseract.tesseract_cmd = r"E:\Алия\Tesseract-OCR\tesseract.exe"
    #
    # custom_config = r'--oem 3 --psm 13'