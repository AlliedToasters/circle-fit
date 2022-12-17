import unittest
from typing import List

import numpy as np

from src.circle_fit import riemannSWFLa, lm, prattSVD, taubinSVD, hyperSVD, kmh, hyperLSQ, standardLSQ


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


if __name__ == '__main__':
    unittest.main()
