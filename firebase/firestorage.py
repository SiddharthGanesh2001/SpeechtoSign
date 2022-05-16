import pyrebase
from pyrebase.pyrebase import Storage

filename = []
firebaseConfig = {
    "apiKey": "AIzaSyCKSoDJgv6WRCuMBGcKw3nq4UDka4dav80",
    "authDomain": "speech-to-sign-c57bc.firebaseapp.com",
    "databaseURL": "https://speech-to-sign-c57bc-default-rtdb.firebaseio.com",
    "projectId": "speech-to-sign-c57bc",
    "storageBucket": "speech-to-sign-c57bc.appspot.com",
    "messagingSenderId": "710870747341",
    "appId": "1:710870747341:web:aad7280fd8b52090a84184",
    "measurementId": "G-KDGWK7MJD6",
    "serviceAccount":"speech-to-sign-c57bc-firebase-adminsdk-5yye7-3ca72567cf.json",
}


firebase = pyrebase.initialize_app(firebaseConfig)

storage = firebase.storage()
list1 = storage.list_files()

for name in list1:
    filename.append(name.name)

print(filename)
# img = "D:\github\Speech-to-Sign\SIGNS\\nice.jpg"
# storage.child("nice").put(img)

def checkImg(img):
    count = filename.count(img)
    return count
    # for name in list1:
    #     print(name.name)
    # count = list1.count(img)
    # return count

def getImgUrl(img):
    auth = firebase.auth()
    email ="developersshelby@gmail.com"
    password = "123456"
    user = auth.sign_in_with_email_and_password(email,password)
    url = storage.child(img).get_url(user['idToken'])
    # print(url)
    return url


