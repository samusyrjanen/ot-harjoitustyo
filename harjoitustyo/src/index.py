from tkinter import Tk
from ui import UI
from service import Service
from file_reader import Repository
from database_connection import get_database_connection


def main():
    '''
    Käynnistää sovelluksen luomalla ikkunan ja kutsumalla UI:ta.
    '''

    repository = Repository(get_database_connection())
    service = Service(repository)

    window = Tk()
    window.title("Budjetointisovellus")

    user_interface = UI(window, service)
    user_interface.start()

    window.mainloop()

if __name__ == '__main__':
    main()
