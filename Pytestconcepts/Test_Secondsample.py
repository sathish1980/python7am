import pytest

@pytest.mark.usefixtures("launch")
class Test_secondsample:

    @pytest.mark.MustRun
    def test_thirdtestcase(self):
        print("This is third test case")

    @pytest.mark.xfail
    def test_fourthtestcase(self):
        print("This is fourth test case")

    @pytest.mark.Regression
    @pytest.mark.MustRun
    def test_fourthtestcases(self):
        print("This is latest test case")

    @pytest.mark.Sanity
    def test_sample(self):
        print("This is sample test case")