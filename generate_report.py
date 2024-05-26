def generate_html_report(extracted_text, result_image_path):
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Image Analysis Report</title>
    </head>
    <body>
        <h1>Image Analysis Report</h1>
        <h2>Extracted Text</h2>
        <p>{extracted_text}</p>
        <h2>Visual Elements</h2>
        <img src="{result_image_path}" alt="Segmented Visual Elements">
    </body>
    </html>
    """
    with open("report.html", "w") as report_file:
        report_file.write(html_content)
