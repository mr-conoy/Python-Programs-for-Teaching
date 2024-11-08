from tkinter import HIDDEN, NORMAL, Tk, Canvas

def toggle_eyes():
    current_color = c.itemcget(eye_left, 'fill')
    new_color = c.body_color if current_color == 'white' else 'white'
    current_state = c.itemcget(pupil_left, 'state')
    new_state = NORMAL if current_state == HIDDEN else HIDDEN
    c.itemconfigure(pupil_left, state=new_state)
    c.itemconfigure(pupil_right, state=new_state)
    c.itemconfigure(eye_left, fill=new_color)
    c.itemconfigure(eye_right, fill=new_color)

def blink():
    toggle_eyes()
    root.after(250, toggle_eyes)
    root.after(3000, blink)

def toggle_pupils():
    if not c.crossed_eyes:
        c.move(pupil_left, 10, -5)
        c.move(pupil_right, -10, -5)
        c.crossed_eyes = True
    else:
        c.move(pupil_left, -10, 5)
        c.move(pupil_right, 10, 5)
        c.crossed_eyes = False

def toggle_tongue():
    if not c.tongue_out:
        c.itemconfigure(tongue, state=NORMAL)
        c.tongue_out = True
    else:
        c.itemconfigure(tongue, state=HIDDEN)
        c.tongue_out = False

def cheeky(event):
    toggle_tongue()
    toggle_pupils()
    hide_happy(event)
    root.after(1000, toggle_tongue)
    root.after(1000, toggle_pupils)
    return

def show_happy(event):
    if (20 <= event.x <= 350) and (20 <= event.y <= 350):
        c.itemconfigure(cheek_left, state=NORMAL)
        c.itemconfigure(cheek_right, state=NORMAL)
        c.itemconfigure(mouth_happy, state=NORMAL)
        c.itemconfigure(mouth_normal, state=HIDDEN)
        c.itemconfigure(mouth_sad, state=HIDDEN)
        c.happy_level = 10
    return

def hide_happy(event):
    c.itemconfigure(cheek_left, state=HIDDEN)
    c.itemconfigure(cheek_right, state=HIDDEN)
    c.itemconfigure(mouth_happy, state=HIDDEN)
    c.itemconfigure(mouth_normal, state=NORMAL)
    c.itemconfigure(mouth_sad, state=HIDDEN)
    return

def sad():
    if c.happy_level == 0:
        c.itemconfigure(mouth_happy, state=HIDDEN)
        c.itemconfigure(mouth_normal, state=HIDDEN)
        c.itemconfigure(mouth_sad, state=NORMAL)
    else:
        c.happy_level -= 1
    root.after(5000, sad)

root = Tk()
c = Canvas(root, width=400, height=400)
c.configure(bg='dark blue', highlightthickness=0)
c.body_color = 'SkyBlue1'
body = c.create_oval(35, 20, 365, 350, outline=c.body_color, fill=c.body_color)
ear_left = c.create_oval(75, 70, 75+40, 70+60, outline=c.body_color, fill=c.body_color)
ear_right = c.create_oval(285, 70, 285+40, 70+60, outline=c.body_color, fill=c.body_color)
foot_left = c.create_oval(65, 320, 65+75, 320+20, outline=c.body_color, fill=c.body_color)
foot_right = c.create_oval(260, 320, 260+75, 320+20, outline=c.body_color, fill=c.body_color)

eye_left = c.create_oval(130, 110, 130+50, 110+60, outline='black', fill='white')
pupil_left = c.create_oval(140, 110, 140+20, 110+40, outline='black', fill='black', state=NORMAL)
eye_right = c.create_oval(230, 110, 230+50, 110+60, outline='black', fill='white')
pupil_right = c.create_oval(240, 110, 240+20, 110+40, outline='black', fill='black', state=NORMAL)

mouth_normal = c.create_line(170, 250, 200, 272, 230, 250, smooth=1, width=2, state=NORMAL)
mouth_happy = c.create_line(170, 250, 200, 282, 230, 250, smooth=1, width=2, state=HIDDEN)
mouth_sad = c.create_line(170, 250, 200, 232, 230, 250, smooth=1, width=2, state=HIDDEN)

tongue_main = c.create_rectangle(170, 250, 230, 290, outline='red', fill='red', state=NORMAL)
tongue_tip = c.create_oval(170, 285, 230, 300, outline='red', fill='red', state=NORMAL)

cheek_left = c.create_oval(70, 180, 120, 230, outline='pink', fill='pink', state=HIDDEN)
cheek_right = c.create_oval(280, 180, 330, 230, outline='pink', fill='pink', state=HIDDEN)

c.pack()

c.bind('<Motion>', show_happy)
c.bind('<Leave>', hide_happy)
c.bind('<Double-1>', cheeky)

c.happy_level = 10
c.eyes_crossed = False
c.tongue_out = False

root.after(1000, blink)
root.after(5000, sad)
root.mainloop()  # Start the Tkinter event loop
