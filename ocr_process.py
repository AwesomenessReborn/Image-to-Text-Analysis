import cv2
import pytesseract 

# NOTE python pytesseract and tesseract OCR are two different dependencies for the program to run. 
#       python pytesseract is not the core OCR engine, it uses tesseract OCR installation to 1` 
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

class PROFILE: 
    def __init__(self, first_name, last_name, image_destination): 
        self.first_name = first_name
        self.last_name = last_name
        self.cumulative_unweighted_GPA, self.cumulative_unweighted_GPA = self.read_GPA(pytesseract.image_to_string(cv2.imread("sample_transcript_1.png")))

    def read_GPA(self, raw_text): 
        lower_raw_text = raw_text.lower()       
        
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

        return UNWEIGHTED_GPA, WEIGHTED_GPA


sample_profile = PROFILE("John", "Smith", "sample_transcript_1.png")