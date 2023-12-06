#!/bin/sh

apt update
apt upgrade -y

python3 -m pip install --upgrade pip 

pip install requests
pip install bs4 

apt install tesseract-ocr
apt install libtesseract-dev

apt install tesseract-ocr-jpn tesseract-ocr-jpn-vert
apt install tesseract-ocr-script-jpan tesseract-ocr-script-jpan-vert

apt install poppler-utils
