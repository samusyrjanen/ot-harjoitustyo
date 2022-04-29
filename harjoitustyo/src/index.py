from tkinter import Tk
from ui import UI
from service import Service
from file_reader import Repository
from database_connection import get_database_connection


def main():
    repository = Repository(get_database_connection())
    service = Service(repository)

    window = Tk()
    window.title("Budjetointisovellus")

    ui = UI(window, service)
    ui.start()

    window.mainloop()

if __name__ == '__main__':
    main()