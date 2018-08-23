from flask import json
from unittest import TestCase
from config import DevelopmentConfig
from run import APP

class TestRoutes(TestCase):
    def setUp(self):
        """Define test variables and initialize app"""
        self.APP = APP
        self.client = self.APP.test_client

    def test_get_questions(self):
        """ tests if all questions are got"""
        result = self.client().get('/api/v1/questions')
        self.assertEqual(result.status_code, 200)
        result2 = self.client().get('/api/v1/questions/hce')
        self.assertEqual(result2.status_code, 404)

    def test_get_a_question(self):
        """ tests if a question is got """
        result = self.client().get('/api/v1/questions/1')
        self.assertEqual(result.status_code, 200)
        result1 = self.client().get('/api/v1/questions/gc')
        self.assertEqual(result1.status_code, 404)
        result2 = self.client().get('/api/v1/questions/.1')
        self.assertEqual(result2.status_code, 404)

    def test_post_a_question(self):
        """ tests for posting a question """
        result = self.client().post('/api/v1/questions', data=json.dumps(dict(QuestionID=2, QuestionName="how sort an array", Question_owner="paul", Question_type="python", Question_description="how to test in python", Question_post_date="02/04/2018", answer="[]")), content_type='application/json')
        self.assertEqual(result.status_code, 201) 

    def test_post_answers(self):
        """ This tests whether a question is posted. """
        result = self.client().post('/api/v1/questions/1/answers', data=json.dumps(
        dict(answerID=2, answer_author="hope", content="very hard", correctness="false", Question_post_date="01/09/2018", answer_post_date="02/11/2018")), content_type='application/json')
        self.assertEqual(result.status_code, 201)
