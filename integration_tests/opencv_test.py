from . import EngineCase


class OpenCVTest(EngineCase):
    engine = 'opencv_engine'

    def test_single_params(self):
        self.exec_single_params()
