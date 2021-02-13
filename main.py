import tkinter
from PIL import ImageTk, Image

# ---- CONSTANTS ----
TIME = "00:00"
BIG_TEXT = ("gothic", 40, "bold")
TEXT = ("Arial", 20, "bold")
TEAL = "#2AA19B"
BLACK = "#09061A"
YELLOW = "#F2C830"
POMODORO = 25
SHORT_BREAK = 5
LONG_BREAK = 30

# ----- FUNCTIONS ------


# ------ UI DESIGN ------
window = tkinter.Tk()
window.title("POMODORO")

# locking window settings
window.resizable(width=0, height=0)

window.geometry("450x750")
window.config(padx=20, pady=20)
window["bg"] = TEAL   # sets the color of the window background

# add an icon to left corner of root window
window.iconphoto(False, tkinter.PhotoImage(file="./Images/tomato_icon.png"))

# add main image on root window
main_image = Image.open("./Images/POMODORO.png")
main_pomodoro = ImageTk.PhotoImage(main_image)

image_main_label = tkinter.Label(image=main_pomodoro, bg=TEAL)
image_main_label.image = main_pomodoro
image_main_label.pack(side="top", pady=20)

# adding text labels(studying - quote for studying, short break)
text_label = tkinter.Label(text="Working", font=TEXT, bg=TEAL)
text_label.pack(side="top", pady=10)

# -----time label-----
time_label = tkinter.Label(text=f"{TIME}", font=BIG_TEXT, bg=TEAL)
time_label.pack(side="top")

# -----create two buttons, start and reset-----
button_reset = tkinter.Button(window, text="Reset", bg="white", fg=BLACK, width=60, highlightthickness=0)
# include activebackground=YELLOW for making background on hoover change to desired color.
button_reset.pack(side="bottom", pady=20, padx=50)

button_start = tkinter.Button(window, text="Start", bg="white", fg=BLACK, width=60, highlightthickness=0)
button_start.pack(side="bottom", padx=50)


# to keep window open:
window.mainloop()

