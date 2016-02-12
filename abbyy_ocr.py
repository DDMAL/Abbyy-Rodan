#--------------------------------------------------------------------------------------------------
# Program Name:         abbyy_ocr.py
# Program Description:  Job wrappers for ABBYY to work inside Rodan, in order to use
#                       the capabilities of OCR form the first, inside a Rodan workflow
# WORK IN PROGRESS
#--------------------------------------------------------------------------------------------------
##import PIL.Image
import subprocess
from rodan.jobs.base import RodanTask

class AbbyyOCR(RodanTask):
    name = "abbyy.abbyy_ocr"
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
        'name': 'input_image',
        'resource_types': [
            'image/png', 'image/jpeg', 'image/jp2', 'image/tiff',
            'image/bmp', 'image/x-pcx', 'image/x-dcx',
            'application/pdf'
            ],
        'minimum': 1,
        'maximum': 1
    }]
    output_port_types = [{
        'name': 'export_file',
        'resource_types': ['application/abbyy+xml'],
        'minimum': 1,
        'maximum': 1
    }]

    def run_my_task(self, inputs, settings, outputs):
        # The 3 parameters we are giving Abbyy to do OCR: the input and output files, and the language recognition key
        input_file = inputs['input_image'][0]['resource_path']
        output_file = outputs['export_file'][0]['resource_path']
        language_recognition_key = ""
        if settings['Languages'] == 0:
        	language_recognition_key = "-rl English"
        else if settings['Languages'] == 1:
        	language_recognition_key = "-rl Italian"
        # CL Abbyy instruction for OCR
        abbyy_instruction = "abbyyocr11 " + language_recognition_key + " -if " + input_file  + " -f " + "XML" + " -of " + output_file
        subprocess.call(abbyy_instruction)
        return True

    # # Still in process
    # def test_my_task(self, testcase):
    # # Test formats
    #     outputs = {
    #         'export_file': [
    #             {'resource_type': 'application/abbyy+xml',
    #              'resource_path': testcase.new_available_path()
    #             }
    #         ]
    #     }

    #     inputs = {
    #         'input_image': [
    #             {'resource_type': 'image/png',
    #              'resource_path': testcase.new_available_path()
    #             }
    #         ]
    #     }
    #     PIL.Image.new("RGBA", size=(50, 50), color=(256, 0, 0)).save(inputs['input_image'][0]['resource_path'], 'PNG')
    #     self.run_my_task(inputs, {}, outputs)
    #     #result = PIL.Image.open(outputs['export_file'][0]['resource_path'])	# IT IS AN XML, SO THESE TWO LINES MAY BE USELESS!
    #     #testcase.assertEqual(result.format, 'XML')

    #     inputs = {
    #         'input_image': [
    #             {'resource_type': 'image/jpeg',
    #              'resource_path': testcase.new_available_path()
    #             }
    #         ]
    #     }
    #     PIL.Image.new("RGBA", size=(50, 50), color=(256, 0, 0)).save(inputs['input_image'][0]['resource_path'], 'JPEG')
    #     self.run_my_task(inputs, {}, outputs)
    #     #result = PIL.Image.open(outputs['export_file'][0]['resource_path'])
    #     #testcase.assertEqual(result.format, 'XML')

    #     inputs = {
    #         'input_image': [
    #             {'resource_type': 'image/jp2',
    #              'resource_path': testcase.new_available_path()
    #             }
    #         ]
    #     }
    #     PIL.Image.new("RGBA", size=(50, 50), color=(256, 0, 0)).save(inputs['input_image'][0]['resource_path'], 'JPEG2000')
    #     self.run_my_task(inputs, {}, outputs)
    #     #result = PIL.Image.open(outputs['export_file'][0]['resource_path'])
    #     #testcase.assertEqual(result.format, 'XML')

    #     inputs = {
    #         'input_image': [
    #             {'resource_type': 'image/tiff',
    #              'resource_path': testcase.new_available_path()
    #             }
    #         ]
    #     }
    #     PIL.Image.new("RGBA", size=(50, 50), color=(256, 0, 0)).save(inputs['input_image'][0]['resource_path'], 'TIFF')
    #     self.run_my_task(inputs, {}, outputs)
    #     #result = PIL.Image.open(outputs['export_file'][0]['resource_path'])
    #     #testcase.assertEqual(result.format, 'XML')

    #     inputs = {
    #         'input_image': [
    #             {'resource_type': 'image/bmp',
    #              'resource_path': testcase.new_available_path()
    #             }
    #         ]
    #     }
    #     PIL.Image.new("RGBA", size=(50, 50), color=(256, 0, 0)).save(inputs['input_image'][0]['resource_path'], 'BMP')
    #     self.run_my_task(inputs, {}, outputs)
    #     #result = PIL.Image.open(outputs['export_file'][0]['resource_path'])
    #     #testcase.assertEqual(result.format, 'XML')

    #     inputs = {
    #         'input_image': [
    #             {'resource_type': 'image/x-pcx',
    #              'resource_path': testcase.new_available_path()
    #             }
    #         ]
    #     }
    #     PIL.Image.new("RGBA", size=(50, 50), color=(256, 0, 0)).save(inputs['input_image'][0]['resource_path'], 'PCX')
    #     self.run_my_task(inputs, {}, outputs)
    #     #result = PIL.Image.open(outputs['export_file'][0]['resource_path'])
    #     #testcase.assertEqual(result.format, 'XML')

    #     inputs = {
    #         'input_image': [
    #             {'resource_type': 'image/x-dcx',
    #              'resource_path': testcase.new_available_path()
    #             }
    #         ]
    #     }
    #     PIL.Image.new("RGBA", size=(50, 50), color=(256, 0, 0)).save(inputs['input_image'][0]['resource_path'], 'DCX')
    #     self.run_my_task(inputs, {}, outputs)
    #     #result = PIL.Image.open(outputs['export_file'][0]['resource_path'])
    #     #testcase.assertEqual(result.format, 'XML')

    #     inputs = {
    #         'input_image': [
    #             {'resource_type': 'application/pdf',
    #              'resource_path': testcase.new_available_path()
    #             }
    #         ]
    #     }
    #     PIL.Image.new("RGBA", size=(50, 50), color=(256, 0, 0)).save(inputs['input_image'][0]['resource_path'], 'PDF')
    #     self.run_my_task(inputs, {}, outputs)
    #     #result = PIL.Image.open(outputs['export_file'][0]['resource_path'])
    #     #testcase.assertEqual(result.format, 'XML')