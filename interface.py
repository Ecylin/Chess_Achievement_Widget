import tkinter as tk
import webbrowser

from chess_achievements import *
from format import *

width = 600
height = 400

root = tk.Tk()
root.title("Chess.com Achievements Helper")
root.geometry(f"{str(width)}x{str(height)}")

username_var = tk.StringVar()


def callback(url):
    webbrowser.open_new(url)


def submit():
    username = username_var.get()

    try:
        achievement_list = f"{get_names(get_missing(username))}"
        output = format_list(achievement_list, 40)

    except KeyError:
        output = f"Unable to load achievements for user \"{username}\"." \
                 "\nMake sure you input your username correctly"

    missing_names_head = tk.Label(root,
                                  text=f"Missing Achievements for \"{username}\":",
                                  font=('Courier', 14))
    missing_names = tk.Label(root,
                             text=output,
                             font=('Courier', 12),
                             justify="left",
                             cursor="star")

    missing_names_head.grid(row=2, column=0, columnspan=5)
    missing_names.grid(row=3, column=0, columnspan=5)
    missing_names.bind("<Button-1>", lambda e: callback("https://www.chess.com/blog/Nevisaurus_Rex/"
                                                        "list-of-all-achievements-1"))


# creating a label for
# name using widget Label
username_label = tk.Label(root, text='Username', font=('Courier', 12))

# creating an entry for input
# name using widget Entry
username_entry = tk.Entry(root, textvariable=username_var, font=('Courier', 10, 'normal'))

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
