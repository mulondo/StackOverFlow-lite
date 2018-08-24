"""contain the API logi"""
from flask import request, jsonify, Response
from flask.views import MethodView
from app.modal import Datastore

class Api_controller(MethodView):
    questions={}
    answers={}
    """ contains methods that perform the logic"""
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
        if not Datastore.get_questions():
            return jsonify({'questions': 'There are no questions yet'})

        return jsonify({'questions': Datastore.get_questions()}), 200
        

    @staticmethod
    def get_a_question(question_id):
        """ gets a specific question from the data store"""
      
        for qn in Datastore.get_questions():
            if qn['QuestionID'] == question_id:
                question = {
                    'Question name': qn['QuestionName'],
                    'Question description': qn['Question_description'],
                    'Question date': qn['Question_date'],
                    'Question author': qn['Question_author']
                }
        question_answers = Api_controller.qn_answers(question_id)
        if not question_answers:
            return jsonify({'questions': Api_controller.question, 'answers': 'No answers currently'})
        return jsonify({'questions': Api_controller.question, 'answers': question_answers}), 200

    @staticmethod
    def qn_answers(question_id=None):
        """
        get answers about a specific question
        """

        qn_answers = []
        for answer in Datastore.get_answers():
            if answer['question_id'] == question_id:
                Api_controller.answers = {
                    'answer content': answer['answer_content'],
                    'answer_author': answer['answer_author'],
                    'answer_date': answer['answer_date'],
                    'answer_correctness': answer['answer_correctness']
                }
                qn_answers.append(Api_controller.answer_)
            continue

        return qn_answers


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
                Datastore.post_an_answer(QuestionID=request_data['QuestionID'],
                                        answerID=request_data['answerID'],
                                        answer_content=request_data['answer_content'],                                            
                                        answer_author=request_data['answer_author'],                                        
                                        answer_correctness=request_data['answer_correctness'] 
                                        )
                return jsonify({"message": "Answer posted succussfully!"}), 201
            return jsonify({"message": " question not found"})

def validation(question_object):
    """This performs a check """
    QuestionID=question_object
    if QuestionID==None:
        return False
    return True
