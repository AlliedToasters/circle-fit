import unittest
import time
from circle_fit import riemannSWFLa, lm, prattSVD, taubinSVD, hyperSVD, kmh, hyperLSQ, standardLSQ
import numpy as np

class AppTest(unittest.TestCase):

    def setUp(self):
        self.startTime = time.time()
        self.data = [
            [329.4165297387034, 22058.59654729173],
            [329.8574976938737, 22054.62783124933],
            [328.9755617834489, 22051.98202025803],
            [327.6526579178539, 22049.77717811104],
            [326.3297510885569, 22047.57233566768],
            [324.1249083488352, 22045.36749322432],
            [321.9200656090292, 22043.60361962528],
            [319.7152228693075, 22041.83974572986],
            [317.0694121744155, 22041.39877718193],
            [314.4236014794393, 22040.5168403824],
            [311.7777907845473, 22040.07587183446],
            [309.1319800895711, 22040.5168403824],
            [305.6042334842544, 22041.39877718193],
            [302.5174548341079, 22042.72168252938],
            [299.8716441392159, 22044.04458787685],
            [298.1077693546644, 22046.24943032021],
            [296.343894570113, 22048.4542724672]
        ]
        self.numpy_data = np.array(self.data)

    def tearDown(self):
        t = time.time() - self.startTime
        print("%s: %.3f seconds" % (self.id(), t))

    def test_hyperLSQ(self):
        circle = hyperLSQ(self.data)
        circle = hyperLSQ(self.numpy_data)

    def test_standardLSQ(self):
        circle = standardLSQ(self.data)
        circle = standardLSQ(self.numpy_data)

    def test_riemannSWFLa(self):
        circle = riemannSWFLa(self.data)
        circle = riemannSWFLa(self.numpy_data)

    def test_lm(self):
        par_ini = np.array([310, 22060, 20])
        circle = lm(self.data, par_ini)
        circle = lm(self.numpy_data, par_ini)

    def test_prattSVD(self):
        circle = prattSVD(self.data)
        circle = prattSVD(self.numpy_data)

    def test_taubinSVD(self):
        circle = taubinSVD(self.data)
        circle = taubinSVD(self.numpy_data)

    def test_hyperSVD(self):
        circle = hyperSVD(self.data)
        circle = hyperSVD(self.numpy_data)

    def test_kmh(self):
        circle = kmh(self.data)
        circle = kmh(self.numpy_data)

if __name__ == '__main__':
    unittest.main()
