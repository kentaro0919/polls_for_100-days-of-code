from selenium import webdriver
from django.test import LiveServerTestCase
from django.test import TestCase
from polls.models import Question, Choice
from django.utils import timezone
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

binary = FirefoxBinary('/Applications/Firefox.app/Contents/MacOS/firefox-bin')
browser = webdriver.Firefox(firefox_binary=binary)


class QumiCanSeeHerPageTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_qumi_can_see_the_index_page(self):
        self.browser.get(self.live_server_url + "/Qumi/")
        self.assertEqual("Qumi's Preserved food recipes.",
                         self.browser.find_element_by_id("TopTitle").text)
