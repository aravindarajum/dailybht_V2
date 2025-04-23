import pytest
import softest

from pages.solution_bhtpage import solutions_bht

@pytest.mark.usefixtures("setup")
class test_solutionBHT(softest.TestCase):
    def test_solBHT(self):
        bht = solutions_bht(self.driver)
        bht.solBHT()
