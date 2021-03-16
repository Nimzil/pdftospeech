from pdfReader import DocReader
from txtSpeech import TextToSpeech

pdfRead = DocReader


def toText():
    path = 'test file.pdf'
    text = pdfRead.convert_pdf_to_txt(path)
    return text


def toSpeech(text):
    textspeech = TextToSpeech(text)
    textspeech.convertText()


toSpeech(toText())
