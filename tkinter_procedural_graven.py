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

# creation d'image
width = 80
height = 80
image = PhotoImage(file="seed_pumpkin.png").zoom(50).subsample(100)

# create a canva to graphic creation, here image of pumpkin seed
pumpkin_canva = Canvas(frame, width=width, height=height)
pumpkin_canva.create_image(width/2, height/2, image=image)
pumpkin_canva.grid(row=1, column=1)



# ajout du bouton/image
button = Button(frame, image=image, bg='#dee5dc', bd=0, relief=SUNKEN, command=add_cookie)
button.pack()

# ajout de la frame au centre
frame.pack(expand=YES)

# affichage
window.mainloop()