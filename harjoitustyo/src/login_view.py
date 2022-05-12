from tkinter import ttk, constants, StringVar

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
            error_vatiable: Virheviesti
        '''

        self._root = root
        self._frame = None
        self._service = service
        self._show_front_view = show_front_view
        self._error_variable = None

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

        self._error_variable = StringVar(self._frame)

        heading_label = ttk.Label(master=self._frame, text="kirjaudu/rekisteröidy")
        username_label = ttk.Label(master=self._frame, text="käyttäjätunnus")
        password_label = ttk.Label(master=self._frame, text="salasana")
        self._error_label = ttk.Label(master=self._frame, textvariable=self._error_variable)

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

        self._hide_error()

    def _handle_login(self):
        username = self._username_entry.get()
        password = self._password_entry.get()

        if not username or not password:
            self._show_error('Täytä molemmat kentät')
            return

        if self._service.check_username_availability(username):
            self._show_error('Käyttäjätunnusta ei ole rekisteröity')
            return

        if self._service.login(username, password):
            self._show_front_view()
        else:
            self._show_error('Väärä salasana')

    def _handle_register(self):
        username = self._username_entry.get()
        password = self._password_entry.get()

        if not username or not password:
            self._show_error('Täytä molemmat kentät')
            return

        if not self._service.check_username_availability(username):
            self._show_error('Käyttäjätunnus on jo rekisteröity')
            return

        if self._service.register(username, password):
            self._show_front_view()
        else:
            self._show_error('Virhe')
            
    def _show_error(self, message):
        self._error_variable.set(message)
        self._error_label.grid(row=5, column=1)

    def _hide_error(self):
        self._error_label.grid_remove()