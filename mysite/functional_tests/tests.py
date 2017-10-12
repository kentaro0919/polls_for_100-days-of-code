from selenium import webdriver
from django.test import LiveServerTestCase
from django.test import TestCase


class mayNotworkTest(LiveServerTestCase):
    
    def setUp(self):
            
        self.browser = webdriver.Safari()

    def tearDown(self):
        self.browser.quit()
    

    def test_write_views_that_actually_do_something(self):
        self.browser.get(self.live_server_url+"/polls/")
        #help(self.browser)
        self.assertEqual("Hello, world. You're at the polls index.",
                         self.browser.find_element_by_id("tt").text )    
        


class NewPollsTest(LiveServerTestCase):
    
    def setUp(self):
        
        self.browser = webdriver.Safari()

    def tearDown(self):
        self.browser.quit()
    
    def test_your_first_view(self):
        self.browser.get(self.live_server_url+"/polls/")
        #help(self.browser)
        self.assertEqual("Hello, world. You're at the polls index.",
                         self.browser.find_element_by_id("tt").text )
