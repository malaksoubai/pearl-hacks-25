import cv2
import time
import pyautogui
import shutil
import os
#workshop
# Initialize the face detector with the YuNet model


detector = cv2.FaceDetectorYN.create("model.onnx", "", (300, 300))

# Set up video capture from camera (index 1) (or index 0, you may have to try both)
cv2.namedWindow("cam")
capture = cv2.VideoCapture(0)

screenshots_folder = "screenshots"

if(os.path.exists(screenshots_folder)):
    #Clear old screenshots from folder
    shutil.rmtree(screenshots_folder)


# Check if the camera is accessible
if capture.isOpened():
    rval, frame = capture.read()
    img_w, img_h = frame.shape[1], frame.shape[0]
    detector.setInputSize((img_w, img_h))
else:
    rval = False

def is_eye_contact(right_eye_x, left_eye_x, img_w):
    center_x = img_w/2
    threshold = 40
    if abs(right_eye_x - center_x) < threshold and abs(left_eye_x - center_x) < threshold:
        return True
    return False

saved_time = time.time()


# Main loop for real-time face detection
while rval:
    rval, frame = capture.read()
    if not rval:
        break

    # Detect faces in the current frame
    detections = detector.detect(frame)[1]

    if detections is not None:
        for i in range(len(detections)):
            # Convert detection coordinates to integers
            output = [int(x) for x in detections[i,:14]]

            # Extract face bounding box
            top_x, top_y, width, height = output[:4]

            # Extract facial landmark coordinates
            right_eye_x, right_eye_y = output[4:6]
            left_eye_x, left_eye_y = output[6:8]
            nose_tip_x, nose_tip_y = output[8:10]
            mouth_right_corner_x, mouth_right_corner_y = output[10:12]
            mouth_left_corner_x, mouth_left_corner_y = output[12:14]

            # Extract face confidence score
            face_score = detections[i, 14]

            # Draw bounding box around detected face
            cv2.rectangle(frame, (top_x, top_y), (top_x + width, top_y + height), (255, 0, 0), 2)

            # Draw facial landmarks
            cv2.rectangle(frame, (right_eye_x - 2, right_eye_y - 2), (right_eye_x + 2, right_eye_y + 2), (0, 0, 255), 1)
            cv2.rectangle(frame, (left_eye_x - 2, left_eye_y - 2), (left_eye_x + 2, left_eye_y + 2), (0, 0, 255), 1)
            cv2.rectangle(frame, (nose_tip_x - 5, nose_tip_y - 5), (nose_tip_x + 5, nose_tip_y + 5), (0, 255, 0), 1)
            cv2.rectangle(frame, (mouth_left_corner_x, mouth_left_corner_y), (mouth_right_corner_x, mouth_right_corner_y), (100, 100, 100), 2)

            # Display face detection confidence score
            cv2.putText(frame, f"{face_score:.2f}", (top_x, top_y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.4, (255, 0, 0), 1)
            if not is_eye_contact(right_eye_x, left_eye_x, img_w):
                cv2.putText(frame, "LOOK AT ME", (50, 50), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0), 2)
            
            current_time = time.time()
            if saved_time is None or current_time - saved_time >= 20:
                #Save to screenshots folder
                pic_name = os.path.join(screenshots_folder, f"screenshot_{int(current_time)}.png")
                screenshot = pyautogui.screenshot()
                snapshot = cv2.imwrite(pic_name, frame)
                print("Screenshot saved!")
                saved_time = current_time

    # Show the video feed with detections
    cv2.imshow("cam", frame)
       

    # Exit loop when 'Esc' key (27) is pressed
    if cv2.waitKey(27) == 27:
        break

# Release resources
capture.release()
cv2.destroyAllWindows()
