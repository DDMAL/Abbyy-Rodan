#--------------------------------------------------------------------------------------------------
# Program Name:         abbyy_ocr.py
# Program Description:  Job wrappers for ABBYY to work inside Rodan, in order to use
#                       the capabilities of OCR form the first, inside a Rodan workflow
# WORK IN PROGRESS
#--------------------------------------------------------------------------------------------------
import subprocess
from rodan.jobs.base import RodanTask

class AbbyyOCR(RodanTask):
    name = "abbyy.abbyy_ocr"
    author = "Martha Thomae & Gabriel Vigliensoni"
    description = "Performs Abbyy OCR in document"
    settings = {
        'title': 'Abbyy processing/recognition keys',
        'type': 'object', 
        'properties' : {
            'Languages' : {
                'enum' : ['English', 'Italian'], 
                'type' : 'string', 
                'default' : 'English'
                'description': 'Language given as a parameter to the recognition key (-rl)'
            } 
        } 
    }
    enabled = True
    category = "OCR"
    interactive = False

    input_port_types = [{
        'name': 'Input image',
        'resource_types': ['image/png',
                           'image/rgb+png',
                           'image/greyscale+png',
                           'image/grey16+png',
                           'image/onebit+png',
                           'image/jpeg',
                           'image/jp2',
                           'image/tiff',
                           'image/bmp',
                           'application/pdf',
                           'image/x-pcx',
                           'image/x-dcx'],
        'minimum': 1,
        'maximum': 1
    }]
    output_port_types = [{
        'name': 'Output XML',
        'resource_types': ['application/abbyy+xml'],
        'minimum': 1,
        'maximum': 1
    }]

    def run_my_task(self, inputs, settings, outputs):
        # The 3 parameters we are giving Abbyy to do OCR: the input and output files, and the language recognition key
        input_file = inputs['input_image'][0]['resource_path']  # Question (the fixed number --> gives me some trouble with the definition of the input dictionary in the test_my_task method)
        output_file = outputs['export_file'][0]['resource_path']
        language_recognition = "-rl " + settings['properties']['Languages']['default']  # For now it is "English" --> at which stage is this parameter defined? 
        # CL Abbyy instruction for OCR
        abbyy_instruction = "abbyyocr11 " + language_recognition + " -if " + input_file  + " -f " + "XML" + " -of " + output_file
        subprocess.call(abbyy_instruction)
        return True

    # Still in process
    # def test_my_task(self, testcase):
    #     inputs ={
    #         'input_image' : [ {'resource_path' : testcase.new_available_path() , 'resource_type' : 'image/png'},
    #                     {'resource_path' : testcase.new_available_path() , 'resource_type' : 'image/rgb+png'},
    #                     {'resource_path' : testcase.new_available_path() , 'resource_type' : 'image/greyscale+png'},
    #                     {'resource_path' : testcase.new_available_path() , 'resource_type' : 'image/grey16+png'},
    #                     {'resource_path' : testcase.new_available_path() , 'resource_type' : 'image/onebit+png'},
    #                     {'resource_path' : testcase.new_available_path() , 'resource_type' : 'image/jpeg'},
    #                     {'resource_path' : testcase.new_available_path() , 'resource_type' : 'image/jp2'},
    #                     {'resource_path' : testcase.new_available_path() , 'resource_type' : 'image/tiff'},
    #                     {'resource_path' : testcase.new_available_path() , 'resource_type' : 'image/bmp'},
    #                     {'resource_path' : testcase.new_available_path() , 'resource_type' : 'image/x-pcx'},
    #                     {'resource_path' : testcase.new_available_path() , 'resource_type' : 'image/x-dcx'},
    #                     {'resource_path' : testcase.new_available_path(), 'resource_type' : 'application/pdf'} ] }
    #     outputs = { 'export_file' : [{'resource_path' : testcase.new_available_path() , 'resource_type' : 'application/abbyy+xml'}] }
    #     self.run_my_task(inputs, {}, outputs)