import cv2

# Load the image
image_path = "cat.jpg"
image = cv2.imread(image_path)

# Load the Haar cascade for cat face detection
cat_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalcatface.xml')

# Check if the image and cascade were loaded properly
if image is not None and not cat_cascade.empty():
    # Convert image to grayscale (required for the Haar cascade)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect cat faces
    cat_faces = cat_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Draw rectangles around detected cat faces
    for (x, y, w, h) in cat_faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Show the result
    cv2.imshow("Cat Detection", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    if len(cat_faces) == 0:
        print("No cat detected.")
    else:
        print(f"Detected {len(cat_faces)} cat(s).")

else:
    print("Error loading the image or the cascade classifier.")