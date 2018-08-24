from models import Questions
from flask import request, jsonify, Response
from flask.views import MethodView
from models import Controllers

class Controllers:
    @staticmethod
    def get(question_id=None):
        """ Calls methods that require a get request """
        if str(request.url_rule) == "/api/v1/questions":
            return Api_controller.get_all_questions()
        if str(request.url_rule) == "/api/v1/questions/<int:question_id>":
            return Api_controller.get_a_question(question_id)
    @staticmethod
    def get_all_questions():
        """ gets all questions from the data store"""
        if not Questions.get_all_questions():
            return jsonify({'questions': 'There are no questions yet'})
        return jsonify({'questions': Datastore.get_questions()}), 200

    @staticmethod
    def post(question_id=None):
        if str(request.url_rule) =="/api/v1/questions":
            return Controllers.post_a_question()
    
    def post_a_question():
        request_data=request.get_json()
        if request_data!=None:
            Questions.post_question({question_id = request_data['question_id'],
            question_name = request_data})
            
        