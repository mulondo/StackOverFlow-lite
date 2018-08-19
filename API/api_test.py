from flask import json
from unittest import TestCase
from config import *
from run import App

class TestRoutes(TestCase):
    def setUp(self):
        self.APP = App
        self.client = self.APP.test_client

    def test_get_questions(self):       
        result = self.client().get('/api/v1/questions')
        self.assertEqual(result.status_code, 200)
        result2 = self.client().get('/api/v1/questions/hce')
        self.assertEqual(result2.status_code, 404)

    def test_get_a_question(self):
        result = self.client().get('/api/v1/questions/1')                
        self.assertEqual(result.status_code, 200)
        result1 = self.client().get('/api/v1/questions/gc')
        self.assertEqual(result1.status_code, 404)
        result1 = self.client().get('/api/v1/questions/#@')
        self.assertEqual(result1.status_code, 404)

    def test_post_a_question(self):
        result = self.client().post('/api/v1/questions', data=json.dumps(
            dict(QuestionID=2, QuestionName="how sort an array", Question_owner="paul")), content_type='application/json')
        self.assertEqual(result.status_code, 201) 

    def test_post_answers(self):  
        result = self.client().post('/api/v1/questions/2/answers/', data=json.dumps(
        dict(answerID=2, answer_owners="hope", content="very hard")), content_type='application/json')
        self.assertEqual(result.status_code,204)