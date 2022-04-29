from front_view import FrontView
from login_view import LoginView

class UI:
    def __init__(self, root, servic):
        self._root = root
        self._current_view = None
        self._service = servic

    def start(self):
        self._show_login_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()
        self._current_view = None

    def _show_front_view(self):
        self._hide_current_view()

        self._current_view = FrontView(self._root, self._service, self._show_login_view)

        self._current_view.pack()

    def _show_login_view(self):
        self._hide_current_view()

        self._current_view = LoginView(self._root, self._service, self._show_front_view)

        self._current_view.pack()