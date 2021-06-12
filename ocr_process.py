import cv2
import pytesseract 
import numpy as np

img = cv2.imread("sample_transcript_1.png")

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

final_text = pytesseract.image_to_string(img)

print(final_text)

cv2.imshow("TRANSCRIPT", img)
cv2.waitKey(0)