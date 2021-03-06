from tkinter import ttk, constants, StringVar

class DataView:
    '''
    Luo dataosion sovelluksen perusnäkymään.

    Attributes:
        root: Sovelluksen ikkuna.
        service: Sovelluslogiikasta huolehtiva luokka.
    '''

    def __init__(self, root, service):
        '''
        Konstruktori, joka luo muuttujat ja käynnistää näkymän luonnin.

        Args:
            root: Sovelluksen ikkuna.
            service: Sovelluslogiikasta huolehtiva luokka.
        '''

        self._root = root
        self._frame = None
        self._service = service
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

        estimation = self._service.get_estimation()
        data = self._service.print_data()
        user = self._service.username()

        self._error_variable = StringVar(self._frame)

        user_label = ttk.Label(master=self._frame, text=f"Käyttäjä: {user}", foreground="green")
        heading_label = ttk.Label(master=self._frame, text="Varallisuusarvio")
        estimation_label = ttk.Label(master=self._frame, text=estimation)
        data_label = ttk.Label(master=self._frame, text=data)
        self._error_label = ttk.Label(
            master=self._frame,
            textvariable=self._error_variable,
            foreground="red"
        )

        user_label.grid(row=0, column=0, sticky=constants.W)
        heading_label.grid(row=1, column=0, sticky=constants.W)
        estimation_label.grid(row=2, column=0, sticky=constants.W)
        data_label.grid(row=3, column=0, sticky=constants.W)

        self._hide_error()

    def show_error(self, message):
        self._error_variable.set(message)
        self._error_label.grid(row=4, column=2)

    def _hide_error(self):
        self._error_label.grid_remove()

