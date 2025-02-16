import cv2

# Load our image
img = cv2.imread("conference.jpg")

# Initialize the face detector using the YuNet model
detector = cv2.FaceDetectorYN.create("model.onnx", "", (300,300))

# Set the input image size for the detector
img_h, img_w, _ = img.shape
detector.setInputSize((img_w, img_h))

# Perform face detection
detections = detector.detect(img)[1]

# If faces are detected, process each detected face
if detections is not None:
    for i in range(len(detections)):
        # Convert detection coordinates to integers
        output = [int(x) for x in detections[i,0:14]]

        # Extract face bounding box coordinates
        top_x, top_y, width, height = output[:4]

        # Extract facial landmark coordinates (fun stuff!)
        right_eye_x, right_eye_y = output[4:6]
        left_eye_x, left_eye_y = output[6:8]
        nose_tip_x, nose_tip_y = output[8:10]
        mouth_right_corner_x, mouth_right_corner_y = output[10:12]
        mouth_left_corner_x, mouth_left_corner_y = output[12:14]

        # Extract confidence score of the detected face
        face_score = detections[i,14]

        # Draw face box
        cv2.rectangle(img, (top_x, top_y), ((top_x + width), 
                                            (top_y + height)), (255,0,0), 2)
        
        # Draw right eye
        cv2.rectangle(img, (right_eye_x-2, right_eye_y-2), ((right_eye_x + 2, right_eye_y + 2)), (0,0,255), 1)

        # Draw left eye
        cv2.rectangle(img, (left_eye_x - 2, left_eye_y - 2), ((left_eye_x + 2, left_eye_y + 2)), (0,0,255), 1)

        # Draw nose tip
        cv2.rectangle(img, (nose_tip_x - 5, nose_tip_y - 5), (nose_tip_x + 5, nose_tip_y + 5), (0,255,0),1)

        # Draw rectangle around mouth
        cv2.rectangle(img, (mouth_left_corner_x, mouth_left_corner_y), (mouth_right_corner_x, mouth_right_corner_y), (100,100,100), 2)

        # Write face score
        cv2.putText(img, str(face_score), (top_x, top_y), cv2.FONT_HERSHEY_COMPLEX, 0.4, (255,0,0), 1)
        
        
cv2.imshow("Face Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
