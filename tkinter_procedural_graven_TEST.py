from tkinter import *

cookie_count = 0


def add_cookie():
    global cookie_count
    cookie_count += 1
    label_counter.config(text=cookie_count)


# creer la fenetre
window = Tk()
window.title("Cookie Clicker")
window.geometry("720x480")
window.iconbitmap("cookie.ico")
window.config(background='#dee5dc')

# ajout du compteur
label_counter = Label(window, text="0", font=("Courrier", 30), bg="#dee5dc")
label_counter.pack()

# creer la frame principale
frame = Frame(window, bg='#dee5dc')
frame_1 = Frame(window, bg="green")

# creation d'image
width = 300
height = 300
image = PhotoImage(file="seed_pumpkin.png").zoom(32).subsample(64)

# ajout du bouton/image
button = Button(frame, image=image, bg='#dee5dc', bd=0, relief=SUNKEN, command=add_cookie)
button.pack()

# ajout écriture
label = Label(frame_1, text=" Test réussi !!!", font=("Helvetica", 20), bg="green", fg ="white")

# ajout de la frame au centre
frame_1.pack()
frame.pack(expand=YES)

# affichage
window.mainloop()