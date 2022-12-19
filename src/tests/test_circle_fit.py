import unittest
from typing import List
import time

import numpy as np

from src.circle_fit import riemannSWFLa, lm, prattSVD, taubinSVD, hyperSVD, kmh, hyperLSQ, standardLSQ
from src.circle_fit import hyper_fit, least_squares_circle


class AppTest(unittest.TestCase):

    perfect_delta = 1E-4
    noisy_delta = 1E-1

    def create_data(self):
        self.center = np.random.uniform(-100, 100) + np.random.uniform(-100, 100) * 1j
        self.radius = 10 ** np.random.uniform(0, 2)
        self.noise = self.radius * 0.1
        self.perfect_phasor = self.radius * np.e ** (1j * np.linspace(0, 2 * np.pi, 100, endpoint=False)) + self.center
        self.perfect_data = np.array([self.perfect_phasor.real, self.perfect_phasor.imag]).transpose()
        self.noisy_data = self.perfect_data + np.random.normal(scale=self.noise, size=self.perfect_data.shape)
        self.perfect_data_as_list: List[List[float]] = self.perfect_data.tolist()

    def check_perfect_data_fit(self, xc, yc, r, _):
        self.assertAlmostEqual(xc, self.center.real, delta=self.perfect_delta * self.radius)
        self.assertAlmostEqual(yc, self.center.imag, delta=self.perfect_delta * self.radius)
        self.assertAlmostEqual(r, self.radius, delta=self.perfect_delta * self.radius)

    def check_noisy_data_fit(self, xc, yc, r, _):
        self.assertAlmostEqual(xc, self.center.real, delta=self.noisy_delta * self.radius)
        self.assertAlmostEqual(yc, self.center.imag, delta=self.noisy_delta * self.radius)
        self.assertAlmostEqual(r, self.radius, delta=self.noisy_delta * self.radius)

    def apply_test_repeatedly(self, method, precall=None):
        perfect_data_failures = 0
        noisy_data_failures = 0
        n_tries = 1000
        for n in range(1000):
            self.create_data()
            args = precall() if precall else ()
            try:
                self.check_perfect_data_fit(*method(self.perfect_data_as_list, *args))
            except AssertionError:
                perfect_data_failures += 1
            try:
                self.check_perfect_data_fit(*method(self.perfect_data, *args))
            except AssertionError:
                perfect_data_failures += 1
            try:
                self.check_noisy_data_fit(*method(self.noisy_data, *args))
            except AssertionError:
                noisy_data_failures += 1
        print(f"Method {method.__name__} failed {perfect_data_failures}/{n_tries * 2} perfect data fits, "
              f"{noisy_data_failures}/{n_tries} noisy data fits.")
        self.assertLess(perfect_data_failures, 10)
        self.assertLess(noisy_data_failures, 10)

    def test_hyperLSQ(self):
        self.apply_test_repeatedly(hyperLSQ)

    def test_standardLSQ(self):
        self.apply_test_repeatedly(standardLSQ)

    def test_riemannSWFLa(self):
        self.apply_test_repeatedly(riemannSWFLa)

    def test_lm(self):
        def par_ini(): return (np.array([self.center.real, self.center.imag, self.radius]),)
        self.apply_test_repeatedly(lm, par_ini)

    def test_prattSVD(self):
        self.apply_test_repeatedly(prattSVD)

    def test_taubinSVD(self):
        self.apply_test_repeatedly(taubinSVD)

    def test_hyperSVD(self):
        self.apply_test_repeatedly(hyperSVD)

    def test_kmh(self):
        self.apply_test_repeatedly(kmh)


class BackwardsCompatTest(unittest.TestCase):
    """
    Unaltered original tests, for testing backwards compatibility.
    """
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

    def test_hyper_fit(self):
        _ = hyper_fit(self.data)
        _ = hyper_fit(self.numpy_data)

    def test_circle_fit(self):
        _ = least_squares_circle(self.data)
        _ = least_squares_circle(self.numpy_data)


if __name__ == '__main__':
    unittest.main()
