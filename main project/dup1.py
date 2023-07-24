import tkinter as tk
from tkinter import ttk

def open_profile_window():
    profile_window = tk.Toplevel(root)
    profile_window.title("Profile")
    profile_window.geometry("300x200")

    # Add your profile-related widgets here (e.g., labels, entry boxes, buttons, etc.)
    label_name = ttk.Label(profile_window, text="Name:")
    label_name.pack()
    entry_name = ttk.Entry(profile_window)
    entry_name.pack()
    # Add more profile widgets as needed

def create_dashboard():
    # Dashboard main window
    root = tk.Tk()
    root.title("Dashboard")
    root.geometry("800x600")

    # Top section with profile button and user information
    top_frame = ttk.Frame(root, padding=(10, 5))
    top_frame.pack(side=tk.TOP, fill=tk.X)

    label_user_info = ttk.Label(top_frame, text="User: John Doe")  # Replace this with actual user information
    label_user_info.pack(side=tk.LEFT, padx=10)

    button_profile = ttk.Button(top_frame, text="Profile", command=open_profile_window)
    button_profile.pack(side=tk.RIGHT, padx=10)

    # Main section with some sample data
    main_frame = ttk.Frame(root, padding=(10, 10))
    main_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    # Add sample data to the main section (e.g., labels, tables, charts, etc.)
    label_sample_data = ttk.Label(main_frame, text="Sample Data")
    label_sample_data.pack()

    # Add more widgets displaying your data

    root.mainloop()

if __name__ == "__main__":
    create_dashboard()
