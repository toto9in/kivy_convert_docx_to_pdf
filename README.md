# kivy_convert_docx_to_pdf

This is a simple desktop application that allows you to convert docx and LibreOffice Writer files to PDF format. The program uses the Kivy framework for the graphical user interface and the LibreOffice converter tool to perform the conversion.

## Usage

To use the program, simply drag and drop a docx or LibreOffice Writer archive onto the main window of the program. The program will automatically convert the file to PDF format and save it to the documents folder of the system user.

## Requirements

To run the program, you will need to have the following software installed on your system:

- Python 3.10.12 (version used and tested)
- Kivy framework
- LibreOffice installed in the machine

## Installation

To install the program, follow these steps:

1. Create a virtual environment: `python -m venv env`
2. Activate the virtual environment: `source env/bin/activate` (Linux/Mac) or `env\Scripts\activate` (Windows)
3. Clone the repository to your local machine.
4. Install the required dependencies using pip: `pip install -r requirements.txt`
5. Build the executable using PyInstaller: `pyinstaller --onefile main.py`
6. The executable will be created in the `dist` folder.

OBS: pyinstaller==5.0 was used because was the tested version

## License

This program is licensed under the MIT License. See the `LICENSE` file for more information.
