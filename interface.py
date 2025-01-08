import tkinter as tk

from chess_achievements import *

root = tk.Tk()
root.title("Chess.com Achievements Helper")
root.geometry("600x400")

username_var = tk.StringVar()


def submit():
    username = username_var.get()

    try:
        achievement_list = f"Missing Achievements:\n{get_names(get_missing(username))}"
    except KeyError:
        achievement_list = f"Unable to load achievements for user \"{username}\"." \
                           "\nMake sure you input your username correctly"

    missing_names = tk.Label(root,
                             text=achievement_list,
                             font=('calibre', 12))

    missing_names.grid(row=2, column=0, columnspan=3)


# creating a label for
# name using widget Label
username_label = tk.Label(root, text='Username', font=('calibre', 10, 'bold'))

# creating an entry for input
# name using widget Entry
username_entry = tk.Entry(root, textvariable=username_var, font=('calibre', 10, 'normal'))

# creating a button using the widget
# Button that will call the submit function
sub_btn = tk.Button(root,
                    text='Get Missing Achievements',
                    activeforeground="blue",
                    command=lambda: submit())

username_label.grid(row=0, column=0)
username_entry.grid(row=0, column=1)
sub_btn.grid(row=0, column=2)

root.mainloop()
