import cv2
from quickHand import HandDetector

# Pour la capture video:
# Vous pouvez passez en paramètre une valeur de -1 à 0 pour utiliser une webcam.
# Vous pouvez donner l'emplacement d'une vidéo. Exemple: "./videoAmusante.mp4" .
cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8,maxHands=2)

def main():
    while True:
        success, image = cap.read()
        detector.findHands(image, draw=False)#,flipType=False)

        cv2.imshow("Image", image)
        k = cv2.waitKey(1)
        if k == ord('q'):
            break

if __name__ == '__main__':
    main()
