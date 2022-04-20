def Ethnomed(img_str):
    import numpy as np
    from skimage import io
    from cv2 import cv2
    import io as io2
    import base64

    plant_cascade=cv2.CascadeClassifier(r'./localpackage/cascade.xml')

    encoded_data = img_str.split(',')[1]
    nparr = np.fromstring(encoded_data.decode('base64'), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    plants = plant_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in plants:
        cv2.rectangle(img,(x,y),(x+w,y+h), (255,0,0), 2)

        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
    
    is_success, buffer = cv2.imencode(".jpg", img)
    byte_img = buffer.tobytes()

    
    return byte_img

    