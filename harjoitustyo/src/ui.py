from tkinter import Tk, ttk, constants
from front_view import FrontView

class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_front_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()
        self._current_view = None

    def _show_front_view(self):
        self._hide_current_view()

        self._current_view = FrontView(self._root)

        self._current_view.pack()


        

window = Tk()
window.title("Budjetointisovellus")

ui = UI(window)
ui.start()

window.mainloop()