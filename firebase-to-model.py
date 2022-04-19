import firebase_admin
from firebase_admin import credentials, firestore, storage
import datetime
import urllib.request
from skimage import io


def main():  

    cred=credentials.Certificate(r'C:\Users\regdi\Documents\reg documents\Miscellaneous\Mark Desperation\ethnomed\firebasekey.json')
    firebase_admin.initialize_app(cred, {
        'storageBucket': 'ethnomed-de562.appspot.com'
    })
    db = firestore.client()

    bucket = storage.bucket()
    blob = bucket.blob("puzzle-piece-template-13.png")
    image_url = blob.generate_signed_url(datetime.timedelta(seconds=300), method='GET')
    
    urllib.request.urlretrieve(image_url, r"C:\Users\regdi\Documents\reg documents\Miscellaneous\Mark Desperation\ethnomed")

if __name__ == "__main__":
    main();