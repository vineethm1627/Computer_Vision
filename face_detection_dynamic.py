import cv2
face_model = cv2.CascadeClassifier("haar-cascade-files/haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(0)
while True:

   ret,photo = cap.read()
   faces = face_model.detectMultiScale(photo, 1.2, 1)
   for (x,y,w,h) in faces:
       cv2.rectangle(photo, (x,y),(x+w , y+h), (0,255,0), 2)
   cv2.imshow("face",photo)
   if cv2.waitKey(10) & 0xFF == ord('q'):
       break

cv2.destroyAllWindows()
cap.release()