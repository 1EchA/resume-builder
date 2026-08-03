"""
Generate a PDF from an HTML resume file using Playwright.

Usage:
    python generate_pdf.py <input.html> [output.pdf]

If output is not specified, it defaults to the input filename with .pdf extension.
Requires: pip install playwright && python -m playwright install chromium
"""
import sys
import os
from playwright.sync_api import sync_playwright


def generate_pdf(html_path, pdf_path=None):
    if not os.path.exists(html_path):
        print(f"Error: {html_path} not found")
        sys.exit(1)

    if pdf_path is None:
        pdf_path = os.path.splitext(html_path)[0] + '.pdf'

    abs_html = os.path.abspath(html_path).replace('\\', '/')
    file_url = f'file:///{abs_html}'

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(file_url)
        page.wait_for_timeout(3000)  # Wait for fonts to load
        page.pdf(
            path=pdf_path,
            format='A4',
            margin={
                'top': '10mm',
                'right': '8mm',
                'bottom': '10mm',
                'left': '8mm'
            },
            print_background=True
        )
        browser.close()

    print(f"PDF generated: {pdf_path}")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    html_file = sys.argv[1]
    pdf_file = sys.argv[2] if len(sys.argv) > 2 else None
    generate_pdf(html_file, pdf_file)
