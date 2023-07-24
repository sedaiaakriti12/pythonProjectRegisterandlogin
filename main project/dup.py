from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import *
import sqlite3


def create_table():
    connect = sqlite3.connect("expense.db")
    cursor = connect.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS expense_table(
                date text,
                title text,
                expense real)""")
    connect.commit()


def open_expense_window():
    expense_window = Toplevel()
    expense_window.title('Expense')
    expense_window.geometry('400x300')
    expense_window.resizable(0, 0)

    # Variables for Expense tab
    date = StringVar()
    title = StringVar()
    expense = StringVar()

    # Function to insert expense data into the database
    def insert():
        connect = sqlite3.connect("expense.db")
        cursor = connect.cursor()

        date_value = date_entry.get()
        title_value = title_entry.get()
        expense_value = expense_entry.get()

        # Insert expense data into the database
        cursor.execute("INSERT INTO expense_table VALUES (?, ?, ?)", (date_value, title_value, expense_value))
        connect.commit()

        # Clear the entry fields
        date_entry.delete(0, END)
        title_entry.delete(0, END)
        expense_entry.delete(0, END)

    # Expense tab widgets
    date_label = ttk.Label(expense_window, text='Date:')
    date_label.pack()
    date_entry = DateEntry(expense_window, width=12, textvariable=date)
    date_entry.pack()

    title_label = ttk.Label(expense_window, text='Title:')
    title_label.pack()
    title_entry = ttk.Entry(expense_window, width=20, textvariable=title)
    title_entry.pack()

    expense_label = ttk.Label(expense_window, text='Expense:')
    expense_label.pack()
    expense_entry = ttk.Entry(expense_window, width=20, textvariable=expense)
    expense_entry.pack()

    insert_button = ttk.Button(expense_window, text='Add Expense', command=insert)
    insert_button.pack()

    expense_window.mainloop()


def open_search_window():
    search_window = Toplevel()
    search_window.title('Search / Edit / Delete')
    search_window.geometry('400x300')
    search_window.resizable(0, 0)

    # Variables for Search/Edit/Delete tab
    search_type = StringVar()
    search_text = StringVar()

    # Function to search for records
    def search():
        connect = sqlite3.connect("expense.db")
        cursor = connect.cursor()

        search_type_value = search_type.get()
        search_text_value = search_text.get()

        if search_type_value == "Date":
            cursor.execute("SELECT * FROM expense_table WHERE date=?", (search_text_value,))
        elif search_type_value == "Title":
            cursor.execute("SELECT * FROM expense_table WHERE title=?", (search_text_value,))
        elif search_type_value == "Expense":
            cursor.execute("SELECT * FROM expense_table WHERE expense=?", (search_text_value,))

        records = cursor.fetchall()
        connect.commit()

        # Clear the Treeview
        for item in tree_view.get_children():
            tree_view.delete(item)

        # Insert the search results into the Treeview
        for record in records:
            tree_view.insert("", END, values=record)

    # Function to delete a selected record
    def delete_record():
        selected_item = tree_view.focus()
        if selected_item:
            confirm = messagebox.askyesno("Delete Record", "Are you sure you want to delete this record?")
            if confirm:
                connect = sqlite3.connect("expense.db")
                cursor = connect.cursor()

                # Get the record values from the selected item in the Treeview
                record_values = tree_view.item(selected_item)['values']

                # Delete the record from the database
                cursor.execute("DELETE FROM expense_table WHERE date=? AND title=? AND expense=?",
                               (record_values[0], record_values[1], record_values[2]))
                connect.commit()

                # Delete the selected item from the Treeview
                tree_view.delete(selected_item)
        else:
            messagebox.showinfo("No Record Selected", "Please select a record to delete.")

    # Search/Edit/Delete tab widgets
    search_label = ttk.Label(search_window, text='Search by:')
    search_label.pack()
    search_type_combobox = ttk.Combobox(search_window, values=["Date", "Title", "Expense"], textvariable=search_type)
    search_type_combobox.pack()

    search_text_entry = ttk.Entry(search_window, width=20, textvariable=search_text)
    search_text_entry.pack()

    search_button = ttk.Button(search_window, text='Search', command=search)
    search_button.pack()

    tree_view = ttk.Treeview(search_window, columns=(1, 2, 3), show="headings")
    tree_view.pack()

    tree_view.heading(1, text="Date")
    tree_view.heading(2, text="Title")
    tree_view.heading(3, text="Expense")

    delete_button = ttk.Button(search_window, text='Delete', command=delete_record)
    delete_button.pack()

    search_window.mainloop()


def main_screen():
    gui = Tk()
    gui.title('Expense and Income Manager')
    gui.geometry('400x300')
    gui.resizable(0, 0)

    create_table()

    expense_button = ttk.Button(gui, text='Expense', command=open_expense_window)
    expense_button.pack()

    search_button = ttk.Button(gui, text='Search / Edit / Delete', command=open_search_window)
    search_button.pack()

    gui.mainloop()


main_screen()
