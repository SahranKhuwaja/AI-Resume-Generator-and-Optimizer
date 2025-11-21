import re

# Removing all special characters and all while preserving any urls and emails
pattern = re.compile(r'(https?://[^\s]+|www\.[^\s]+|[\w\.-]+@[\w\.-]+\.\w+)|[^\w\s]')

def preprocess(text: str):
    """Proprocess resume text by removing all special characters and all while 
       preserving any urls and emails"""
    data = text.lower()
    data = pattern.sub(lambda m: m.group(1) if m.group(1) else ' ', data)
    data = re.sub(r'\s+', ' ', data).strip().replace('_',' ')
    data = re.sub(r'(?<=[\w/])([.,;\'")]+)(\s|$)', r'\2', data)
    return data