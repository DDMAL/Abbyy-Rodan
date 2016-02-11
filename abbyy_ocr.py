import subprocess
from rodan.jobs.base import RodanTask


class AbbyyOCR(RodanTask):
    name = "abbyy.abbyy_ocr"
    author = "Martha Thomae & Gabriel Vigliensoni"
    description = "Performs Abbyy OCR in document"
    settings = { 'properties' : {'Languages' : {'enum' : ['English', 'Italian'], 'type' : 'string' , 'default' : 'English'} } }    enabled = True
    category = "OCR"
    interactive = False

    input_port_types = [{
        'name': 'Input image',
        'resource_types': ['image/png', 'image/rgb+png', 'image/greyscale+png', 'image/grey16+png', 'image/onebit+png', 'image/jpeg', 'image/jp2', 'image/tiff', 'image/bmp', 'application/pdf', 'image/x-pcx', 'image/x-dcx'],        'minimum': 1,
        'maximum': 1
    }]
    output_port_types = [{
        'name': 'Output XML',
        'resource_types': ['application/abbyy+xml'],
        'minimum': 1,
        'maximum': 1
    }]

    def run_my_task(self, inputs, settings, outputs):
        input_file = inputs['input_image'][0]['resource_path']
        output_file = outputs['export_file'][0]['resource_path']
        abbyy_instruction = "abbyyocr11 " + "-rl LANGUAGE" + " -if " + input_file  + " -f " + "XML" + " -of " + output_file   #still missing opt_if and ofile
        subprocess.call(abbyy_instruction)
        return True

    def test_my_task(self, testcase):
        inputs ={#does the number of keys depends on the number of input ports? the minimum and maximum is 1, so only 1 key?
            'input_image' : [ {'resource_path' : testcase.new_available_path() , 'resource_type' : 'image/png'},
                        {'resource_path' : testcase.new_available_path() , 'resource_type' : 'image/rgb+png'},
                        {'resource_path' : testcase.new_available_path() , 'resource_type' : 'image/greyscale+png'},
                        {'resource_path' : testcase.new_available_path() , 'resource_type' : 'image/grey16+png'},
                        {'resource_path' : testcase.new_available_path() , 'resource_type' : 'image/onebit+png'},
                        {'resource_path' : testcase.new_available_path() , 'resource_type' : 'image/jpeg'},
                        {'resource_path' : testcase.new_available_path() , 'resource_type' : 'image/jp2'},
                        {'resource_path' : testcase.new_available_path() , 'resource_type' : 'image/tiff'},
                        {'resource_path' : testcase.new_available_path() , 'resource_type' : 'image/bmp'},
                        {'resource_path' : testcase.new_available_path() , 'resource_type' : 'image/x-pcx'},
                        {'resource_path' : testcase.new_available_path() , 'resource_type' : 'image/x-dcx'},
                        {'resource_path' : testcase.new_available_path(), 'resource_type' : 'application/pdf'} ] }
        outputs = { 'export_file' : [{'resource_path' : testcase.new_available_path() , 'resource_type' : 'application/abbyy+xml'}] }
        self.run_my_task(inputs, {}, outputs)