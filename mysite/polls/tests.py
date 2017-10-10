from django.urls import resolve
from django.test import TestCase
from polls.views import index
from django.http import HttpRequest
from polls.models import Question, Choice
import datetime
from django.utils import timezone

class PollsModelTest(TestCase):
    
    def test_saving_and_retrieving_items(self):
        first_question = Question()
        first_question.question_text = "What's new?"
        first_question.pub_date = timezone.now()
        first_question.save()

        saved_items = Question.objects.all()
        self.assertEqual(saved_items.count(), 1)

        second_question = Question()
        second_question.question_text = "What's up?"
        second_question.pub_date = timezone.now()
        second_question.save()

        saved_items = Question.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.question_text, "What's new?")
        self.assertEqual(second_saved_item.question_text, "What's up?")
        self.assertEqual(second_saved_item.pub_date, second_question.pub_date )
        # to test __str__
        #self.assertIn(str(first_saved_item,) "What's new?")
        #self.assertEqual(second_saved_item, "<Question: What's up?>")
        

class SmokeTest(TestCase):
    
    def test_polls_root_url(self):
        response = self.client.get("/polls/")
        self.assertTemplateUsed(response, 'polls/index.html')

    def test_index_returns_correct_html(self):
        request = HttpRequest()
        response = index(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<!DOCTYPE html>'))
        self.assertIn('<h1 id="tt">Hello, world. Youre at the polls index.</h1>', html)
        self.assertTrue(html.endswith('</html>')) 

