# PDF Text Extractor

This project is a Python script that extracts text from a PDF file using the libraries pdf2image and pytesseract. It can handle PDF files in different languages, such as English and Russian.

## Motivation

The purpose of this project is to obtain specific data. Subsequently, this data will be necessary to generate the document.

## Installation

To run this project, you need to install the following dependencies:

- pdf2image: a Python module that wraps the pdftoppm and pdftocairo utilities to convert PDF to images
- pytesseract: a Python wrapper for Google's Tesseract-OCR engine
- poppler: a PDF rendering library that is required by pdf2image
- tesseract: an OCR engine that is required by pytesseract

You can install pdf2image and pytesseract using pip:

pip install pdf2image
pip install pytesseract

You also need to download and install poppler and tesseract from their official websites:

[poppler]
[tesseract]
Make sure to add the paths of poppler and tesseract to your system environment variables.

Usage
To use this project, you need to specify the following parameters in the script:

PDF_PATH: the path of the PDF file that you want to extract text from
LANGUAGES: the languages of the PDF file, separated by a plus sign (+)
DPI: resolution conversion accuracy
POPPLER_PATH: the path of the poppler library
TESSERACT_PATH: the path of the tesseract executable

The script will convert the PDF file into images and then extract text from each image using pytesseract. It will print the text to the standard output and also stop the execution if it finds a string that matches a certain pattern (a combination of dashes and slashes).

License
This project has not any license.