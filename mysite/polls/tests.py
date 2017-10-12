from django.urls import resolve
from django.test import TestCase
from polls.views import index
from django.http import HttpRequest
from polls.models import Question, Choice
import datetime
from django.utils import timezone
from selenium import webdriver


class ViewIndexQuestionTest(TestCase):
    
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_index_view_with_0(self):
        count_0 = Question.objects.all().count()           
        self.assertEqual(count_0, 0)

    def test_index_view_text_with_0(self):
        response = self.client.get('/polls/')
        self.assertIn("No polls are available.", response.content.decode())
        
    def test_index_view_text_with_1(self):
        Question.objects.create(question_text="first", pub_date=timezone.now())
        count_0 = Question.objects.all().count()           
        self.assertEqual(count_0, 1)
        response = self.client.get('/polls/')
        self.assertIn("first", response.content.decode())
   

class WritingMoreViewstest(TestCase):
    
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_detail_view(self):
        response = self.client.get("/polls/5/")
        #self.assertTemplateUsed(response, 'polls/index.html')
        #print(type(response))
        #print(help(response))
        self.assertEqual("You're looking at question 5.", response.content.decode('utf8'))

    def test_results_view(self):
        response = self.client.get("/polls/5/results/")
        #elf.assertTemplateUsed(response, 'polls/index.html')
        self.assertIn("You're looking at the results of question 5", response.content.decode('utf8'))


    def test_vote_view(self):
        response = self.client.get("/polls/5/vote/")
        #self.assertTemplateUsed(response, 'polls/index.html')
        self.assertIn("You're voting on question 5.", response.content.decode('utf8'))

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
        self.assertTrue(html.endswith('</html>')) 

