import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
import sqlite3
import matplotlib.pyplot as plt
import random
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import Notebook, Treeview



class ExpenseIncomeManager:
    def __init__(self, root):
        self.root = root
        self.root.title('Expense and Income Manager')
        self.root.geometry('700x600')
        self.root.resizable(0, 0)
        self.root.configure(bg='#12AD2B')

        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(padx=10, pady=10)

        self.expense_tab = ttk.Frame(self.notebook)
        self.search_tab = ttk.Frame(self.notebook)

        self.notebook.add(self.expense_tab, text="Expense")
        self.notebook.add(self.search_tab, text="Search / Edit / Delete")

        self.create_expense_tab()
        self.create_search_tab()

    def create_database(self):
        self.conn = sqlite3.connect("expense.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS expense_table (
            date text,
            title text,
            expense real)""")
        self.conn.commit()

    def insert_record(self, date, title, expense):
        self.cursor.execute("INSERT INTO expense_table VALUES (?, ?, ?)", (date, title, expense))
        self.conn.commit()

    def show_records(self, tree_view):
        self.cursor.execute("SELECT * FROM expense_table")
        records = self.cursor.fetchall()
        for record in records:
            tree_view.insert('', 'end', values=record)

    def clear_records(self, tree_view):
        tree_view.delete(*tree_view.get_children())

    def delete_all_records(self, window):
        MsgBox = messagebox.askquestion('Delete Everything',
                                        'Are you sure you want to delete all the contents of the table?',
                                        icon='warning')
        if MsgBox == 'yes':
            self.cursor.execute("DELETE FROM expense_table")
            self.conn.commit()
            self.clear_records(window)
        else:
            messagebox.showinfo('Return', 'You will now return to the application screen')

    def create_expense_tab(self):
        self.create_database()

        frame1 = ttk.Frame(self.expense_tab)
        frame1.pack(fill="both", expand=1)

        l_date = ttk.Label(frame1, text='Date:', font=('Arial', 12, 'bold'))
        l_date.grid(row=0, column=0, padx=20, pady=20, sticky='w',)

        self.e_date = DateEntry(frame1, width=12, font=('Arial', 12))
        self.e_date.grid(row=0, column=1, padx=10, pady=20, sticky='w')

        l_title = ttk.Label(frame1, text='Title:', font=('Arial', 12, 'bold'))
        l_title.grid(row=1, column=0, padx=20, pady=5, sticky='w')

        self.e_title = ttk.Entry(frame1, width=20, font=('Arial', 12))
        self.e_title.grid(row=1, column=1, padx=10, pady=5, sticky='w')

        l_expense = ttk.Label(frame1, text='Expense:', font=('Arial', 12, 'bold'))
        l_expense.grid(row=2, column=0, padx=20, pady=25, sticky='w')

        self.e_expense = ttk.Entry(frame1, width=20, font=('Arial', 12))
        self.e_expense.grid(row=2, column=1, padx=10, pady=25, sticky='w')

        button_add = ttk.Button(frame1, text='Add Expense', command=self.add_expense)
        button_add.grid(row=2, column=2, padx=20, pady=15)

        frame2 = ttk.Frame(self.expense_tab)
        frame2.pack(fill="both", expand=1)

        button_show_all = ttk.Button(frame2, text='Show All Records', command=self.show_all_records)
        button_show_all.grid(row=0, column=0, padx=40, pady=10)

        button_delete_all = ttk.Button(frame2, text='Delete All Records', command=self.delete_all_records_prompt)
        button_delete_all.grid(row=0, column=1, padx=40, pady=10)

        self.tree_view_expense = ttk.Treeview(frame2, columns=("Date", "Title", "Expense"), show="headings")
        self.tree_view_expense.heading("Date", text="Date")
        self.tree_view_expense.heading("Title", text="Title")
        self.tree_view_expense.heading("Expense", text="Expense")
        self.tree_view_expense.grid(row=1, column=0, columnspan=2, padx=20, pady=10, sticky='w')

        scrollbar_expense = ttk.Scrollbar(frame2, orient="vertical", command=self.tree_view_expense.yview)
        self.tree_view_expense.configure(yscrollcommand=scrollbar_expense.set)
        scrollbar_expense.grid(row=1, column=2, sticky='ns')

        button_generate_chart = ttk.Button(frame2, text='Generate Pie Chart', command=self.generate_pie_chart)
        button_generate_chart.grid(row=2, column=0, columnspan=2, padx=20, pady=10)

    def generate_pie_chart(self):
        self.cursor.execute("SELECT title, expense FROM expense_table")
        records = self.cursor.fetchall()

        if not records:
            messagebox.showwarning("Warning", "No records found.")
            return

        categories = [record[0] for record in records]
        expenses = [record[1] for record in records]
        colors = random.choices(list(plt.cm.colors.CSS4_COLORS.values()), k=len(records))

        plt.figure(figsize=(8, 6))
        plt.pie(expenses, labels=categories, colors=colors, autopct='%1.1f%%', shadow=True)
        plt.title("Expense Distribution")
        plt.show()

    def create_search_tab(self):
        frame1 = ttk.Frame(self.search_tab)
        frame1.pack(fill="both", expand=1)

        search_options = ["Date", "Title", "Expense"]
        self.variable_search_by = tk.StringVar()
        self.variable_search_by.set(search_options[0])

        search_label = ttk.Label(frame1, text='Search by:', font=('Arial', 12, 'bold'))
        search_label.grid(row=0, column=0, padx=20, pady=20, sticky='w')

        search_dropdown = ttk.OptionMenu(frame1, self.variable_search_by, *search_options)
        search_dropdown.grid(row=0, column=1, padx=10, pady=20, sticky='w')

        self.entry_search = ttk.Entry(frame1, width=20, font=('Arial', 12))
        self.entry_search.grid(row=0, column=2, padx=10, pady=20, sticky='w')

        search_button = ttk.Button(frame1, text='Search',command=self.search_records)
        search_button.grid(row=0, column=3, padx=20, pady=20)

        clear_search_button = ttk.Button(frame1, text='Clear Search Results', command=self.clear_search_results)
        clear_search_button.grid(row=0, column=4, padx=20, pady=20)

        frame2 = ttk.Frame(self.search_tab)
        frame2.pack(fill="both", expand=1)

        delete_selected_button = ttk.Button(frame2, text='Delete Selected Record',
                                            command=self.delete_selected_record_prompt)
        delete_selected_button.grid(row=0, column=0, padx=40, pady=10)

        self.tree_view_search = ttk.Treeview(frame2, columns=("Date", "Title", "Expense"), show="headings")
        self.tree_view_search.heading("Date", text="Date")
        self.tree_view_search.heading("Title", text="Title")
        self.tree_view_search.heading("Expense", text="Expense")
        self.tree_view_search.grid(row=1, column=0, padx=20, pady=10, sticky='w')

        scrollbar_search = ttk.Scrollbar(frame2, orient="vertical", command=self.tree_view_search.yview)
        self.tree_view_search.configure(yscrollcommand=scrollbar_search.set)
        scrollbar_search.grid(row=1, column=1, sticky='ns')

    def add_expense(self):
        date = self.e_date.get()
        title = self.e_title.get()
        expense = self.e_expense.get()

        if date and title and expense:
            self.insert_record(date, title, expense)
            self.tree_view_expense.insert('', 'end', values=(date, title, expense))
            self.clear_entry_fields()
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    def show_all_records(self):
        self.clear_records(self.tree_view_expense)
        self.show_records(self.tree_view_expense)

    def delete_all_records_prompt(self):
        MsgBox = messagebox.askquestion('Delete Everything',
                                        'Are you sure you want to delete all the records?',
                                        icon='warning')
        if MsgBox == 'yes':
            self.delete_all_records(self.tree_view_expense)

    def search_records(self):
        search_by = self.variable_search_by.get()
        search_text = self.entry_search.get()
        if search_text:
            self.clear_records(self.tree_view_search)
            self.cursor.execute(f"SELECT * FROM expense_table WHERE {search_by}=?", (search_text,))
            records = self.cursor.fetchall()
            for record in records:
                self.tree_view_search.insert('', 'end', values=record)
        else:
            messagebox.showwarning("Warning", "Search field is empty.")

    def clear_search_results(self):
        self.clear_records(self.tree_view_search)

    def delete_selected_record_prompt(self):
        selected_item = self.tree_view_search.selection()
        if selected_item:
            MsgBox = messagebox.askquestion('Delete Selected Record',
                                            'Are you sure you want to delete the selected record?',
                                            icon='warning')
            if MsgBox == 'yes':
                for item in selected_item:
                    record = self.tree_view_search.item(item, "values")
                    self.cursor.execute("DELETE FROM expense_table WHERE date=? AND title=? AND expense=?",
                                        (record[0], record[1], record[2]))
                    self.conn.commit()
                    self.tree_view_search.delete(item)
        else:
            messagebox.showwarning("Warning", "No record selected.")

    def clear_entry_fields(self):
        self.e_date.delete(0, 'end')
        self.e_title.delete(0, 'end')
        self.e_expense.delete(0, 'end')


if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseIncomeManager(root)
    root.mainloop()
