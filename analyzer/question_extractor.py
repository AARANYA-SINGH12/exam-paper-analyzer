import re

def extract_questions(text, year):
    questions = []
    chunks = re.split(r"\n\d+\s", text)

    for chunk in chunks:
        chunk = chunk.strip()
        if len(chunk) < 15:
            continue

        if "semester" in chunk.lower() or "examination" in chunk.lower():
            continue

        match = re.search(r"\((\d+)\)", chunk)
        if match:
            marks = int(match.group(1))
        else:
            marks = 0
        
        entry = {
            "text" : chunk,
            "year": year,
            "marks": marks
        }

        questions.append(entry)
        
    return questions

if __name__ == "__main__":
    from pdf_parser import extract_text_from_pdf
    text = extract_text_from_pdf("pyq.pdf")
    questions = extract_questions(text, 2022)
    for q in questions:
        print(q)
        print("---")