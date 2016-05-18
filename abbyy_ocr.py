#--------------------------------------------------------------------------------------------------
# Program Name:         abbyy_ocr.py
# Program Description:  Job wrappers for ABBYY to work inside Rodan, in order to use
#                       the capabilities of OCR from the first inside a Rodan workflow
#--------------------------------------------------------------------------------------------------

import subprocess
from rodan.jobs.base import RodanTask

class AbbyyOCR(RodanTask):
    """Wrap ABBYY inside Rodan."""
    name = "OCR image with ABBYY"
    author = "Martha Thomae & Gabriel Vigliensoni"
    description = "Performs Abbyy OCR in document"
    settings = {
        'title': 'Abbyy processing/recognition keys',
        'type': 'object',
        'properties': {
            'Languages' : {
                'enum': ['English', 'Italian'],
                'type': 'string',
                'default': 'English',
                'description': 'Language given as a parameter to the recognition key (-rl)'
            }
        }
    }
    enabled = True
    category = "OCR"
    interactive = False

    input_port_types = [{
        'name': 'Input image for OCR',
        'resource_types': [
            'image/onebit+png', 'image/rgb+png', 'image/greyscale+png', 'image/grey16+png',
            'image/png', 'image/jpeg', 'image/jp2', 'image/tiff',
            'image/bmp', 'image/x-pcx', 'image/x-dcx',
            'application/pdf'
            ],
        'minimum': 1,
        'maximum': 1
    }]
    output_port_types = [{
        'name': 'Output file: Abbyy XML',
        'resource_types': ['application/abbyy+xml'],
        'minimum': 1,
        'maximum': 1
    },
    {
        'name': 'Output file: text',
        'resource_types': ['text/plain'],
        'minimum': 1,
        'maximum': 1
    }]

    def run_my_task(self, inputs, settings, outputs):
        """Send the command line instruction to perform OCR with ABBYY, given the input and output files and the languate settings selected by the user."""
        # The 3 parameters we are giving Abbyy to do OCR: the input and output files, and the language recognition key
        input_file = inputs['Input image for OCR'][0]['resource_path']
        output_file_xml = outputs['Output file: Abbyy XML'][0]['resource_path']
        output_file_text = outputs['Output file: text'][0]['resource_path']
        language_recognition_key = ""
        if settings['Languages'] == 0:
            language_recognition_key = "English"
        elif settings['Languages'] == 1:
            language_recognition_key = "Italian"
        format_options_xml = "XML"
        format_options_text = "TextUnicodeDefaults -tet UTF8"
        # CL Abbyy instruction for OCR
        subprocess.call(["abbyyocr11", "-rl", language_recognition_key, "-if", input_file, "-f", format_options_text, "-of", output_file_text, "-f", format_options_xml, "-of", output_file_xml])

        return True