import pytest


class Test_firstsample():

    @pytest.mark.SIT
    @pytest.mark.Sanity
    @pytest.mark.run(order=2)
    def test_fristtestcase(self,launch):
        print("this is first test case")

    @pytest.mark.Sanity
    @pytest.mark.run(order=1)
    def test_secondtestcase(self,launch):
        print("this is second test case")

    @pytest.mark.SIT
    def test_thirdtestcase(self,launch):
        print("this is third test case")
