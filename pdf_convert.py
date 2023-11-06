

#checks if the actual plataform is windows or linux
import os
import platform
import subprocess

def convert_to_pdf(input_file_path):
    """Converts a docx file to pdf"""
    if platform.system() == 'Windows':
        libreoffice_path = r"C:\Program Files\LibreOffice\program\swriter.exe"
    else:
        libreoffice_path = "libreoffice"
    
    output_file_path = os.path.join(os.path.expanduser("~"), "Documents", os.path.splitext(os.path.basename(input_file_path))[0] + ".pdf")
    
    convertion = subprocess.call([libreoffice_path, '--convert-to', 'pdf', '--outdir', os.path.dirname(output_file_path), input_file_path])

    if convertion == 0:
        return True
    else:
        return False
    
