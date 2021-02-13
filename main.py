import tkinter

# ---- CONSTANTS ----
TEAL = "#2BC4BF"
BLACK = "#09061A"
POMODORO = 25
SHORT_BREAK = 5
LONG_BREAK = 30

# ----- FUNCTIONS ------


# ------ UI DESIGN ------

window = tkinter.Tk()
window.title("POMODORO")

window.maxsize(width=700, height=650)
window.geometry("700x650")
window["bg"] = TEAL   # sets the color of the window background

# add an icon to left corner of root window
window.iconphoto(False, tkinter.PhotoImage(file="./Images/ICON_POMODORO.jpeg"))


# to keep window open:
window.mainloop()

