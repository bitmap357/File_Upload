import tkinter
from tkinter import *
from tkinter.messagebox import askyesno
from tkinter import ttk
from tkinter import filedialog
from pathlib import Path
import tkinter.messagebox
import sqlite3
import datetime
import os


frames = []


# Declaring global dictionary
dic = {}
table_name = ''
toplevel = ''
cat = ''

# Creating database and cursor
with sqlite3.connect('test.db') as conn:
    c = conn.cursor()

    # Create table for partners

    c.execute('''CREATE TABLE  IF NOT EXISTS partners (
                tag text,
                file_name text,
                file blob,
                date text,
                size text
                )''')

    # Creating table for non-partners
    c.execute('''CREATE TABLE  IF NOT EXISTS non_partners (
                tag text,
                file_name text,
                file blob,
                date text,
                size text
                )''')

    # Creating table for internal
    c.execute('''CREATE TABLE  IF NOT EXISTS internal (
                tag text,
                file_name text,
                file blob,
                date text,
                size text
                )''')

    # Creating table for other
    c.execute('''CREATE TABLE  IF NOT EXISTS other (
                tag text,
                file_name text,
                file blob,
                date text,
                size text
                )''')


def upload_file_com():
    """Upload a file to the database."""

    # Get the file path from the user.
    file_path = filedialog.askopenfilename(
        filetypes=[("DOCX files", ".docx"), ("TXT files", ".txt"), ("DOC files", ".doc"), ("PDF files", ".pdf")])

    # Check if the user selected a file.
    if file_path:

        # Get the file name and data.
        file_name = Path(file_path).name
        file_data = open(file_path, 'rb').read()
        # Get the file size.
        file_size = file_size_mb(file_path)

        # Update the choose_file_label with the file name.
        choose_file_label.config(text=file_name)

        # Changing state of button to normal because a file is selected
        save_button['state'] = tkinter.NORMAL

        # Insert the file into the treeview.
        trv.insert('', 'end', values=(category1.get(), file_name, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                                      file_size))

        # Dictionary to accept inputs for save function
        global dic
        dic = {
            "file_name": file_name,
            "file": file_data,
            "file_size": file_size
        }

    else:

        # The user did not select a file.
        choose_file_label.config(text="NO FILE CHOSEN")

        # Disabling button because no file is chosen
        save_button['state'] = tkinter.DISABLED


def file_size_mb(file_path):
    size_bytes = os.path.getsize(file_path)
    size_mb = size_bytes / (1024 * 1024)
    rounded = str(round(size_mb, 2)) + " MB"
    return rounded


def change_to_frame(frame):
    """Switch to the specified frame."""
    for f in frames:
        f.pack_forget()  # Hide all frames
    frame.pack(fill='both', expand=1)  # Show the specified frame


def change_to_main():
    """Switch to the main screen."""

    # Hide all frames except the main frame.
    upload.pack_forget()
    category.pack_forget()
    search.pack_forget()
    main.pack(fill='both', expand=1)


def change_to_upload():
    """Switch to the upload screen."""

    # Hide all frames except the upload frame.
    main.pack_forget()
    category.pack_forget()
    search.pack_forget()
    upload.pack(fill='both', expand=1)


def change_to_category():
    """Switch to the category screen."""

    # Hide all frames except the category frame.
    main.pack_forget()
    upload.pack_forget()
    search.pack_forget()
    category.pack(fill='both', expand=1)


def change_to_search(tag=None):
    """Switch to the search screen and display files with the specified tag."""

    # Hide all frames except the search frame.
    main.pack_forget()
    upload.pack_forget()
    category.pack_forget()
    search.pack(fill='both', expand=1)

    # Clear existing treeview items.
    trv.delete(*trv.get_children())

    # Calling global table_name
    global table_name
    global cat
    cat = tag

    # Create a database connection and cursor.
    with sqlite3.connect('test.db') as conn:
        c = conn.cursor()

        if tag:
            # Fetch records matching the specified tag.
            table_name = tag.lower()
            query = "SELECT *, oid FROM {} WHERE tag=?".format(table_name)
            c.execute(query, (tag,))
            records = c.fetchall()

        else:
            # Fetch all records.
            c.execute("""SELECT *, oid FROM partners
                         UNION ALL
                         SELECT *, oid FROM non_partners
                         UNION ALL
                         SELECT *, oid FROM internal
                         UNION ALL
                         SELECT *, oid FROM other""")
            records = c.fetchall()

        # Insert records into the treeview.

        # Inside the `search_files()` function
        for record in records:
            count = 1
            file_size = record[4]
            date = record[3]
            record_display = (record[0], record[1], date, file_size, record[5])
            if count % 2 == 1:
                trv.insert('', 'end', values=record_display, tags=['odd'])
            else:
                trv.insert('', 'end', values=record_display, tags=['even'])

        conn.commit()


