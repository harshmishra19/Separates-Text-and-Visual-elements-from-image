import cv2
import pytesseract


def analyze_image(image_path):
    # Load the image
    img = cv2.imread(image_path)

    # Text extraction using Tesseract OCR
    extracted_text = pytesseract.image_to_string(img)

    # Visual element segmentation using OpenCV
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200)

    # Find contours
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw bounding boxes around contours
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Save the result image
    result_image_path = "result_image.png"
    cv2.imwrite(result_image_path, img)

    return extracted_text, result_image_path
