import pdfplumber
import re

def extract_text_from_pdf(filepath):
    pages_text = []
    with pdfplumber.open(filepath) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text is not None:
                pages_text.append(text)
    joined = "\n".join(pages_text)
    return clean_text(joined)

def clean_text(text):
    text = re.sub(r".*university.*", "", text, flags=re.IGNORECASE)
    text = re.sub(r"page \d+" , "", text, flags=re.IGNORECASE)
    text = re.sub(r"time:.*" , "", text)
    text = re.sub(r"max.*\d+" , "", text)
    text = re.sub(r".*college.*", "", text, flags=re.IGNORECASE)
    text = re.sub(r".*department.*", "", text, flags=re.IGNORECASE)
    text = re.sub(r".*your name.*", "", text, flags=re.IGNORECASE)
    text = re.sub(r".*roll no.*", "", text, flags=re.IGNORECASE)
    text = re.sub(r".*unit.*", "", text, flags=re.IGNORECASE)
    text = re.sub(r".*assignment.*", "", text, flags=re.IGNORECASE)
    text = re.sub(r".*internal assesment.*", "", text, flags=re.IGNORECASE)
    text = re.sub(r".*b tech.*", "", text, flags=re.IGNORECASE)
    text = re.sub(r".*technological university.*", "", text, flags=re.IGNORECASE)
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"part [a-d]", "", text, flags=re.IGNORECASE)
    text = re.sub(r"co-\d+", "", text, flags=re.IGNORECASE)
    text = re.sub(r"page \d+ of \d+", "", text, flags=re.IGNORECASE)
    text = re.sub(r"reg no.*", "", text, flags=re.IGNORECASE)
    text = re.sub(r"course code:.*", "", text, flags=re.IGNORECASE)
    text = re.sub(r"course name:.*", "", text, flags=re.IGNORECASE)
    text = re.sub(r"duration:.*", "", text, flags=re.IGNORECASE)
    text = re.sub(r"\d{14,}", "", text)  
    return text



if __name__ == "__main__":
    text = extract_text_from_pdf("pyq.pdf")
    print(text[:500])