import tkinter as tk

from chess_achievements import *

root = tk.Tk()
root.title("Chess.com Achievements Helper")
root.geometry("600x400")

username_var = tk.StringVar()


# function pulled from https://stackoverflow.com/questions/171662/formatting-a-list-of-text-into-columns
def formatcols(mylist, cols):
    maxWidth = max(map(lambda x: len(x), mylist))
    justifyList = list(map(lambda x: x.ljust(maxWidth), mylist))
    lines = (' '.join(justifyList[i:i + cols])
             for i in range(0, len(justifyList), cols))
    return "\n".join(lines)


def format_list(input_list, maxsize):
    size = len(input_list.splitlines())
    return formatcols(input_list.splitlines(), size // maxsize + 1)


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
                                  font=('Courier', 12))
    missing_names = tk.Label(root,
                             text=output,
                             font=('Courier', 10),
                             justify="left")

    missing_names_head.grid(row=2, column=0, columnspan=5)
    missing_names.grid(row=3, column=0, columnspan=5)


# creating a label for
# name using widget Label
username_label = tk.Label(root, text='Username', font=('calibre', 12))

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
