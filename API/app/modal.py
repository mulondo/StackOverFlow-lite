"""
Data store
"""
class Datastore:
    """
    Datastore class
    """

    Question_datastore = []
    Answers_datastore = []

    class Questions_Handler:
        def __init__ (self, QuestionID=None, QuestionName=None, Question_description=None, Question_date=None, Question_author=None):
            self.QuestionID = QuestionID
            self.QuestionName=QuestionName
            self.Question_description=Question_description
            self.Question_date = Question_date           
            self.Question_author = Question_author

    class Answers_Handler:
        def __init__(self, QuestionID=None, answerID=None, answer_content=None, answer_author=None,answer_date=None,answer_correctness=None):
            self.QuestionID = QuestionID
            self.answerID = answerID
            self.answer_date = answer_date           
            self.the_answer = the_answer
            self.answer_author = answer_owner
            self.answer_correctness=answer_correctness

    @staticmethod
    def get_questions():
        return Datastore().Question_datastore

    @classmethod
    def get_all_answers(cls):
        return cls.answers_list

    @staticmethod
    def post_a_question(QuestionID, QuestionName, Question_description, Question_date, Question_author):
        question = Datastore.Questions_Handler(QuestionID, QuestionName, Question_description, Question_date, Question_author)
        question_dict= {
            'QuestionID': question.QuestionID,
            'QuestionName':question.QuestionName,
            'Question_description': Question_description,
            'Question_date': question.Question_date,
            'Question_author': question.Question_author           
        }
        Datastore.Question_datastore.append(question_dict)
        return question_dict

    @staticmethod
    def post_an_answer(QuestionID, answerID, answer_content, answer_author, answer_date, answer_correctness):
        answer = Datastore.Answers_handler(QuestionID, answerID, answer_content, answer_author, answer_date, answer_correctness)
        answers_dict = {
            'QuestionID': answer.QuestionID,
            'answerID': answer.answerID,
            'answer_content': answer.answer_content,
            'answer_author': answer.answer_author,
            'answer_date': answer.answer_date,
            'answer_correctness': answer.answer_correctness
        }
        Datastore.answers_list.append(answers_dict)
        return answers_dict

    @staticmethod
    def validate_qid(qid) -> bool:
        """
        Checks for the availability of the id
        :param :
        :param qid:
        :return:
        """
        question_id = qid
        for question in AppData.get_all_questions():
            if question['question_id'] == question_id:
                return True
            else:
                continue
        return False
