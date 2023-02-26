from pdf2image import  convert_from_path
import  pytesseract
import util
from PIL import Image

from parser_prescription import PrescriptionParser
from parser_patient_details import PatientDetailsParser

pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files\Tesseract-OCR\tesseract.exe"
POPPLERPATH=r"C:\poppler-23.01.0\Library\bin"



def extract(filepath,file_format):





    pages=convert_from_path(filepath,poppler_path=POPPLERPATH)

    document_text=''


    for page in pages:
        processed_image=util.processed_img(page)
        text = pytesseract.image_to_string(processed_image, lang="eng")
        document_text += text



    # return document_text

    if file_format=='prescription':
        extracted_data=PrescriptionParser(document_text).parse()


    elif file_format=='patient_details':
        extracted_data=PatientDetailsParser(document_text).parse()

    else:
        raise Exception(f'unsupported file format: {file_format}')



    return extracted_data


if __name__=='__main__':
   data = extract('../resources/prescription/pre_2.pdf','prescription')


   print(data)
