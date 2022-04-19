import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("firebasekey.json")
firebase_admin.initialize_app(cred)

app = firebase_admin.initialize_app(cred, {
    'storageBucket': 'gs://ethnomed-de562.appspot.com/',
}, name='storage')

bucket = storage.bucket(app=app)
blob = bucket.blob("puzzle-piece-template-13.png")

print(blob.generate_signed_url(datetime.timedelta(seconds=300), method='GET'))
