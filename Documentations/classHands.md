## La classe **Hands**:
>Toute la documentation est en anglais et j'ai pas le moindrement envie de traduire. Considéré ceci comme un exercise pour pratiquee votre anglais. ✌️
### 1. Options de configurations:
   ```py
   mp_hand.Hands(static_image_mode=False,      
                   min_detection_confidence=0.7,
                   min_tracking_confidence=0.7,
                   max_num_hands=2)
   ```
- **static_image_mode**: Indicates if the input images should be treated as independent and non related (True) or should be treated as a video stream (False). We are going to set the value to False, which means that, after a successful detection of hands in the video frame, the algorithm will localize the landmarks and, in subsequent frames, it will simply track the landmarks without invoking another detection, until it loses track of any of the hands.
  
- **max_num_hands**: Maximum number of hands to be detected. Although this parameter defaults to 2, we will explicitly set this field to the same value, to illustrate its usage.
  
- **min_detection_confidence**: Minimum confidence value (between 0 and 1) for the hand detection to be considered successful. We will set it to 0.7.

- **min_tracking_confidence**: Minimum confidence value (between 0 and 1) for the hand landmarks to be considered tracked successfully. We will set it to 0.7.

### 2. Sortie/Output

Naming style may differ slightly across platforms/languages.

- **MULTI_HAND_LANDMARKS**
Collection of detected/tracked hands, where each hand is represented as a list of 21 hand landmarks and each landmark is composed of x, y and z. x and y are normalized to [0.0, 1.0] by the image width and height respectively. z represents the landmark depth with the depth at the wrist being the origin, and the smaller the value the closer the landmark is to the camera. The magnitude of z uses roughly the same scale as x.

- **MULTI_HAND_WORLD_LANDMARKS**
Collection of detected/tracked hands, where each hand is represented as a list of 21 hand landmarks in world coordinates. Each landmark is composed of x, y and z: real-world 3D coordinates in meters with the origin at the hand’s approximate geometric center.

- **MULTI_HANDEDNESS**
Collection of handedness of the detected/tracked hands (i.e. is it a left or right hand). Each hand is composed of label and score. label is a string of value either "Left" or "Right". score is the estimated probability of the predicted handedness and is always greater than or equal to 0.5 (and the opposite handedness has an estimated probability of 1 - score).

Note that handedness is determined assuming the input image is mirrored, i.e., taken with a front-facing/selfie camera with images flipped horizontally. If it is not the case, please swap the handedness output in the application.

### 3. Exemple simple
```py
import cv2
import mediapipe as mp

mp_draw = mp.solutions.drawing_utils
mp_hand = mp.solutions.hands

capture = cv2.VideoCapture(0)

with mp_hand.Hands(static_image_mode=False,
                   min_detection_confidence=0.7,
                   min_tracking_confidence=0.7,
                   max_num_hands=2) as hands:

    while (True):
        ret, frame = capture.read()
        results = hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

        if results.multi_hand_landmarks != None:
            for handLandmarks in results.multi_hand_landmarks:
                mp_draw.draw_landmarks(frame, handLandmarks, mp_hand.HAND_CONNECTIONS)

        cv2.imshow('Test hand', frame)
        if cv2.waitKey(1) == 27:
            break

cv2.destroyAllWindows()
capture.release()
```
