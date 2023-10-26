import sys,os,pathlib,subprocess,glob,itertools,shutil,random

#bash_file_setup = subprocess.call(["chmod","x+","tools_install.sh"],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
#bash_file_start = subprocess.call(["./tools_install.sh"],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)

import requests # docx
from bs4 import BeautifulSoup

def pdf_changer(main_path="PDF",pdf_date="PDF_File",path_image="Image_Date",image_file_path="Image_File",path_ocr="OCR_Text",word_file="word_file",path_name="../pdf_path/*.pdf",cycle=itertools.cycle(r"/-\|")):

    pathlib.Path(main_path).mkdir(exist_ok=True)

    for path_date in glob.glob(path_name):

        file_name = os.path.splitext(os.path.basename(path_date))[0]

        file_path_year = file_name.split("_")[0]
        pathlib.Path(f"{main_path}/{file_path_year}").mkdir(exist_ok=True)
        pathlib.Path(f"{main_path}/{file_path_year}/{file_name}").mkdir(exist_ok=True)
       
        # PDF & PDF_Change_Image & Image_Write_OCR & PDF_File 
        pathlib.Path(f"{main_path}/{file_path_year}/{file_name}/{pdf_date}").mkdir(exist_ok=True) # PDF_File
        pathlib.Path(f"{main_path}/{file_path_year}/{file_name}/{path_image}").mkdir(exist_ok=True) # PDF_Change_Image
        pathlib.Path(f"{main_path}/{file_path_year}/{file_name}/{image_file_path}").mkdir(exist_ok=True) # PDF_Image
        pathlib.Path(f"{main_path}/{file_path_year}/{file_name}/{path_ocr}").mkdir(exist_ok=True) # Image_Write_OCR
        #pathlib.Path(f"{main_path}/{file_path_year}/{file_name}/{word_file}").mkdir(exist_ok=True) # Word_File

        sys.stdout.write("\r")
        sys.stdout.write(f"PDF_Change... < {path_date} > ~ {next(cycle)}")
        sys.stdout.flush()

        path_date_name = os.path.basename(path_date)

        shutil.copyfile(path_date,f"{main_path}/{file_path_year}/{file_name}/{pdf_date}/{path_date_name}")

        pdftoppm_date = subprocess.call(["pdftoppm","-png",path_date,f"{main_path}/{file_path_year}/{file_name}/{path_image}/{file_name}"],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
        
        pdfimages_date = subprocess.call(["pdfimages","-png",path_date,f"{main_path}/{file_path_year}/{file_name}/{image_file_path}/{file_name}"],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)

        for image_path in pathlib.Path(f"{main_path}/{file_path_year}/{file_name}/{path_image}").glob("*"):

            image_path_name = os.path.splitext(os.path.basename(image_path))[0]

            tesseract_date = subprocess.call(["tesseract",image_path,f"{main_path}/{file_path_year}/{file_name}/{path_ocr}/{image_path_name}","-l","jpn"],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)

        #for ocr_text in pathlib.Path(f"{main_path}/{file_path_year}/{file_name}/{path_ocr}").mkdir(exist_ok=True):

            #docx_file = os.path.splitext(os.path.basename(ocr_text))[0]

            #doc = docx.Document()

            #for file_date in open(ocr_text,"r",encoding="utf-8").readlines():

                #doc.add_paragraph(file_date)

            #doc.save(f"{main_path}/{file_path_year}/{file_name}/{word_file}/{docx_file}")

               
def main():

    pdf_changer()        

if __name__ == "__main__":

  main()

