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

        
    def test_was_published_recentlyd_true(self):
        first_question = Question()
        first_question.question_text = "have to be True"
        first_question.pub_date = timezone.now()
        first_question.save()

        saved_item = Question.objects.all().first()

        self.assertTrue(saved_item.was_published_recently())

    def test_was_published_recentlyd_false(self):
        question = Question()
        question.question_text = "have to be False"
        question.pub_date = datetime.datetime(2015, 1, 1, 12, 30, 59, 0, timezone.utc)
        question.save()

        saved_item = Question.objects.all().first()

        self.assertFalse(saved_item.was_published_recently())

    def test_question_has_chice(self):
        question = Question()
        question.question_text = "has choice"
        question.pub_date = timezone.now()
        question.save()

        question.choice_set.create(choice_text='Not much', votes=0)
        question.choice_set.create(choice_text='The sky', votes=0)

        saved_item = Question.objects.get(pk=1)

        self.assertEqual(saved_item.choice_set.count(), 2)
        self.assertEqual(saved_item.choice_set.first().choice_text, 'Not much')


    def test_str(self):
        question = Question()
        question.question_text = "What's new?"
        question.pub_date = timezone.now()
        question.save()

        saved_item = Question.objects.all().first()
        self.assertEqual(saved_item.__str__(), "What's new?")

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

