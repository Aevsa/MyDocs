import pytest
from sampletest_demo.Pages.practice_page import PracticePage


@pytest.mark.usefixtures('setup')
class TestSuiteOne:

    @pytest.fixture(autouse=True)
    def init_page_object(self, request):
        self.practice_page = PracticePage(request.cls.driver)

    @pytest.mark.test_one
    def test_click_radio_button(self):
        self.practice_page.click_radio_button()

    @pytest.mark.test_two
    def test_click_checkbox_one(self):
        self.practice_page.select_checkbox_one()

    @pytest.mark.test_three
    def test_select_dropdown(self):
     self.practice_page.select_dropdown()
