def Ethnomed(image_url):
    import numpy as np
    from skimage import io
    from cv2 import cv2

    plant_cascade=cv2.CascadeClassifier(r'cascade.xml')

    
    img = io.imread(image_url)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    plants = plant_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in plants:
        cv2.rectangle(img,(x,y),(x+w,y+h), (255,0,0), 2)

        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
    
    is_success, buffer = cv2.imencode(".jpg", img)
    io_buf = io.BytesIO(buffer)
    
    decode_img = cv2.imdecode(np.frombuffer(io_buf.getbuffer(), np.uint8), -1)
    
    return decode_img

    