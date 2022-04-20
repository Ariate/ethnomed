import firebase_admin
from firebase_admin import credentials, firestore, storage
import datetime
from localpackage.PlantProgramRes import Ethnomed


def main(request):  

    # Firebase Store 
    cred=credentials.Certificate(r'firebasekey.json')
    firebase_admin.initialize_app(cred, {
        'storageBucket': 'ethnomed-de562.appspot.com'
    })
    db = firestore.client()

    bucket = storage.bucket()
    blob = bucket.blob("raw_img.jpg")
    image_url = blob.generate_signed_url(datetime.timedelta(seconds=300), method='GET')
    
    Ethnomed(str(image_url))
    
    blob = bucket.blob(r"localpackage\psd_img.png")
    blob.upload_from_filename("psd_img.png")
    
    return request

if __name__ == "__main__":
    main();