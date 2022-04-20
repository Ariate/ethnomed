def main(request):  
    import firebase_admin
    from firebase_admin import credentials, firestore, storage
    import datetime
    import json
    from localpackage.PlantProgramRes import Ethnomed

    request_json = request.get_json(silent=True)

    image = request_json['encoded']['image']
    status = Ethnomed(image)
    print (status)
    data_set = {"status": status}
    json_dump = json.dumps(data_set)
    json_object = json.loads(json_dump)
    
    return json_object
            
    # Firebase Store 
    # cred=credentials.Certificate(r'firebasekey.json')
    # firebase_admin.initialize_app(cred, {
    #     'storageBucket': 'ethnomed-de562.appspot.com'
    # })
    # db = firestore.client()
    
    # bucket = storage.bucket()
    # blob = bucket.blob("raw_img.jpg")
    # image_url = blob.generate_signed_url(datetime.timedelta(seconds=300), method='GET')


    