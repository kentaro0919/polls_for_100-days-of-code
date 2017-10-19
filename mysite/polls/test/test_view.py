from django.urls import resolve
from django.test import TestCase

from django.http import HttpRequest
from polls.models import Question, Choice
import datetime
from django.utils import timezone
from hypothesis.extra.django.models import models


class indexViewTest(TestCase):

    def setUp(self):
        q = models(Question).example()

    def tearDown(self):
        pass

    def index_test_with_hypothesis(self):
        response = self.client.get('/polls/')
        self.assertIn(q.question_text, response.content.decode())
        self.assertIn(q.choice_set, response.content.decode())
        response2 = self.client.get('/polls/1/')
        self.assertIn(q.question_text, response2.content.decode())
        self.assertIn(q.choice_set, response.content.decode())
        response = self.client.get('/polls/5000/')
        self.assertEqual(404, response.status_code)


class index0QuestionViewTest(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_index_view_text_with_0(self):
        response = self.client.get('/polls/')
        self.assertIn("No polls are available.", response.content.decode())

    def test_index_view_text_with_1(self):
        Question.objects.create(question_text="first", pub_date=timezone.now())
        count_0 = Question.objects.all().count()
        self.assertEqual(count_0, 1)
        response = self.client.get('/polls/')
        self.assertIn("first", response.content.decode())


class detailViewTest(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_detail_view(self):
        Question.objects.create(question_text="You're looking at question 5",
                                pub_date=timezone.now(), )
        response = self.client.get("/polls/1/")
        self.assertIn("You&#39;re looking at question 5",
                      response.content.decode('utf8'))


class resultsViewTest(TestCase):

    def setUp(self):
        q = models(Question).example()

    def tearDown(self):
        pass

    def test_results_view(self):
        response = self.client.get("/polls/1/results/")
        q = Question.objects.get(pk=1)
        self.assertIn(q.question_text,
                      response.content.decode('utf8'))


class voteViewTest(TestCase):

    def setUp(self):
        q = models(Question).example()

    def tearDown(self):
        pass

    def test_vote_view(self):
        response = self.client.get("/polls/1/vote/")
        q = Question.objects.get(pk=1)
        self.assertIn(q.question_text,
                      response.content.decode('utf8'))

    def test_vote_no_choice(self):
        response = self.client.post("/polls/1/vote/")
        q = Question.objects.get(pk=1)
        self.assertIn(q.question_text,
                      response.content.decode('utf8'))
        self.assertIn("You didn&#39;t select a choice.",
                      response.content.decode('utf8'))
        self.assertEqual(200, response.status_code)

    def test_vote_with_choice(self):
        ## not working
        q = Question.objects.get(pk=1)
        response = self.client.post(
            "/polls/1/vote/", data={"Vote": 1})
        self.assertIn(q.question_text, response.content.decode())
        self.assertEqual(response.status_code, 200)
        #self.assertRedirects(response, '/polls/1/results/', status_code=200)
        #self.assertEqual(response['location'], '/polls/1/results/')


class SixQuestionIndexTest(TestCase):

    def setUp(self):
        q0 = Question.objects.create(question_text="zero",
                                     pub_date=timezone.now())
        q1 = Question.objects.create(question_text="one",
                                     pub_date=timezone.now())
        q2 = Question.objects.create(question_text="tow",
                                     pub_date=timezone.now())
        q3 = Question.objects.create(question_text="tree",
                                     pub_date=timezone.now())
        q4 = Question.objects.create(question_text="four",
                                     pub_date=timezone.now())
        q5 = Question.objects.create(question_text="five",
                                     pub_date=timezone.now())
        q5.choice_set.create(choice_text="Chice Text on Five")

    def question_6_count(self):
        count_6 = Question.objects.all().count()
        self.assertEqual(count_6, 6)

    def test_index_view_with_0(self):
        response = self.client.get('/polls/')
        self.assertNotIn("zero", response.content.decode())
        response_zero = self.client.get('/polls/1/')
        self.assertIn("zero", response_zero.content.decode())

    def test_index_view_with_1(self):
        response = self.client.get('/polls/')
        self.assertIn("one", response.content.decode())

    def test_index_view_with_2(self):
        response = self.client.get('/polls/')
        self.assertIn("tow", response.content.decode())

    def test_index_view_with_3(self):
        response = self.client.get('/polls/')
        self.assertIn("tree", response.content.decode())

    def test_index_view_with_4(self):
        response = self.client.get('/polls/')
        self.assertIn("four", response.content.decode())

    def test_index_view_with_5(self):
        response = self.client.get('/polls/')
        self.assertIn("five", response.content.decode())

    def test_index_view_with_6(self):
        response = self.client.get('/polls/')
        self.assertNotIn("six", response.content.decode())
