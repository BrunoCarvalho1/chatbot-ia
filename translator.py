import time
from deep_translator import GoogleTranslator

def translate_text_to_portuguese(text):
    translator = GoogleTranslator(source='english', target='portuguese')
    return translator.translate(text)


def translate_text_to_english(text):
    translator = GoogleTranslator(source='portuguese', target='english')
    return translator.translate(text)

