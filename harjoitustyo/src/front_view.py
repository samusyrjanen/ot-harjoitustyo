from tkinter import Tk, ttk, constants
from service import service

class DataView:
    def __init__(self, root):
        self._root = root
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        estimation = service._get_estimation()
        data = service._print_data()

        heading_label = ttk.Label(master=self._frame, text="Varallisuusarvio")
        estimation_label = ttk.Label(master=self._frame, text=estimation)
        data_label = ttk.Label(master=self._frame, text=data)

        heading_label.grid(row=0, column=0, sticky=constants.W)
        estimation_label.grid(row=1, column=0)
        data_label.grid(row=2, column=0)

class FrontView:
    def __init__(self, root):
        self._root = root
        self._frame = None
        self._data_frame = None
        self._data_view = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize_data(self):
        if self._data_view:
            self._data_view.destroy()

        self._data_view = DataView(self._data_frame)

        self._data_view.pack()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._data_frame = ttk.Frame(master=self._frame)

        self._initialize_data()

        self._add_income_name_entry = ttk.Entry(master=self._frame)
        self._add_income_amount_entry = ttk.Entry(master=self._frame)
        self._delete_income_name_entry = ttk.Entry(master=self._frame)
        self._add_expense_name_entry = ttk.Entry(master=self._frame)
        self._add_expense_amount_entry = ttk.Entry(master=self._frame)
        self._delete_expense_name_entry = ttk.Entry(master=self._frame)

        add_income_button = ttk.Button(
            master=self._frame,
            text="Add income",
            command=self._handle_add_income
        )
        delete_income_button = ttk.Button(
            master=self._frame,
            text="Delete income",
            command=self._handle_delete_income
        )
        add_expense_button = ttk.Button(
            master=self._frame,
            text="Add expense",
            command=self._handle_add_expense
        )
        delete_expense_button = ttk.Button(
            master=self._frame,
            text="Delete expense",
            command=self._handle_delete_expense
        )

        self._data_frame.grid(row=0, column=0)

        self._add_income_name_entry.grid(row=3, column=0)
        self._add_income_amount_entry.grid(row=4, column=0)
        add_income_button.grid(row=5, column=0)
        self._add_expense_name_entry.grid(row=3, column=1)
        self._add_expense_amount_entry.grid(row=4, column=1)
        add_expense_button.grid(row=5, column=1)
        self._delete_income_name_entry.grid(row=6, column=0)
        delete_income_button.grid(row=7, column=0)
        self._delete_expense_name_entry.grid(row=6, column=1)
        delete_expense_button.grid(row=7, column=1)

    def _handle_add_income(self):
        add_income_name = self._add_income_name_entry.get()
        add_income_amount = int(self._add_income_amount_entry.get())
        
        service._add_income(add_income_name, add_income_amount)

        self._initialize_data()

    def _handle_add_expense(self):
        add_expense_name = self._add_expense_name_entry.get()
        add_expense_amount = int(self._add_expense_amount_entry.get())
        
        service._add_expense(add_expense_name, add_expense_amount)

        self._initialize_data()

    def _handle_delete_income(self):
        delete_income_name = self._delete_income_name_entry.get()

        service._delete_income(delete_income_name)

        self._initialize_data()

    def _handle_delete_expense(self):
        delete_expense_name = self._delete_expense_name_entry.get()

        service._delete_expense(delete_expense_name)

        self._initialize_data()