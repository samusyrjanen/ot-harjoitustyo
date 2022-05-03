from tkinter import ttk, constants

class LoginView:
    '''
    Luo kirjautumisnäkymän.

    Attributes:
        root: Sovelluksen ikkuna.
        service: Sovelluslogiikasta huolehtiva luokka.
        show_front_view: Metodi, joka näyttää seuraavan näymän.
    '''

    def __init__(self, root, service, show_front_view):
        '''
        Konstruktori, joka luo muuttujat ja käynnistää näkymän luonnin.

        Args:
            root: Sovelluksen ikkuna.
            service: Sovelluslogiikasta huolehtiva luokka.
            show_front_view: Metodi, joka näyttää seuraavan näymän.
        '''

        self._root = root
        self._frame = None
        self._service = service
        self._show_front_view = show_front_view

        self._initialize()

    def pack(self):
        '''
        Viimeistelee näkymän luonnin.
        '''

        self._frame.pack(fill=constants.X)

    def destroy(self):
        '''
        Poistaa tämänhetkisen näkymän.
        '''

        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        heading_label = ttk.Label(master=self._frame, text="kirjaudu/rekisteröidy")
        username_label = ttk.Label(master=self._frame, text="käyttäjätunnus")
        password_label = ttk.Label(master=self._frame, text="salasana")

        self._username_entry = ttk.Entry(master=self._frame)
        self._password_entry = ttk.Entry(master=self._frame, show='*')

        login_button = ttk.Button(
            master=self._frame,
            text="kirjaudu",
            command=self._handle_login
        )
        register_button = ttk.Button(
            master=self._frame,
            text="rekisteröidy",
            command=self._handle_register
        )

        heading_label.grid(row=0, column=0)
        username_label.grid(row=1, column=0, sticky=constants.E)
        password_label.grid(row=2, column=0, sticky=constants.E)

        self._username_entry.grid(row=1, column=1)
        self._password_entry.grid(row=2, column=1)

        login_button.grid(row=3, column=1)
        register_button.grid(row=4, column=1)

    def _handle_login(self):
        username = self._username_entry.get()
        password = self._password_entry.get()

        if self._service.login(username, password):
            self._show_front_view()

    def _handle_register(self):
        username = self._username_entry.get()
        password = self._password_entry.get()

        if self._service.register(username, password):
            self._show_front_view()
            