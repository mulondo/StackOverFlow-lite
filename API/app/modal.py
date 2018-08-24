"""
Data store
"""
from datetime import datetime

class Datastore:
    """
    Datastore class
    """

    Question_datastore = []
    Answers_datastore = []

    class Questions_Handler:
        def __init__ (self, QuestionID=None, QuestionName=None, Question_description=None, Question_author=None):
            self.QuestionID = QuestionID
            self.QuestionName=QuestionName
            self.Question_description=Question_description                      
            self.Question_author = Question_author

    class Answer_Handler:
        def __init__(self, QuestionID=None, answerID=None, answer_content=None, answer_author=None,answer_correctness=None):
            self.QuestionID = QuestionID
            self.answerID = answerID
            self.answer_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")            
            self.the_answer = the_answer
            self.answer_author = answer_owner
            self.answer_correctness=answer_correctness
  

    @classmethod
    def get_questions(cls):
        return cls.Question_datastore

    @classmethod
    def get_answers(cls):
        return cls.Answers_datastore

    @staticmethod
    def post_a_question(QuestionID, QuestionName, Question_description, Question_author):
        question = Datastore.Questions_Handler(QuestionID, QuestionName, Question_description, Question_author)
        question_dict= {
            'QuestionID': question.QuestionID,
            'QuestionName':question.QuestionName,
            'Question_description': question.Question_description,
            'Question_author': question.Question_author           
        }
        Datastore.Question_datastore.append(question_dict)
        return question_dict

    @staticmethod
    def post_an_answer(QuestionID, answerID, answer_content, answer_author, answer_correctness):
        answer = Datastore.Answer_handler(QuestionID, answerID, answer_content, answer_author, answer_correctness)
        answers_dict = {
            'QuestionID': answer.QuestionID,
            'answerID': answer.answerID,
            'answer_content': answer.answer_content,
            'answer_author': answer.answer_author,
            'answer_date': answer.answer_date,
            'answer_correctness': answer.answer_correctness
        }
        Datastore.Answers_datastore.append(answers_dict)
        return answers_dict

    

