import speech_recognition as sr

r = sr.Recognizer()

# Get the audio input from the mic.
with sr.Microphone() as source:
    print("Speak now...")
    audio_input = r.listen(source)
text = r.recognize_google(audio_input)
print("opening letter to principal.pdf")
import PyPDF2

pdf_file = PyPDF2.PdfReader('ie.pdf')
# print(pdf_file)
num_pages = pdf_file.numPages

page = pdf_file.getPage(0)

page_text = page.extractText()
print(page_text)

# alphabet = {'a':[1,0,0,0,0,0],
#             'b':[1,1,0,0,0,0],
#             'c':[1,0,0,1,0,0],
#             'd':[1,0,0,1,1,0],
#             'e':[1,0,0,0,1,0],
#             'f':[1,1,0,1,0,0],
#             'g':[1,1,0,1,1,0],
#             'h':[1,1,0,0,1,0],
#             'i':[0,1,0,1,0,0],
#             'j':[0,1,0,1,1,0],
#             'k':[1,0,1,0,0,0],
#             'l':[1,1,1,0,0,0],
#             'm':[1,0,1,1,0,0],
#             'n':[1,0,1,1,1,0],
#             '0':[1,0,1,0,1,0],
#             'p':[1,1,1,1,0,0],
#             'q':[1,1,1,1,1,0],
#             'r':[1,1,1,0,1,0],
#             's':[0,1,1,1,0,0],
#             't':[0,1,1,1,1,0],
#             'u':[1,0,1,0,0,1],
#             'v':[1,0,1,0,0,1],
#             'w':[0,1,0,1,1,1],
#             'x':[0,0,1,1,0,1],
#             'y':[1,0,1,1,1,1],
#             'z':[1,0,1,0,1,1],
#             ' ':[0,0,0,0,0,0]
#           }

# import pyttsx3
# engine = pyttsx3.init()
# engine.say("Hello")
# # hel = input()
# for h in page_text:
#     print(h)
#     print(alphabet.get(h))