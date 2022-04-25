from tkinter import Tk
from front_view import FrontView
from service import Service
from file_reader import Repository
from database_connection import get_database_connection

class UI:
    def __init__(self, root, servic):
        self._root = root
        self._current_view = None
        self._service = servic

    def start(self):
        self._show_front_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()
        self._current_view = None

    def _show_front_view(self):
        self._hide_current_view()

        self._current_view = FrontView(self._root, self._service)

        self._current_view.pack()

repository = Repository(get_database_connection())
service = Service(repository)

window = Tk()
window.title("Budjetointisovellus")

ui = UI(window, service)
ui.start()

window.mainloop()
