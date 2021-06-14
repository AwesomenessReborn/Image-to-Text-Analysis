import cv2
import pytesseract

raw_image = cv2.imread("sample_transcript_1.png")
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

#   Show images if necessary
# cv2.imshow("raw image", cv2.resize(raw_image, None, fx=0.5, fy=0.5))
# cv2.imshow("black and white image", cv2.resize(cv2.cvtColor(raw_image, cv2.COLOR_BGR2GRAY), None, fx=0.5, fy=0.5))

# black_and_white_text = pytesseract.image_to_string(cv2.cvtColor(raw_image, cv2.COLOR_BGR2GRAY))
raw_text = pytesseract.image_to_string(raw_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

lower_raw_text = raw_text.lower()
# lower_black_and_white_text = black_and_white_text.lower()

print(lower_raw_text)
# print("""

# """)
# print(lower_black_and_white_text)


keywords_for_unweighted_GPA = ["cumulative unweighted gpa", "unweighted gpa"]

raw_unweighted_GPA_index = None
index_counter_for_unweigted_GPA = 0
for index_counter_for_unweigted_GPA, word in enumerate(keywords_for_unweighted_GPA): 
    try: 
        raw_unweighted_GPA_index = lower_raw_text.index(word)
        break
    except ValueError: 
        pass

print("REPORT FOR UNWEIGHTED GPA")
print("index is " + str(raw_unweighted_GPA_index))
print("text is: " + raw_text[raw_unweighted_GPA_index:(raw_unweighted_GPA_index + len(keywords_for_unweighted_GPA[index_counter_for_unweigted_GPA]))])

UNWEIGHTED_GPA = raw_text[(raw_unweighted_GPA_index + len(keywords_for_unweighted_GPA[index_counter_for_unweigted_GPA]) + 1):(raw_unweighted_GPA_index + len(keywords_for_unweighted_GPA[index_counter_for_unweigted_GPA]) + 1)+9]          #   9 characters after the keywords in theory should give the gpa format in 'x.xx/y.yy' 
print("Unweighted GPA is: " + UNWEIGHTED_GPA)

keywords_for_weighted_GPA = ["cumulative weighted gpa", "weighted gpa"]

raw_weighted_GPA_index = None
index_counter_for_weigted_GPA = 0
for index_counter_for_weigted_GPA, word in enumerate(keywords_for_weighted_GPA): 
    try: 
        raw_weighted_GPA_index = lower_raw_text.index(word)
        break
    except ValueError: 
        pass

print("REPORT FOR WEIGHTED GPA")
print("index is " + str(raw_weighted_GPA_index))
print("text is: " + raw_text[(raw_weighted_GPA_index):(raw_weighted_GPA_index + len(keywords_for_weighted_GPA[index_counter_for_weigted_GPA]))])

WEIGHTED_GPA = raw_text[(raw_weighted_GPA_index + len(keywords_for_weighted_GPA[index_counter_for_weigted_GPA]) + 1):(raw_weighted_GPA_index + len(keywords_for_weighted_GPA[index_counter_for_weigted_GPA]) + 1)+9]

print("Weighted GPA is: " + WEIGHTED_GPA)