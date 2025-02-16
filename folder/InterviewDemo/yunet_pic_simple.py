import cv2

# load our image
img = cv2.imread("patient.png")

# initialize the face detector using the YuNet model
detector = cv2.FaceDetectorYN.create("model.onnx", "", (300,300))

# set the input image size for the detector
img_h, img_w, _ = img.shape
detector.setInputSize((img_w, img_h))

# perform face detection
detections = detector.detect(img)[1]

# if face(s) are detected, process the first detected face
if detections is not None:
        # Convert detection coordinates to integers
        output = [int(x) for x in detections[0,0:14]]

        # Extract face bounding box coordinates
        top_x, top_y, width, height = output[:4]

        # Draw face box
        cv2.rectangle(img, (top_x, top_y), ((top_x + width),    #B,G,R
                                            (top_y + height)), (0,255,0), 5)

cv2.imshow("Face Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