def change_to_search_all():
    """Switch to the search screen and display all files."""
    change_to_search()
    treeview_label.config(text="All")
    trv.column("#1", width=100, stretch=tkinter.NO)


def change_to_search_in():
    """Switch to the search screen and display internal files."""
    change_to_search("Internal")
    treeview_label.config(text="Internal")
    trv.column("#1", width=0, stretch=tkinter.NO)


def change_to_search_par():
    """Switch to the search screen and display partner files."""
    change_to_search("Partners")
    treeview_label.config(text="Partners")
    trv.column("#1", width=0, stretch=tkinter.NO)


def change_to_search_non():
    """Switch to the search screen and display non-partner files."""
    change_to_search("Non_Partners")
    treeview_label.config(text="Non-Partners")
    trv.column("#1", width=0, stretch=tkinter.NO)


def change_to_search_oth():
    """Switch to the search screen and display other files."""
    change_to_search("Other")
    treeview_label.config(text="Other")
    trv.column("#1", width=0, stretch=tkinter.NO)


def save(file_name, file, file_size):
    """Save a file to the database."""

    # Get the current timestamp.
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Getting tag from code
    tag = category1.get()

    # Insert into table
    with sqlite3.connect('test.db') as conn:
        c = conn.cursor()
        # Inserting file into partners database
        if tag == "Partners":
            c.execute("INSERT INTO partners (tag, file_name, file, date, size) VALUES (?, ?, ?, ?, ?)",
                      (tag, file_name, file, timestamp, file_size))
        # Inserting file into non-partners database
        if tag == "Non_Partners":
            c.execute("INSERT INTO non_partners (tag, file_name, file, date, size) VALUES (?, ?, ?, ?, ?)",
                      (tag, file_name, file, timestamp, file_size))
        # Inserting file into internal database
        if tag == "Internal":
            c.execute("INSERT INTO internal (tag, file_name, file, date, size) VALUES (?, ?, ?, ?, ?)",
                      (tag, file_name, file, timestamp, file_size))
        # Inserting file into other database
        if tag == "Other":
            c.execute("INSERT INTO other (tag, file_name, file, date, size) VALUES (?, ?, ?, ?, ?)",
                      (tag, file_name, file, timestamp, file_size))
        conn.commit()

    # Pop up message for upload successful
    tkinter.messagebox.showinfo("File Uploaded", "FILE UPLOADED SUCCESSFULLY")
    choose_file_label.config(text="")

    # Disabling button because no file is chosen
    save_button['state'] = tkinter.DISABLED


def search_files():
    """Search for files in the database."""

    # Clear existing treeview items.
    trv.delete(*trv.get_children())

    # Get the search keyword from the entry.
    keyword = search_entry.get()

    # Create a database connection and cursor.
    with sqlite3.connect('test.db') as conn:
        c = conn.cursor()

        # Fetch records matching the search keyword.
        # Calling global table_name
        global table_name

        if table_name == '':
            query = """SELECT * FROM partners WHERE file_name LIKE ?
                     UNION ALL
                     SELECT * FROM non_partners WHERE file_name LIKE ?
                     UNION ALL
                     SELECT * FROM internal WHERE file_name LIKE ?
                     UNION ALL
                     SELECT * FROM other WHERE file_name LIKE ?"""
            c.execute(query, ('%' + keyword + '%', '%' + keyword + '%', '%' + keyword + '%', '%' + keyword + '%'))
            records = c.fetchall()

            for record in records:
                file_size = record[4]
                date = record[3]
                record_display = (record[0], record[1], date, file_size)  # Modified line
                trv.insert('', 'end', values=record_display)

        else:
            query = "SELECT * FROM {} WHERE file_name LIKE ?".format(table_name)

            c.execute(query, ('%' + keyword + '%',))
            records = c.fetchall()

            for record in records:
                file_size = record[4]
                date = record[3]
                record_display = (record[0], record[1], date, file_size)  # Modified line
                trv.insert('', 'end', values=record_display)
        conn.commit()


