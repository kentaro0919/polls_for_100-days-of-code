from selenium import webdriver
import unittest


class NewPollsTest(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Safari()

    def tearDown(self):
        self.browser.quit
    
    def test_your_first_view(self):
        self.browser.get("http://localhost:8000/polls")
        self.assertEqual("Hello, world. You're at the polls index.", self.browser.find_element_by_id("tt"))
