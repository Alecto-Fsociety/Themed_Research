#!/bin/sh

apt update
apt upgrade -y

python3 -m pip install --upgrade pip 

pip install requests
pip install bs4 

apt install tesseract-ocr -y 
apt install libtesseract-dev -y 

apt install tesseract-ocr-jpn  tesseract-ocr-jpn-vert -y
apt install tesseract-ocr-script-jpan tesseract-ocr-script-jpan-vert -y 

apt install poppler-utils -y