def popup(event):
    global toplevel
    toplevel = Toplevel(root)

    toplevel.title("")
    toplevel.geometry("250x100")

    l1 = Label(toplevel, image="::tk::icons::question")
    l1.place(relx=0.1, rely=0.2, anchor=CENTER)
    l2 = Label(toplevel, text="What would you like to do?", font=('Times New Roman', '12'))
    l2.place(relx=0.55, rely=0.2, anchor=CENTER)

    b1 = Button(toplevel, text="Delete Entry", command=delete, width=10)
    b1.place(relx=0.25, rely=0.65, anchor=CENTER)
    b2 = Button(toplevel, text="Modify Entry", command=toplevel.destroy, width=10)
    b2.place(relx=0.7, rely=0.65, anchor=CENTER)


# Create function to delete a record
def delete():
    # Message box
    answer = askyesno(title='Delete Entry', message='Are you sure you want to delete the entry?')

    # Function for message box
    if answer:
        # Get the selected item in the tree view
        selected_item = trv.focus()

        # Retrieve the values of the selected item
        values = trv.item(selected_item, 'values')

        # Extract the file name (assuming it's in the second column)
        entry_id = values[4]
        tag = values[0]

        # Create a database connection and cursor.
        with sqlite3.connect('test.db') as conn:
            c = conn.cursor()

        global table_name
        global cat

        if table_name:
            query1 = "DELETE FROM {} WHERE oid=?".format(table_name)
            c.execute(query1, (entry_id,))
            trv.delete(*trv.get_children())
        else:
            table_name1 = tag.lower()
            query1 = "DELETE FROM {} WHERE oid=?".format(table_name1)
            c.execute(query1, (entry_id,))
            trv.delete(*trv.get_children())

        if cat:
            # Fetch records matching the specified tag.
            query = "SELECT *, oid FROM {} WHERE tag=?".format(table_name)
            c.execute(query, (cat,))
            records = c.fetchall()

        else:
            # Fetch all records.
            c.execute("""SELECT *, oid FROM partners
                         UNION ALL
                         SELECT *, oid FROM non_partners
                         UNION ALL
                         SELECT *, oid FROM internal
                         UNION ALL
                         SELECT *, oid FROM other""")
            records = c.fetchall()

        # Insert records into the treeview.
        # Inside the `search_files()` function
        for record in records:
            file_size = record[4]
            date = record[3]
            record_display = (record[0], record[1], date, file_size, record[5])  # Modified line
            trv.insert('', 'end', values=record_display)

        conn.commit()
        toplevel.destroy()


# Create the main window
root = Tk()
root.geometry('880x500')
root.title('File Upload')

# Create the frames.
main = Frame(root, background='tan')
upload = Frame(root, background='tan')
category = Frame(root, background='tan')
search = Frame(root, background='tan')

# Fonts
title_fonts = ('Algerian', '32')
btn_fonts = ('High tower text', '12')

# Pack the main frame.
main.pack(fill='both', expand=1)

# Create the labels and buttons.
home_button = Button(root, text='HOME', font=('Georgia', '14'), command=change_to_main, background='teal', border=5)
home_button.place(relx=0.007, rely=0)


previous_button = Button(root, text='PREVIOUS', font=('Georgia', '14'),
                         command=change_to_main, background='teal', border=5)
previous_button.place(relx=0.86, rely=0)


# Welcome text on the main screen.
main_label = Label(main, text='WELCOME\n WHAT WOULD YOU LIKE TO DO TODAY?', font=title_fonts, background='tan')
main_label.place(relx=0, rely=0)
main_label.grid(pady=20, padx=10)

# Button for file uploads.
upload_file_button = Button(main, text='UPLOAD FILE', font=btn_fonts, pady=20, padx=40,
                            command=change_to_upload, background='silver', border=5)
upload_file_button.grid(row=2, column=0, padx=10, pady=10)

# Button for browsing files.
browse_files_button = Button(main, text='BROWSE FILES', font=btn_fonts, pady=20, padx=40,
                             command=change_to_category, background='silver', border=5)
browse_files_button.grid(row=3, column=0, padx=10, pady=10)

# Upload Screen
file_upload_label = Label(upload, text='FILE UPLOAD', font=title_fonts, background='tan')
file_upload_label.place(relx=0.5, rely=0.1, anchor=CENTER)

choose_file_button = Button(upload, text='CHOOSE FILE', padx=10, pady=3, command=upload_file_com,
                            font=btn_fonts, background='silver')
choose_file_button.place(relx=0.01, rely=0.25, anchor=W)

choose_file_label = Label(upload, text="", borderwidth=1, relief='solid', padx=180, pady=6, background='lavender')
choose_file_label.place(relx=0.17, rely=0.22)