class FrontView:
    '''
    Luo sovelluksen perusnäkymän.

    Attributes:
        root: Sovelluksen ikkuna.
        service: Sovelluslogiikasta huolehtiva luokka.
        show_login_view: Metodi, joka näyttää kirjautumisnäymän.
        error_variable: Virheviesti
        error_label: Virhe
    '''

    def __init__(self, root, service, show_login_view):
        '''
        Konstruktori, joka luo muuttujat ja käynnistää näkymän luonnin.

        Args:
            root: Sovelluksen ikkuna.
            service: Sovelluslogiikasta huolehtiva luokka.
            show_login_view: Metodi, joka näyttää kirjautumisnäymän.
            error_variable: Virheviesti
            error_label: Virhe
        '''

        self._root = root
        self._frame = None
        self._data_frame = None
        self._data_view = None
        self._service = service
        self._show_login_view = show_login_view

        self._initialize()

    def pack(self):
        '''
        viimeistelee näkymän luonnin.
        '''

        self._frame.pack(fill=constants.X)

    def destroy(self):
        '''
        Poistaa tämänhetkisen näkymän.
        '''

        self._frame.destroy()

    def _initialize_data(self):
        if self._data_view:
            self._data_view.destroy()

        self._data_view = DataView(self._data_frame, self._service)

        self._data_view.pack()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._data_frame = ttk.Frame(master=self._frame)

        self._initialize_data()

        name1_label = ttk.Label(master=self._frame, text="nimi")
        name2_label = ttk.Label(master=self._frame, text="nimi")
        amount1_label = ttk.Label(master=self._frame, text="summa kuukaudessa")
        amount2_label = ttk.Label(master=self._frame, text="Tämänhetkinen varallisuus")

        self._add_income_name_entry = ttk.Entry(master=self._frame)
        self._add_income_amount_entry = ttk.Entry(master=self._frame)
        self._delete_income_name_entry = ttk.Entry(master=self._frame)
        self._add_expense_name_entry = ttk.Entry(master=self._frame)
        self._add_expense_amount_entry = ttk.Entry(master=self._frame)
        self._delete_expense_name_entry = ttk.Entry(master=self._frame)
        self._update_wealth_entry = ttk.Entry(master=self._frame)

        logout_button = ttk.Button(
            master=self._frame,
            text="kirjaudu ulos",
            command=self._handle_logout
        )
        add_income_button = ttk.Button(
            master=self._frame,
            text="lisää tulo",
            command=self._handle_add_income
        )
        delete_income_button = ttk.Button(
            master=self._frame,
            text="poista tulo",
            command=self._handle_delete_income
        )
        add_expense_button = ttk.Button(
            master=self._frame,
            text="lisää meno",
            command=self._handle_add_expense
        )
        delete_expense_button = ttk.Button(
            master=self._frame,
            text="poista meno",
            command=self._handle_delete_expense
        )
        update_wealth_button = ttk.Button(
            master=self._frame,
            text="päivitä varallisuus",
            command=self._handle_update_wealth
        )
        delete_all_data_button = ttk.Button(
            master=self._frame,
            text="poista kaikki tiedot",
            command=self._handle_delete_all_data
        )

        logout_button.grid(row=0, column=2)

        self._data_frame.grid(row=0, column=0)

        name1_label.grid(row=4, column=0, sticky=constants.E)
        amount1_label.grid(row=5, column=0, sticky=constants.E)

        self._add_income_name_entry.grid(row=4, column=1)
        self._add_income_amount_entry.grid(row=5, column=1)
        add_income_button.grid(row=6, column=1)

        self._add_expense_name_entry.grid(row=4, column=2)
        self._add_expense_amount_entry.grid(row=5, column=2)
        add_expense_button.grid(row=6, column=2)

        name2_label.grid(row=7, column=0, sticky=constants.E)

        self._delete_income_name_entry.grid(row=7, column=1)
        delete_income_button.grid(row=8, column=1)

        self._delete_expense_name_entry.grid(row=7, column=2)
        delete_expense_button.grid(row=8, column=2)

        amount2_label.grid(row=9, column=0, sticky=constants.E)

        self._update_wealth_entry.grid(row=9, column=1)
        update_wealth_button.grid(row=10, column=1)

        delete_all_data_button.grid(row=10, column=2)

    def _handle_add_income(self):
        add_income_name = self._add_income_name_entry.get()
        add_income_amount = self._add_income_amount_entry.get()

        if not add_income_amount or not add_income_name:
            self._data_view.show_error('Täytä molemmat kentät')
            return

        try:
            add_income_amount = int(add_income_amount)
        except ValueError:
            self._data_view.show_error('Anna summa kokonaislukuna')
            return

        self._service.add_income(add_income_name, add_income_amount)

        self._initialize_data()

    def _handle_add_expense(self):
        add_expense_name = self._add_expense_name_entry.get()
        add_expense_amount = self._add_expense_amount_entry.get()

        if not add_expense_amount or not add_expense_name:
            self._data_view.show_error('Täytä molemmat kentät')
            return

        try:
            add_expense_amount = int(add_expense_amount)
        except ValueError:
            self._data_view.show_error('Anna summa kokonaislukuna')
            return

        self._service.add_expense(add_expense_name, add_expense_amount)

        self._initialize_data()

    def _handle_delete_income(self):
        delete_income_name = self._delete_income_name_entry.get()

        if not self._service.search_income(delete_income_name):
            self._data_view.show_error('Tuloa ei löytynyt')
            return

        self._service.delete_income(delete_income_name)

        self._initialize_data()

    def _handle_delete_expense(self):
        delete_expense_name = self._delete_expense_name_entry.get()

        if not self._service.search_expense(delete_expense_name):
            self._data_view.show_error('Menoa ei löytynyt')
            return

        self._service.delete_expense(delete_expense_name)

        self._initialize_data()

    def _handle_update_wealth(self):
        wealth = self._update_wealth_entry.get()

        try:
            wealth = int(wealth)
        except ValueError:
            self._data_view.show_error('Anna summa kokonaislukuna')
            return

        self._service.update_wealth(wealth)

        self._initialize_data()

    def _handle_delete_all_data(self):
        self._service.delete_all_data()

        self._initialize_data()

    def _handle_logout(self):
        self._service.logout()
        self._show_login_view()
