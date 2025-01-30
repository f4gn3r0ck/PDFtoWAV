import fitz  # PyMuPDF
import pyttsx3
import os
import time
import sys
from tkinter import Tk, filedialog

# Function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

# Function to convert text to speech and save as wav with progress bar
def text_to_speech(text, output_path):
    engine = pyttsx3.init()
    engine.save_to_file(text, output_path)
    
    # Initialize progress bar for TTS conversion
    total_length = len(text)
    chunk_size = total_length // 100
    
    for i in range(100):
        time.sleep(0.1)  # Simulate processing time
        sys.stdout.write('\r')
        sys.stdout.write("[%-100s] %d%%" % ('='*i, i+1))
        sys.stdout.flush()
    
    engine.runAndWait()

# Main function
def main():
    # Ask user to select a PDF file
    root = Tk()
    root.withdraw()  # We don't want a full GUI, so keep the root window from appearing
    pdf_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    
    if not pdf_path:
        print("No file selected. Exiting...")
        return
    
    text = extract_text_from_pdf(pdf_path)
    output_path = os.path.splitext(pdf_path)[0] + '.wav'
    text_to_speech(text, output_path)
    print(f"\nThe audio file has been saved as {output_path}.")

main()
