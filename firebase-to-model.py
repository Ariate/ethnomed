import firebase_admin
from firebase_admin import credentials, firestore, storage
import datetime
import urllib.request
from PlantProgramRes import Ethnomed
from skimage import io


def main():  

    cred=credentials.Certificate(r'C:\Users\regdi\Documents\reg documents\Miscellaneous\Mark Desperation\ethnomed\firebasekey.json')
    firebase_admin.initialize_app(cred, {
        'storageBucket': 'ethnomed-de562.appspot.com'
    })
    db = firestore.client()

    bucket = storage.bucket()
    blob = bucket.blob("Guava.jpg")
    image_url = blob.generate_signed_url(datetime.timedelta(seconds=300), method='GET')
    
    Ethnomed(str(image_url))
    
    blob = bucket.blob("psd_img.png")
    blob.upload_from_filename("psd_img.png")

if __name__ == "__main__":
    main();