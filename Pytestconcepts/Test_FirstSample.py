import pytest


class Test_firstclass:

    @pytest.mark.Sanity
    @pytest.mark.run(order=2)
    def test_firstTestcase(self):
        print("This is first test case")

    @pytest.mark.Sanity
    @pytest.mark.run(order=1)
    def test_secondTestcase(self):
        print("This is second test case")
