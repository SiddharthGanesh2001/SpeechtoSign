import speech_recognition as sr
from PIL import Image

r=sr.Recognizer()

# print(sr.Microphone.list_microphone_names())

with sr.Microphone(0) as source:
    print("Speak")
    r.adjust_for_ambient_noise(source)
    audio=r.listen(source, phrase_time_limit=7)

    try:
        text=r.recognize_google(audio)
        print("you said:{}".format(text))
        if(text=="sign language"):
            im=Image.open(r"C:\Users\siddh\Pictures\Saved Pictures\Ja mom.jpg")
            im.show()
        elif(text=="hello" or text=="hi" or text=="hey"):
            im=Image.open(r"C:\Users\siddh\PycharmProjects\speechrecognition\Pics\Hello.jpg")
            im.show()
        elif(text=="bye" or text=="goodbye"):
            im=Image.open(r"C:\Users\siddh\PycharmProjects\speechrecognition\Pics\Bye.jpg")
            im.show()
        elif(text=="yes" or text=="yeah" or text=="ja mom"):
            im=Image.open(r"C:\Users\siddh\PycharmProjects\speechrecognition\Pics\Yes.jpg")
            im.show()
        elif(text=="no" or text=="Nope" or text=="nein mom"):
            im=Image.open(r"C:\Users\siddh\PycharmProjects\speechrecognition\Pics\No.jpg")
            im.show()
        else:
            print("\nSpeech not recognized")

    except:
        print("Could not recognize speech")