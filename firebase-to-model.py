import firebase_admin
from firebase_admin import credentials, firestore, storage
import datetime
import requests


def main():  

    cred=credentials.Certificate(r'C:\Users\regdi\Documents\reg documents\Miscellaneous\Mark Desperation\ethnomed\firebasekey.json')
    firebase_admin.initialize_app(cred, {
        'storageBucket': 'ethnomed-de562.appspot.com'
    })
    db = firestore.client()

    bucket = storage.bucket()
    blob = bucket.blob("puzzle-piece-template-13.png")
    image_url = blob.generate_signed_url(datetime.timedelta(seconds=300), method='GET')
    
    img_data = requests.get(image_url).content
    with open('puzzle-piece-template-13.png', 'wb') as handler:
        handler.write(img_data)

if __name__ == "__main__":
    main();