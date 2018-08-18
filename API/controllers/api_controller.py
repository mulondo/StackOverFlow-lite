from flask import request, jsonify, Response, json
from flask.views import MethodView
from app.modal import Data_store

class Api_controller(MethodView): 
    global questions
    
    questions = Data_store.available_questions


    @staticmethod
    def get(question_id=None):
        # Return a specific question
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
            # return all questions
            return jsonify({'questions': questions})
    
    @staticmethod
    def post(question_id=None):
        if str(request.url_rule) == "/api/v1/questions":
            return Api_controller.do_post_question(question_id)
        return 'Errors'

    @staticmethod
    def do_post_question(self):
        request_data = request.get_json()
        if valid_question(request_data):
            post_question = {
                'QuestionID': request_data['QuestionID'],
                'Question_owner': request_data['Question_owner'],
                'the_question': request_data['QuestionName'],
                'Answers': request_data['answers']
            }
            questions.append(post_question)
            response = Response("", 201, mimetype="application/json")
            response.headers['Location'] = "questions/" + str(request_data['QuestionID'])
            return jsonify({'questions': questions})
        else:
            bad_object = {
                "error": "Invalid Question Format",
                "help format": "Request format should be {'question_id': '5',"
                               "'person_who_asked': '7.99','the_question': 'Your Question' }"
            }
            response = Response(json.dumps(bad_object), status=400, mimetype="application/json")
            return response

# Validating a question
def valid_question(question_object):
    if 'QuestionID' in question_object and 'Question_owner' in question_object and 'QuestionName' in question_object:
        return True
    else:
        return False
