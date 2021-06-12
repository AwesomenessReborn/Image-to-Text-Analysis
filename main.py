import pytesseract 
from PIL import Image
import cv2

def general_process(): 
    image1 = Image.open("sample_transcript.png")
    text = pytesseract.image_to_string


def main(): 
    general_process()



#   Define later for analysis 
class StudentProfile: 
    """
        Start by creating a new profile for the image the student submits. 
    """
    def __init__(self, iamge, student_id, first_name, last_name):
        pass


if __name__ == "__main__": 
    main()