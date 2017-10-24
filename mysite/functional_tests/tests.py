from selenium import webdriver
from django.test import LiveServerTestCase
from django.test import TestCase
from polls.models import Question, Choice
from django.utils import timezone
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

binary = FirefoxBinary('/Applications/Firefox.app/Contents/MacOS/firefox-bin')
browser = webdriver.Firefox(firefox_binary=binary)


class DiteirViewChoiceTest(LiveServerTestCase):

    def setUp(self):
        q = Question(question_text="What's new?", pub_date=timezone.now())
        q.save()
        q.choice_set.create(choice_text='choice_text', votes=0)
        q.save()
        # self.browser = webdriver.Safari()
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_detail_views(self):
        q_one = Question.objects.get(pk=1)
        c_one = q_one.choice_set.all().first()
        self.browser.get(self.live_server_url + "/polls/1/")
        self.assertIn(q_one.question_text,
                      self.browser.find_element_by_id("questiontext").text)
        self.assertIn(c_one.choice_text,
                      self.browser.find_element_by_id(f"choice{c_one.pk }").text)


class mayNotworkTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Safari()

    def tearDown(self):
        self.browser.quit()

    def test_write_views_that_actually_do_something(self):
        self.browser.get(self.live_server_url + "/polls/")
        # help(self.browser)
        self.assertEqual("Hello, world. You're at the polls index.",
                         self.browser.find_element_by_id("TopTitle").text)


class NewPollsTest(LiveServerTestCase):

    def setUp(self):

        self.browser = webdriver.Safari()

    def tearDown(self):
        self.browser.quit()

    def test_your_first_view(self):
        self.browser.get(self.live_server_url + "/polls/")
        # help(self.browser)
        self.assertEqual("Hello, world. You're at the polls index.",
                         self.browser.find_element_by_id("TopTitle").text)
