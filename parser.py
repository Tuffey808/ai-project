import spacy
nlp = spacy.load("en_core_web_sm")

from utils.extract_text import extract_text_from_pdf
from utils.preprocess import clean_text
from utils.skill_matcher import extract_skills
import spacy

nlp = spacy.load("en_core_web_sm")

class ResumeParser:
    def __init__(self, file_path):
        self.text = clean_text(extract_text_from_pdf(file_path))
        self.doc = nlp(self.text)

    def get_name(self):
        for ent in self.doc.ents:
            if ent.label_ == "PERSON":
                return ent.text

    def get_skills(self):
        return extract_skills(self.text)

    def get_education(self):
        return [ent.text for ent in self.doc.ents if ent.label_ == "ORG"]
