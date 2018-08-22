"""contain the API logi"""
from flask import request, jsonify, Response, json
from flask.views import MethodView
from app.modal import Datastore

questions = Datastore.available_questions
class Api_controller(MethodView):
    """ contains methods that perform the logic"""
    @staticmethod
    def get(question_id=None):
        if str(request.url_rule)=="/api/v1/questions":
            return Api_controller.get_all_questions()
        if str(request.url_rule)=="/api/v1/questions/<int:question_id>":
            return Api_controller.get_a_question(question_id)
    
    @staticmethod
    def get_all_questions():
        return jsonify({'questions':questions})
    
    @staticmethod
    def get_a_question(question_id):        
            for one_question in questions:
                if one_question['QuestionID'] == question_id:
                    return jsonify(one_question)
                else:
                    return jsonify({'question':question_})
            # return all questions
                     
            #else:
                #return jsonify({'Message':'The question is not found'})
    
   

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
                'Question_Name': request_data['QuestionName'],
                'Question_type': request_data['Question_type'],
                'Question_description': request_data['Question_description'],
                'Question_post_date': request_data['Question_post_date'],
                'answer':[]
                }      
            questions.append(question)
            return jsonify({'questions':questions})
            #response = Response("", 201, mimetype="application/json")
            #response.headers['Location'] = "questions/" + str(request_data['QuestionID'])
            #return response
        else:
            return jsonify({'Message':'Question not created due to incorrect format'})
           # bad_object = {
              #  "error": "Incorrect Question Format",
              #  "use": "{'QuestionID': '4',"
              #  "'QuestionID': '1','QuestionName': 'hello world' }"
           # }
           # response = Response(json.dumps(bad_object), status=400, mimetype="application/json")
            



    @staticmethod
    def answer_question(question_id):
        """ Adds an answer for a question"""
        request_data = request.get_json()
        for question in questions:
            if question['QuestionID'] == question_id:                
                post_answer={
                    'answerID':request_data['answerID'],
                    'content':request_data['content'],
                    'answer_author':request_data['answer_author'],
                    'correctness':request_data['correctness'],
                    'answer_post_date':request_data['answer_post_date']
                }
                question['answers'].append(post_answer)
                
            return jsonify({'Message :':'The resource not found'})


def valid_question(question_object):
    """This performs a check """
    if 'QuestionID' in question_object and 'Question_owner' in question_object and 'QuestionName' in question_object:
        return True

    return False
