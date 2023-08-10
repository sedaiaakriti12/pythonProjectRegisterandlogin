import tkinter as tk
import unittest
from tkinter import ttk, messagebox
from tkcalendar import DateEntry

# Import the correct class from your module here
import expenditure_report


class TestExpenseIncomeManager(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root = tk.Tk()
        cls.app = expenditure_report.ExpenseIncomeManager(cls.root)

    @classmethod
    def tearDownClass(cls):
        cls.root.destroy()

    def test_add_expense_valid_data(self):
        self.app.e_date.set_date('2023-08-10')
        self.app.e_title.insert(0, 'Groceries')
        self.app.e_expense.insert(0, '50')
        self.app.add_expense()

        # Assuming that the record has been added to the display
        self.assertTrue(self.app.tree_view_expense.exists("", "end"))

    def test_add_expense_empty_fields(self):
        # Attempt to add an expense with empty fields
        self.app.add_expense()

        # Assert that a messagebox error is shown
        self.assertTrue(messagebox._show.called)
        self.assertEqual(messagebox._show.call_args[0][0], 'Error')

    def test_search_records_valid_date(self):
        self.app.variable_search_by.set('Date')
        self.app.entry_search.insert(0, '2023-08-10')
        self.app.search_records()

        # Assuming the search result is displayed correctly
        self.assertTrue(self.app.tree_view_search.exists("", "end"))

    # Similar test methods for other functionalities (search, delete, pie chart, etc.)


if _name_ == '_main_':
    unittest.main()