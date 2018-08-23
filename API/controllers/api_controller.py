"""contain the API logi"""
from flask import request, jsonify, Response
from flask.views import MethodView
from app.modal import Datastore


class Api_controller(MethodView):
    """ contains methods that perform the logic"""
    @staticmethod
    def get(question_id=None):
        """ Calls methods that require a get request """
        if str(request.url_rule) == "/api/v1/questions":
            return Api_controller.get_all_questions()
        if str(request.url_rule) == "/api/v1/questions/<int:question_id>":
            return Api_controller.get_a_question(question_id)

   # @staticmethod
   # def get_all_questions():
        """ gets all questions from the data store"""
       # return jsonify({'questions':QUESTIONS})

    #@staticmethod
    #def get_a_question(question_id):
       # """ gets a specific question from the data store"""
       # for one_question in QUESTIONS:
          #  if one_question['QuestionID'] == question_id:
              #  return jsonify(one_question)
           # return jsonify({'Message':'The question is not found'})


    @staticmethod
    def post(question_id=None):
        """ posts a question"""
        if str(request.url_rule) == "/api/v1/questions":
            return Api_controller.do_post_question()
        if str(request.url_rule) == "/api/v1/questions/<int:question_id>/answers":
            return Api_controller.answer_question(question_id)


    @staticmethod
    def do_post_question():
        """ this enable one to add a question"""
        request_data = request.get_json()
        if validation(request_data):
            Datastore.post_a_question(QuestionID=request_data['QuestionID'],
                                  QuestionName=request_data['QuestionName'],
                                  Question_description=request_data['Question_description'],
                                  Question_date=request_data['Question_date'],
                                  Question_author=request_data['Question_author'])        
            return jsonify({"Message ": "Question posted succussfully"}), 201
        return jsonify({'Message':'Missing some parameters'})
           

    @staticmethod
    def answer_question(question_id):
        """ Adds an answer for a question """
        request_data = request.get_json()
        questions = Datastore.get_questions()            
        
        for question in questions:
            if question['QuestionID'] == question_id:
                Datastore.post_an_answer(QuestionID=question_id,
                                        answerID=request_data['answerID'],
                                        answer_content=request_data['answer_content'],                                            
                                        answer_author=request_data['answer_author'], 
                                        answer_date=request_data['answer_date'],
                                        answer_correctness=request_data['answer_correctness'] 
                                        )
                return jsonify({"message": "Answer posted succussfully!"}), 201
            return jsonify({"message": " some field are empty"})

def validation(question_object):
    """This performs a check """
    QuestionID=question_object
    if QuestionID!=None:
        return True

    return False
