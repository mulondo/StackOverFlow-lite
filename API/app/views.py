"""api routes"""
from controllers.api_controller import Api_controller

class Routes:
    """ class for api routes"""
    @staticmethod
    def generate_routes(app):
        """generates the routes"""
        app.add_url_rule('/api/v1/questions', view_func=Api_controller.as_view('get_questions'), methods=['GET'],
        strict_slashes=False)
        app.add_url_rule('/api/v1/questions/<int:question_id>', view_func=Api_controller.as_view('get_a_question'), methods=['GET'],
        strict_slashes=False)
        app.add_url_rule('/api/v1/questions', view_func=Api_controller.as_view('post_question'),
        methods=['POST'],strict_slashes=False)       
        app.add_url_rule('/api/v1/questions/<int:question_id>/answers', view_func=Api_controller.as_view('post_an_answer'), methods=['POST'],strict_slashes=False)
        