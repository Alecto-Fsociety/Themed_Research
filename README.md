# 📝 PDF Automation Tools

**PDF Automation Tools** is a collection of Python-based utilities designed to streamline the downloading, processing, and conversion of PDF documents. These tools automate fetching PDFs from websites, modifying their structure, and preparing them for further analysis.

This project was initially developed as part of a **school research project**, focusing on **automating the processing of past exam questions for automotive mechanics certification**. The system helps in structuring and digitizing past test materials to improve accessibility and study efficiency.

---

## **📌 Features**
🏙 **Automated PDF Downloading** - Fetches PDFs from structured web pages  
🌐 **PDF Image Extraction & OCR** - Converts PDFs to images and extracts text  
🛠 **Batch Processing** - Organizes and processes multiple files efficiently  
🌐 **Dependency-Free Execution** - Only requires Python3 with minimal dependencies  

---

## **🎅 Installation**
To ensure full functionality, install the required dependencies using the provided script.

```bash
chmod +x tools_install.sh
./tools_install.sh
```

Alternatively, install required packages manually:
```bash
sudo apt update && sudo apt install -y tesseract-ocr poppler-utils
pip3 install requests beautifulsoup4
```

---

## **🚀 Usage**
### **🔹 Download PDFs**
Use `pdf_downloader.py` to fetch PDFs from a list of predefined web pages.

```bash
python3 pdf_downloader.py
```

This script retrieves past exam papers from `jaspa.or.jp`, extracts relevant links, and downloads PDFs.

---

### **🔹 Process & Convert PDFs**
Use `PDF_Changer.py` to process downloaded PDFs, extract images, and perform OCR.

```bash
python3 PDF_Changer.py
```

💂 Output Directory Structure:
```
PDF/
 ├── <YEAR>/
 │   ├── <PDF_NAME>/
 │   │   ├── PDF_File/         # Original PDFs
 │   │   ├── Image_Date/       # Extracted images
 │   │   ├── Image_File/       # Individual pages
 │   │   ├── OCR_Text/         # Extracted text
 │   │   ├── word_file/        # (Optional) Converted Word documents
```

---

## **🛠 Script Breakdown**
### **1️⃣ `pdf_downloader.py`**
- **Fetches and downloads PDFs** from `https://www.jaspa.or.jp/mechanic/past/`
- Supports **batch downloading from multiple years**
- Saves files into a dedicated directory

### **2️⃣ `PDF_Changer.py`**
- **Extracts images from PDFs** using `pdftoppm`
- **Performs OCR text extraction** using `Tesseract`
- **Organizes results** into structured folders for easy access

### **3️⃣ `tools_install.sh`**
- **Sets up dependencies** required for PDF manipulation
- Ensures all necessary packages (`poppler-utils`, `tesseract`) are installed

---

## **⚠️ Disclaimer**
This tool is intended **for personal research and automation**.  
**Unauthorized use of web scraping on third-party websites may violate terms of service**.  

---

## **🐟 License**
This project is licensed under the **[MIT License](https://github.com/Alecto-Fsociety/Alecto-Fsociety/blob/main/LICENSE)**.  
Feel free to use, modify, and contribute!

---

## **🌍 Contributing**
💡 **Have ideas for improvement?**  
Open an issue or submit a pull request on **GitHub**!

---

## **💎 Contact**
Developer: **[Alecto-Fsociety](https://github.com/Alecto-Fsociety)**  
GitHub: **[https://github.com/Alecto-Fsociety](https://github.com/Alecto-Fsociety)**  
Proton Mail: **goodbye_friend1111@proton.me**
