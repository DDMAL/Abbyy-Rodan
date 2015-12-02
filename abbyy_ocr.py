import subprocess
from rodan.jobs.base import RodanTask


class AbbyyOCR(RodanTask):
    name = "abbyy.abbyy_ocr"
    author = "Martha Thomae & Gabriel Vigliensoni"
    description = "Performs Abbyy OCR in document"
    settings = {}
    enabled = True
    category = "OCR"
    interactive = False

    input_port_types = [{
        'name': 'Input image',
        'resource_types': ['image/rgb+png'],
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
        subprocess.call('ls')
        return True

    def test_my_task(self, testcase):
        inputs = {
            'in': [
                {'resource_type': 'image/jpeg',
                 'resource_path': testcase.new_available_path()
                 }
            ]
        }
        PIL.Image.new("RGBA", size=(50, 50), color=(256, 0, 0)).save(inputs['in'][0]['resource_path'], 'JPEG')
        outputs = {
            'out': [
                {'resource_type': 'image/rgb+png',
                 'resource_path': testcase.new_available_path()
                 }
            ]
        }

        self.run_my_task(inputs, {}, outputs)
        result = PIL.Image.open(outputs['out'][0]['resource_path'])
        testcase.assertEqual(result.format, 'PNG')
