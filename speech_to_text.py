#Reference for converting speech to text
#Thepythoncode.com. 2021. How to Convert Speech to Text in Python - Python Code. [online] Available at: <https://www.thepythoncode.com/article/using-speech-recognition-to-convert-speech-to-text-python> [Accessed 11 September 2021].
import speech_recognition as sr
filename = "OSR_us_000_0010_8k.wav"
# initialize the recognizer
r = sr.Recognizer()
# open the file
with sr.AudioFile(filename) as source:
    # listen for the data (load audio to memory)
    audio_data = r.record(source)
    # recognize (convert from speech to text)
    text = r.recognize_google(audio_data)
    #print(text)

#Writing the text into another file
report = open("report.txt", 'a')
report.write(text + "\n")
report.close()
