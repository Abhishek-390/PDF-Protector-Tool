# PDF Password Protector

This is a simple Python script that adds password protection to a PDF file using the `PyPDF2` library.

## Features

- Takes an input PDF file.
- Protects it with a password.
- Saves the password-protected file as a new output PDF.

## Requirements

- Python 3.x
- `PyPDF2` library

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/yourusername/protect-pdf.git
    cd protect-pdf
    ```

2. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. You will need **PyPDF2** to run the script. You can install it directly by running:

    ```bash
    pip install PyPDF2
    ```

## Usage

Run the script from the command line:

```bash
python protect_pdf_clean.py input.pdf output.pdf password
