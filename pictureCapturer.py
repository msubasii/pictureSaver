import cv2
import threading
import os

save_folder = "captured_images"
if not os.path.exists(save_folder):
    os.makedirs(save_folder)

# video yakalaması burada oluyor
cap = cv2.VideoCapture(0)

# 1.jpg 2.jpg şeklinde olsun diye count
image_count = 0

#klasöre save ediyorum
def save_frame(frame, count):
    filename = os.path.join(save_folder, f"{count}.jpg")
    cv2.imwrite(filename, frame)

    print(f"Image {count} saved as {filename}")

#görüntüyü alıyorum
def capture_images():
    global image_count
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # ekranda camera görüntüsü
        cv2.imshow('Camera', frame)

        # kaydetme butonu "s"
        key = cv2.waitKey(1)
        if key == ord('s'):
            image_count += 1
            #threading ile image_count ile save ediyo
            thread = threading.Thread(target=save_frame, args=(frame, image_count))
            thread.start()

        #çıkış için "q"
        if key == ord('q'):# Press 'q' to quit
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    capture_images()