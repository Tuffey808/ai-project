import re

def clean_text(text):
    text = re.sub(r'\s+', ' ', text)  # Remove multiple spaces
    text = text.strip()
    return text
