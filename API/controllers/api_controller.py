"""contain the API logi"""
from flask import request, jsonify, Response, json
from flask.views import MethodView
from app.modal import Datastore

questions = Datastore.available_questions
class Api_controller(MethodView):
    """ contains methods that perform the logic"""
    @staticmethod
    def get(question_id=None):
        """ gets a specific question"""
        if question_id:
            question = {}
            for item in questions:
                if item['question_id'] == id:
                    question = {
                        'questionID': item['QuestionID'],
                        'question': item['QuestionName']
                    }

            return jsonify(question)
        else:
            return jsonify({'questions': questions})

    @staticmethod
    def post(question_id=None):
        """ posts a question"""
        if str(request.url_rule) == "/api/v1/questions":
            return Api_controller.do_post_question(question_id)
        if str(request.url_rule) == "/api/v1/questions/<int:question_id>/answers":
            return Api_controller.answer_question(question_id)
        return 'Errors'

    @staticmethod
    def do_post_question(self):
        """ this enable one to add a question"""
        request_data = request.get_json()
        if valid_question(request_data):
            question = {
                'QuestionID': request_data['QuestionID'],
                'Question_owner': request_data['Question_owner'],
                'Question_content': request_data['QuestionName'],
                'answer':[answers]}      
            questions.append(question)
            response = Response("", 201, mimetype="application/json")
            response.headers['Location'] = "questions/" + str(request_data['QuestionID'])
            return response
        else:
            bad_object = {
                "error": "Incorrect Question Format",
                "use": "{'QuestionID': '4',"
                "'QuestionID': '1','QuestionName': 'hello world' }"
            }
            response = Response(json.dumps(bad_object), status=400, mimetype="application/json")
            return response



    @staticmethod
    def answer_question(question_id):
        """ Adds an answer for a question"""
        request_data = request.get_json()
        for question in questions:
            if question['QuestionID'] == question_id:
                question['Answers'].append(request_data['Answers'])
            else:
                continue
            response = Response("", status="204")
            response.headers['Location'] = "/api/v1/questions/" + str(question_id) + "/"
            return response


def valid_question(question_object):
    """This performs a check """
    if 'QuestionID' in question_object and 'Question_owner' in question_object and 'QuestionName' in question_object:
        return True

    return False
