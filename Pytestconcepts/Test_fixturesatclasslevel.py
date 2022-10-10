import pytest


#@pytest.mark.usefixtures("launch")
class Test_fixturesatclasslevel:

    @pytest.mark.SIT
    @pytest.mark.MustRun
    @pytest.mark.run(order=2)
    def test_fristtestcase(self):
        print("this is first test case")

    @pytest.mark.MustRun
    @pytest.mark.run(order=1)
    def test_secondtestcase(self):
        print("this is second test case")

    @pytest.mark.SIT
    def test_thirdtestcase(self):
        print("this is third test case")
