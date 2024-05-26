from generate_report import generate_html_report
from image_analysis import analyze_image

if __name__ == "__main__":
    image_path = "designelements.jpg"

    extracted_text, result_image_path = analyze_image(image_path)
    generate_html_report(extracted_text, result_image_path)

    print("Report generated: report.html")
