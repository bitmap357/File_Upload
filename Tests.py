# # from tkinter import *
# # from tkinter import font
#
# # root = Tk()
# # root.geometry('880x500')
# #
# # greet = Frame(root)
# # order = Frame(root)
# #
# #
# # def change_to_greet():
# #     greet.pack(fill='both', expand=1)
# #     order.pack_forget()
# #
# #
# # def change_to_order():
# #     order.pack(fill='both', expand=1)
# #     greet.pack_forget()
# #
# #
# # # Create fonts for making difference in the frame
# # font1 = font.Font(family='Georgia', size=22, weight='bold')
# # font2 = font.Font(family='Aerial', size=12)
# #
# # # Add a heading logo in the frames
# # label1 = Label(greet, text="Hey There! Welcome to TutorialsPoint.", foreground="green3", font=font1)
# # label1.pack(pady=20)
# #
# # label2 = Label(order, text="Find all the interesting Tutorials.", foreground="blue", font=font2)
# # label2.pack(pady=20)
# #
# # # Add a button to switch between two frames
# # btn1 = Button(root, text="Switch to Greet", font=font2, command=change_to_order)
# # btn1.pack(pady=20)
# #
# # btn2 = Button(order, text="Switch to Order", font=font2, command=change_to_greet)
# # btn2.pack(pady=20)
# #
# # root.mainloop()
#
#
# # def scankey(event):
# #     val = event.widget.get()
# #     print(val)
# #
# #     if val == '':
# #         data = list1
# #     else:
# #         data = []
# #         for item in list1:
# #             if val.lower() in item.lower():
# #                 data.append(item)
# #
# #     update(data)
# #
# #
# # def update(data):
# #     listbox.delete(0, 'end')
# #
# #     # put new data
# #     for item in data:
# #         listbox.insert('end', item)
# #
# #
# # list1 = ('C', 'C++', 'Java', 'Python', 'Perl', 'PHP', 'ASP', 'JS')
# #
# # ws = Tk()
# #
# # entry = Entry(ws)
# # entry.pack()
# # entry.bind('<KeyRelease>', scankey)
# #
# # listbox = Listbox(ws)
# # listbox.pack()
# # update(list1)
# #
# # ws.mainloop()
#
# import tkinter
# from tkinter import *
# from tkinter import ttk
# from tkinter import filedialog
# from pathlib import Path
# import sqlite3
# from tkinter.filedialog import askopenfile
# import datetime
# import os.path
#
# root = Tk()
# root.geometry('880x500')
# root.title('File Upload')
#
# # Creating database and cursor
# conn = sqlite3.connect('test.db')
# c = conn.cursor()
#
# # Create table
# c.execute('''CREATE TABLE IF NOT EXISTS files (
#             tag text,
#             file_name text,
#             file blob,
#             date text,
#             size text
#             )''')
#
# main = Frame(root)
# upload = Frame(root)
# category = Frame(root)
# search = Frame(root)
# main.pack()
#
# dic = {}
#
#
# def upload_file_com():
#     """Upload a file to the database."""
#
#     # Get the file path from the user.
#     file_path = filedialog.askopenfilename(
#         filetypes=[("TXT files", ".txt"), ("DOC files", ".doc"), ("DOCX files", ".docx"), ("PDF files", ".pdf")])
#
#     # Check if the user selected a file.
#     if file_path:
#
#         # Get the file name and data.
#         file_name = Path(file_path).name
#         file_data = open(file_path, 'rb').read()
#         # Get the file size.
#        # file_size = file_size_mb(file_path)
#     else:
#         choose_file_label.config(text="NO FILE CHOSEN")
#     global dic
#
#
#
# def change_to_main():
#     main.pack(fill='both', expand=1)
#     upload.pack_forget()
#     category.pack_forget()
#     search.pack_forget()
#
#
# def change_to_upload():
#     upload.pack(fill='both', expand=1)
#     category.pack_forget()
#     search.pack_forget()
#     main.pack_forget()
#
#
# def change_to_category():
#     category.pack(fill='both', expand=1)
#     upload.pack_forget()
#     search.pack_forget()
#     main.pack_forget()
#
#
# def change_to_search():
#     search.pack(fill='both', expand=1)
#     category.pack_forget()
#     upload.pack_forget()
#     main.pack_forget()
#
#
# def save(tag, file_name, file):
#     # Get the current timestamp
#     timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#
#     # Get the file size
#     file_size = len(file)
#
#     # Insert into table
#     c.execute("INSERT INTO files (tag, file_name, file, date, size) VALUES (?, ?, ?, ?, ?)",
#               (tag, file_name, file, timestamp, file_size))
#
#     # Commit changes
#     conn.commit()
#
#
# # def search_files():
# #     search_query = search_entry.get()
# #
# #     # Clear existing search results
# #     for record in trv.get_children():
# #         trv.delete(record)
# #
# #     # Search the database for matching files
# #     c.execute("SELECT * FROM files WHERE file_name LIKE ? OR tag LIKE ?",
# #               ('%' + search_query + '%', '%' + search_query + '%'))
# #     results = c.fetchall()
# #
# #     # Display the search results in the treeview
# #     for row in results:
# #         trv.insert('', 'end', text=row[0], values=(row[1], row[3], row[4]))
#
# def search_files():
#     # Clear existing treeview items
#     trv.delete(*trv.get_children())
#
#     # Get the search keyword from the entry
#     keyword = search_entry.get()
#
#     # Create a database connection and cursor
#     conn = sqlite3.connect('test.db')
#     c = conn.cursor()
#
#     # Fetch records matching the search keyword
#     c.execute("SELECT * FROM files WHERE file_name LIKE ?", ('%' + keyword + '%',))
#     records = c.fetchall()
#
#     # Insert records into the treeview
#     for record in records:
#         trv.insert('', 'end', values=record)
#
#     # Close the database connection
#     conn.close()
#
#
# home_button = Button(root, text='HOME', font=('Georgia', '14'), command=change_to_main)
# home_button.place(relx=0, rely=0)
#
# # Welcome text on the main screen
# main_label = Label(main, text='WELCOME\n WHAT WOULD YOU LIKE TO DO TODAY?', font=('Times New Roman', '32'))
# main_label.place(relx=0, rely=0)
# main_label.grid(pady=20, padx=10)
#
# # Button for file uploads
# upload_file_button = Button(main, text='UPLOAD FILE', pady=20, padx=40, command=change_to_upload)
# upload_file_button.grid(row=2, column=0, padx=10, pady=10)
#
# # Button for browsing files
# browse_files_button = Button(main, text='BROWSE FILES', pady=20, padx=40, command=change_to_category)
# browse_files_button.grid(row=3, column=0, padx=10, pady=10)
#
# # Upload Screen
# file_upload_label = Label(upload, text='FILE UPLOAD', font=('Times New Roman', '32'))
# file_upload_label.place(relx=0.5, rely=0.1, anchor=CENTER)
#
# choose_file_button = Button(upload, text='CHOOSE FILE', padx=10, pady=3, command=lambda: upload_file_com())
# choose_file_button.place(relx=0.01, rely=0.25, anchor=W)
#
# choose_file_label = Label(upload, text="", borderwidth=1, relief='solid', padx=180, pady=6)
# choose_file_label.place(relx=0.13, rely=0.22)
#
# frame_1 = Frame(upload, highlightbackground='gray', highlightthickness=2, padx=10, pady=10)
# frame_1.place(relx=0.3, rely=0.3)
#
# category_label = Label(frame_1, text='SELECT CATEGORY', font=('Times New Roman', '18'), padx=30)
# category_label.pack()
#
# category1 = StringVar(value='Other')
# internal_radio = Radiobutton(frame_1, text='Internal File', value='Internal', variable=category1,
#                              font=('Times New Roman', '14'))
# partners_radio = Radiobutton(frame_1, text='Partners File', value='Partners', variable=category1,
#                              font=('Times New Roman', '14'))
# non_partners_radio = Radiobutton(frame_1, text='Non-Partners File', value='Non-Partners', variable=category1,
#                                  font=('Times New Roman', '14'))
# other_radio = Radiobutton(frame_1, text='Other File', value='Other', variable=category1, font=('Times New Roman', '14'))
#
# internal_radio.pack(padx=10, pady=10)
# partners_radio.pack(padx=10, pady=10)
# non_partners_radio.pack(padx=10, pady=10)
# other_radio.pack(padx=10, pady=10)
#
# frame_2 = Frame(upload, highlightbackground='gray', highlightthickness=2, padx=10, pady=10)
# frame_2.place(relx=0.55, rely=0.3)
#
# save_button = Button(upload, text='SAVE', padx=150, pady=3, command=lambda: save(tag=category1.get(), file_name="file_name", file="file_data"))
# save_button.place(relx=0.3, rely=0.9)
#
# # Category Screen
# categories_label = Label(category, text='CATEGORIES', font=('Times New Roman', '32'))
# categories_label.place(relx=0.5, rely=0.1, anchor=CENTER)
#
# internal_button = Button(category, text='INTERNAL', padx=110, pady=50, command=change_to_search)
# internal_button.place(relx=0.16, rely=0.2)
#
# partners_button = Button(category, text='PARTNERS', padx=90, pady=50, command=change_to_search)
# partners_button.place(relx=0.5, rely=0.2)
#
# non_partners_button = Button(category, text='NON-PARTNERS', padx=90, pady=50, command=change_to_search)
# non_partners_button.place(relx=0.16, rely=0.6)
#
# other_button = Button(category, text='OTHER', padx=120, pady=50, command=change_to_search)
# other_button.place(relx=0.5, rely=0.6)
#
# # Search Screen
# # search_label = Label(search, text='SEARCH', font=('Times New Roman', '32'))
# # search_label.place(relx=0.5, rely=0.1, anchor=CENTER)
# #
# # search_entry = Entry(search, font=('Times New Roman', '14'), width=40)
# # search_entry.grid(row=0, column=0, padx=10, pady=10)
# #
# # search_button = Button(search, text='SEARCH', padx=50, pady=3, command=search_files)
# # search_button.grid(row=0, column=1, padx=10, pady=10)
#
# # search_label = Label(search, text='SEARCH FILES', font=('Times New Roman', '32'))
# # search_label.grid(row=0, column=0, padx=10, pady=10, columnspan=2)
# #
# # search_frame = Frame(search)
# # search_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
# #
# # search_entry = Entry(search_frame, font=('Times New Roman', '14'), width=40)
# # search_entry.pack(side=LEFT, padx=5)
# #
# # search_button = Button(search_frame, text='SEARCH', padx=50, pady=3, command=search_files)
# # search_button.pack(side=LEFT, padx=5)
#
#
# # trv = ttk.Treeview(search, columns=(1, 2, 3), show="headings", height=15)
# # trv.place(relx=0.5, rely=0.5, anchor=CENTER)
# #
# # trv.heading(1, text="Tag")
# # trv.column(1, width=100, anchor=CENTER)
# # trv.heading(2, text="File Name")
# # trv.column(2, width=300, anchor=CENTER)
# # trv.heading(3, text="Size")
# # trv.column(3, width=100, anchor=CENTER)
#
# # trv = ttk.Treeview(search)
# # trv.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
# # trv["columns"] = ("1", "2")
# # trv.column("#0", width=80, anchor='c')
# # trv.column("1", width=10, anchor='c')
# # trv.column("2", width=80, anchor='c')
# # trv.heading("#0", text='Label', anchor='c')
# # trv.heading("1", text='ID', anchor='c')
# # trv.heading("2", text='Name', anchor='c')
# #
# # scroll = ttk.Scrollbar(search, orient='vertical', command=trv.yview)
# # scroll.place(relx=0.95, rely=0.5, anchor=E)
# # trv.configure(yscrollcommand=scroll.set)
#
# search_label = Label(search, text='SEARCH FILES', font=('Times New Roman', '32'))
# search_label.place(relx=0.5, rely=0.1, anchor=CENTER)
#
# search_entry = Entry(search, font=('Times New Roman', '14'), width=40)
# search_entry.place(relx=0.4, rely=0.2, anchor=CENTER)
#
# search_button = Button(search, text='SEARCH', padx=50, pady=3)  # command=search_files)
# search_button.place(relx=0.7, rely=0.2, anchor=CENTER)
#
# trv = ttk.Treeview(search, columns=('1', '2', '3', '4'), show="headings", height=15)
# trv.place(relx=0.5, rely=0.6, anchor=CENTER)
#
# trv.heading(1, text="Tag")
# trv.column(1, width=100, anchor=CENTER)
# trv.heading(2, text="File Name")
# trv.column(2, width=300, anchor=CENTER)
# trv.heading(3, text="Date")
# trv.column(3, width=100, anchor=CENTER)
# trv.heading(4, text="Size")
# trv.column(4, width=100, anchor=CENTER)
#
# scroll = ttk.Scrollbar(search, orient='vertical', command=trv.yview)
# scroll.place(relx=0.95, rely=0.5, anchor=E)
# trv.configure(yscrollcommand=scroll.set)
#
#
# change_to_main()
#
# root.mainloop()
#


import tkinter as tk
from tkinter import ttk


def on_button_click(event):
    item_id = treeview.focus()
    print("Button clicked for item ID:", item_id)


# Create the main window
window = tk.Tk()

# Create a Treeview widget
treeview = ttk.Treeview(window)
treeview.pack()

# Define the columns of the Treeview
treeview["columns"] = ("button",)

# Configure column properties
treeview.column("#0", width=150)
treeview.column("button", width=100)

# Configure column headings
treeview.heading("#0", text="Item")
treeview.heading("button", text="Button")

# Insert tree nodes
item1 = treeview.insert('', 'end', text='Item 1')
item2 = treeview.insert('', 'end', text='Item 2')

# Add buttons to tree nodes
treeview.set(item1, "button", "")
treeview.set(item2, "button", "")

# Bind button click event
treeview.bind("<Button-1>", on_button_click)

# Start the tkinter event loop
window.mainloop()


