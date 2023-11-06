from setuptools import setup, find_packages

setup(
    name='kivy_convert_docx_to_pdf',
    version='0.1',
    packages=find_packages(),
    install_requires=open('requirements.txt').read().splitlines(),
    entry_points={
        'console_scripts': [
            'convert2pdf = app:main',
        ],
    },
)