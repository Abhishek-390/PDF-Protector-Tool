import sys
import os
from PyPDF2 import PdfReader, PdfWriter

print("✅ Script started")

if len(sys.argv) != 4:
    print("⚠️ Usage: python3 protect_pdf_clean.py input.pdf output.pdf password")
    sys.exit(1)

input_pdf = sys.argv[1]
output_pdf = sys.argv[2]
password = sys.argv[3]

print(f"📄 Input PDF: {input_pdf}")
print(f"💾 Output PDF: {output_pdf}")
print(f"🔑 Password: {password}")

if not os.path.exists(input_pdf):
    print(f"❌ File not found: {input_pdf}")
    sys.exit(1)

try:
    print("📂 Reading input PDF...")
    reader = PdfReader(input_pdf)
    writer = PdfWriter()

    for i, page in enumerate(reader.pages, start=1):
        writer.add_page(page)
        print(f"✅ Added page {i}")

    print("🔒 Encrypting PDF...")
    writer.encrypt(password)

    with open(output_pdf, "wb") as f:
        writer.write(f)

    print(f"🎉 Protected PDF created: {output_pdf}")
    print(f"🔑 Use this password to open: {password}")

except Exception as e:
    print(f"⚠️ Error: {e}")
