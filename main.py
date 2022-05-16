import eel
import sys
import os
import time

import speech_recognition as sr
from PIL import Image
from firebase import firestorage

eel.init('frontend')

@eel.expose()
def displayImage(word):
    # count = firestorage.checkImg(word)
    # if count ==0:
    #     return 0
    try:
        # if word =="are":
        #     return 0            
        # else:
        eel.deleteImg()
        img = firestorage.getImgUrl(word)
        eel.displayImg(word,img)
        time.sleep(1)
        return 1

    except Exception as e:
        print(e)
        return 0



# getting text from speech
@eel.expose()
def getTextfromSpeech():
    i=0
    r=sr.Recognizer()
    # print(sr.Microphone.list_microphone_names())

    with sr.Microphone(2) as source:
        print("Speak")
        eel.displayText("Speak")
        # r.adjust_for_ambient_noise(source)
        audio=r.listen(source, phrase_time_limit=5)
        eel.MicOff()

        
        text=r.recognize_google(audio)
        # text = text.lower()
        words = text.split(" ")
        print(words)
        print("you said:{}".format(text))
        eel.displayText(text)

        for i in range(0,len(words)):
            # count = firestorage.checkImg(words[i])
            # print(count);
            if (words[i] == "are" or words[i]=="am"):
                continue
            elif(words[i] == "I"):
                displayImage("me")
            else:
                flag = firestorage.checkImg(words[i])
                # print(flag)
                if(flag == 0):
                    for word in words[i]:
                        displayImage(word)
                        time.sleep(2)
                else:
                    displayImage(words[i])

            time.sleep(2)

            # if(text=="sign language"):
            #     im=Image.open(r"D:\minipro\SIGNS\signs.jpg")
            #     im.show()
            # elif(text=="hello" or text=="hi" or text=="hey"):
            #     # im=Image.open(r"D:\minipro\SIGNS\hello.jpg")
            #     # im.show()
            #     # img = await firestorage.getImgUrl("hello.jpg")
            #     eel.displayImg("Hello","D:\minipro\SIGNS\hello.jpg")

            # elif(text=="bye" or text=="goodbye"):
            #     im=Image.open(r"D:\minipro\SIGNS\goodbye.jpg")
            #     im.show()
            # elif(text=="yes" or text=="yeah" or text=="ja mom"):
            #     im=Image.open(r"D:\minipro\SIGNS\yes.jpg")
            #     im.show()
            # elif(text=="no" or text=="Nope" or text=="nein mom"):
            #     im=Image.open(r"D:\minipro\SIGNS\no.jpg")
            #     im.show()
            # else:
            #     print("\nSpeech not recognized")
            
       



eel.start('html/homepage.html', size = (1000,800), position = (10,10))
