
from controllers.api_controller import Api_controller


class Routes:
    """
    Class to generate urls via static method generate
    """

    @staticmethod
    def generate(app):
        """
        Generate urls on the app context
        It takes no arguments
        :param app: takes in the app variable
        :return: links
        """

        app.add_url_rule('/api/v1/questions/', view_func=Api_controller.as_view('get_questions'), methods=['GET'],
                         strict_slashes=False)