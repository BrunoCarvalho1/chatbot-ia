import time
from deep_translator import GoogleTranslator


def translate_text(text):
    # Instância do translator
    translator = GoogleTranslator(source='english', target='portuguese')
    return translator.translate(text)

