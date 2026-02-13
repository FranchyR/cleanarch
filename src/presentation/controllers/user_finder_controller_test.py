from src.presentation.controllers.user_finder_controller import UserFinderController
from src.data.tests.user_finder import UserFinderSpy


class HttpRequestMock():
    def __init__(self) -> None:
        self.query_params = {"first_name": "meuTeste"}


def test_handle():
    http_request_mock = HttpRequestMock()
    use_case = UserFinderSpy
    user_finder_controller = UserFinderController(use_case)

    response = user_finder_controller.handle(http_request_mock)
    print()
    print()
    print(response.body)