frame_1 = Frame(upload, highlightbackground='gray', highlightthickness=2, padx=35, pady=10, background='lavender')
frame_1.place(relx=0.3, rely=0.3)

category_label = Label(frame_1, text='SELECT CATEGORY', font=('Algerian', '18'), padx=30, background='lavender')
category_label.pack()

category1 = StringVar(value='Other')
internal_radio = Radiobutton(frame_1, text='Internal File', value='Internal', variable=category1,
                             font=('Times New Roman', '14'), background='lavender')
partners_radio = Radiobutton(frame_1, text='Partners File', value='Partners', variable=category1,
                             font=('Times New Roman', '14'), background='lavender')
non_partners_radio = Radiobutton(frame_1, text='Non-Partners File', value='Non_Partners', variable=category1,
                                 font=('Times New Roman', '14'), background='lavender')
other_radio = Radiobutton(frame_1, text='Other File', value='Other', variable=category1,
                          font=('Times New Roman', '14'), background='lavender')

internal_radio.pack(padx=10, pady=10)
partners_radio.pack(padx=10, pady=10)
non_partners_radio.pack(padx=10, pady=10)
other_radio.pack(padx=10, pady=10)

frame_2 = Frame(upload, highlightbackground='gray', highlightthickness=2, padx=10, pady=10)
frame_2.place(relx=0.55, rely=0.3)

save_button = Button(upload, text='SAVE', padx=150, pady=3, state=DISABLED, command=lambda: save(
                     file_name=dic["file_name"], file=dic["file"], file_size=dic["file_size"]), font=btn_fonts,
                     background='cyan', border=5)
save_button.place(relx=0.3, rely=0.9)

# Category Screen
categories_label = Label(category, text='CATEGORIES', font=title_fonts, background='tan')
categories_label.place(relx=0.5, rely=0.1, anchor=CENTER)

internal_button = Button(category, text='INTERNAL', padx=110, pady=50, command=change_to_search_in,
                         background='cyan', border=5)
internal_button.place(relx=0.16, rely=0.2)

partners_button = Button(category, text='PARTNERS', padx=90, pady=50, command=change_to_search_par,
                         background='cyan', border=5)
partners_button.place(relx=0.5, rely=0.2)

non_partners_button = Button(category, text='NON-PARTNERS', padx=90, pady=50, command=change_to_search_non,
                             background='cyan', border=5)
non_partners_button.place(relx=0.16, rely=0.6)

other_button = Button(category, text='OTHER', padx=120, pady=50, command=change_to_search_oth,
                      background='cyan', border=5)
other_button.place(relx=0.5, rely=0.6)

all_button = Button(category, text='ALL', padx=258, pady=15, command=change_to_search_all, background='cyan', border=5)
all_button.place(relx=0.16, rely=0.85)


# Search Screen
search_label = Label(search, text='SEARCH FILES', font=title_fonts, background='tan')
search_label.place(relx=0.5, rely=0.1, anchor=CENTER)

search_entry = Entry(search, font=('Times New Roman', '14'), width=40)
search_entry.place(relx=0.4, rely=0.2, anchor=CENTER)

search_button = Button(search, text='SEARCH', padx=50, pady=3, command=search_files, background='silver')
search_button.place(relx=0.7, rely=0.2, anchor=CENTER)


style = ttk.Style()
style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Calibri', 11))
style.configure("mystyle.Treeview.Heading", font=('Calibri', 13, 'bold'))
style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])


treeview_label = Label(search, text="", font=('Times New Roman', '11'), background='tan')
treeview_label.place(relx=0.5, rely=0.25, anchor=CENTER)

trv = ttk.Treeview(search, columns=('1', '2', '3', '4'), show="headings", height=15, style='mystyle.Treeview')
trv.tag_configure('odd', background='#E8E8E8')
trv.tag_configure('even', background='#DFDFDF')
trv.place(relx=0.5, rely=0.6, anchor=CENTER)

trv.heading(1, text="Tag")
trv.column(1, width=100, anchor=CENTER)
trv.heading(2, text="File Name")
trv.column(2, width=300, anchor=CENTER)
trv.heading(3, text="Date")
trv.column(3, width=150, anchor=CENTER)
trv.heading(4, text="Size")
trv.column(4, width=100, anchor=CENTER)

scroll = ttk.Scrollbar(search, orient='vertical', command=trv.yview)
scroll.place(relx=0.95, rely=0.5, anchor=E)
trv.configure(yscrollcommand=scroll.set)
trv.bind("<Button-1>", popup)


# Start the main loop.
root.mainloop()
