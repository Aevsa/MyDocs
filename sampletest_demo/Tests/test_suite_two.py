import pytest
from sampletest_demo.data.test_data import TestData
from Pages.practice_page import PracticePage # Adjust this import if needed

@pytest.mark.usefixtures('setup')
class TestSuiteTwo:

    @pytest.fixture(autouse=True)
    def init_page_object(self, request):
        self.practice_page = PracticePage(request.cls.driver)



    @pytest.mark.test_four
    def test_enter_name(self):
        self.practice_page.enter_name(TestData.NAME)
