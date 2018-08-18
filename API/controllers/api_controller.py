from flask import request, jsonify, Response, json
from flask.views import MethodView
from app.modal import *

class Api_controller:
    questions=Data_store.available_questions


    @staticmethod
    def get(question_id=None):
        # Return a specific question
        if question_id:
            question_ = {}
            for item in questions:
                if item['question_id'] == id:
                    question_ = {
                        'question_id': item['question_id'],
                        'the_question': item['the_question']
                    }

            return jsonify(question_)
        else:
            # return all questions
            return jsonify({'questions': questions})
