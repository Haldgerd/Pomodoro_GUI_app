import tkinter
from PIL import ImageTk, Image

# ---- CONSTANTS ----
TIME = "00:00"
BIG_TEXT = ("gothic", 30, "bold")
TEXT = ("Arial", 15, "bold")
TEAL = "#239E9A"
BLACK = "#09061A"
POMODORO = 25
SHORT_BREAK = 5
LONG_BREAK = 30

# ----- FUNCTIONS ------


# ------ UI DESIGN ------

window = tkinter.Tk()
window.title("POMODORO")

# locking window settings
window.maxsize(width=450, height=750)
window.minsize(width=450, height=750)

window.geometry("450x750")
window.config(padx=20)
window["bg"] = TEAL   # sets the color of the window background

# add an icon to left corner of root window
window.iconphoto(False, tkinter.PhotoImage(file="./Images/tomato_icon.png"))

# add main image on root window
main_image = Image.open("./Images/POMODORO.png")
main_pomodoro = ImageTk.PhotoImage(main_image)

image_main_label = tkinter.Label(image=main_pomodoro, bg=TEAL)
image_main_label.image = main_pomodoro
image_main_label.pack(side="top", pady=30)

# adding text labels(studying - quote for studying, short break)
text_label = tkinter.Label(text="Working", font=TEXT, bg=TEAL)
text_label.pack(side="top", pady=10)

# time label
time_label = tkinter.Label(text=f"{TIME}", font=BIG_TEXT, bg=TEAL)
time_label.pack(side="top")

# create two buttons, start and reset
button_start = tkinter.Button(text="START", bg="white", fg=BLACK)
button_start.pack(side="left", padx=60)

button_reset = tkinter.Button(text="RESET", bg="white", fg=BLACK)
button_reset.pack(side="right", padx=60)

# to keep window open:
window.mainloop()

