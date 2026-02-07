# Importam "tkinter" - o biblioteca care vine cu Python si ne ajuta sa facem ferestre si butoane
import tkinter as tk

# Importam "random" - o biblioteca care ne ajuta sa generam lucruri aleatorii (pozitii, culori etc.)
import random

# --- Cream fereastra jocului ---
# Tk() creeaza o fereastra noua pe ecran
window = tk.Tk()

# Titlul care apare sus in bara ferestrei
window.title("Prinde Cercurile!")

# Nu lasam fereastra sa fie redimensionata (latimea si inaltimea raman fixe)
window.resizable(False, False)

# Dimensiunile ferestrei in pixeli
WIDTH = 600
HEIGHT = 500

# Cat timp dureaza jocul in secunde
GAME_TIME = 20

# O lista de culori frumoase in format HEX (ca in CSS!)
# Fiecare culoare e un text care incepe cu # urmat de 6 caractere
COLORS = ["#FF6B6B", "#4ECDC4", "#45B7D1", "#96CEB4", "#FFEAA7", "#DDA0DD", "#FF8C00"]

# Variabile care tin minte starea jocului
score = 0                # Scorul jucatorului - incepe de la 0
time_left = GAME_TIME    # Cat timp a mai ramas
circle_id = None         # ID-ul cercului curent (None = nu exista inca)
start_btn = None         # Butonul de start (None = nu exista inca)

# --- Canvas = zona de desen ---
# Canvas e ca o "panza" pe care putem desena forme, text, imagini
# bg = background (culoarea de fundal)
canvas = tk.Canvas(window, width=WIDTH, height=HEIGHT, bg="#1a1a2e")

# pack() pune canvas-ul in fereastra
canvas.pack()

# --- Cream textele care apar pe ecran ---
# create_text() deseneaza text pe canvas
# Parametrii: pozitia (x, y), textul, culoarea (fill), fontul
score_text = canvas.create_text(
    80, 30, text="Scor: 0", fill="white", font=("Arial", 18, "bold")
)
time_text = canvas.create_text(
    WIDTH - 80, 30, text=f"Timp: {GAME_TIME}s", fill="white", font=("Arial", 18, "bold")
)
# Textul din centru - il folosim pentru mesaje (titlu, scor final etc.)
message_text = canvas.create_text(
    WIDTH // 2, HEIGHT // 2, text="", fill="white", font=("Arial", 28, "bold")
)


def show_start_screen():
    """Afiseaza ecranul de start cu titlul si butonul START."""
    global start_btn

    # Punem titlul jocului in centrul ecranului
    canvas.itemconfig(message_text, text="Prinde Cercurile!")

    # Cream un buton de START
    # command = ce functie se apeleaza cand apesi butonul
    start_btn = tk.Button(
        window,
        text="START",
        font=("Arial", 18, "bold"),
        bg="#4ECDC4",       # culoarea de fundal a butonului
        fg="#1a1a2e",       # culoarea textului (inchisa, sa se vada pe fundal deschis)
        width=10,           # latimea butonului
        command=start_game, # cand apesi butonul, porneste jocul
    )
    # place() pune butonul la o pozitie exacta pe ecran
    start_btn.place(x=WIDTH // 2 - 80, y=HEIGHT // 2 + 40)


def start_game():
    """Porneste jocul - reseteaza scorul si timpul, apoi incepe."""
    global score, time_left, start_btn

    # Resetam scorul si timpul
    score = 0
    time_left = GAME_TIME

    # Stergem butonul de start daca exista
    if start_btn:
        start_btn.destroy()  # destroy() sterge butonul de pe ecran
        start_btn = None

    # Actualizam textele de pe ecran
    canvas.itemconfig(score_text, text="Scor: 0")
    canvas.itemconfig(time_text, text=f"Timp: {GAME_TIME}s")
    canvas.itemconfig(message_text, text="")

    # Aratam primul cerc si pornim cronometrul
    show_circle()
    update_timer()


def show_circle():
    """Creeaza un cerc nou intr-o pozitie si culoare aleatoare."""
    global circle_id

    # Daca exista deja un cerc pe ecran, il stergem
    if circle_id:
        canvas.delete(circle_id)

    # Alegem o dimensiune aleatoare intre 25 si 55 de pixeli
    size = random.randint(25, 55)

    # Alegem o pozitie aleatoare pe ecran (dar nu prea la margine)
    x = random.randint(size, WIDTH - size)
    y = random.randint(60, HEIGHT - size)

    # Alegem o culoare aleatoare din lista noastra
    color = random.choice(COLORS)

    # Desenam cercul pe canvas
    # create_oval() deseneaza o forma ovala (cerc daca latimea = inaltimea)
    circle_id = canvas.create_oval(
        x - size, y - size,   # coltul stanga-sus
        x + size, y + size,   # coltul dreapta-jos
        fill=color,           # culoarea de umplere
        outline="white",      # culoarea marginii
        width=2               # grosimea marginii
    )

    # tag_bind() = cand cineva da click pe cerc, apeleaza functia circle_clicked
    canvas.tag_bind(circle_id, "<Button-1>", circle_clicked)


def circle_clicked(event):
    """Cand cineva da click pe cerc, creste scorul si apare un cerc nou."""
    global score

    # Crestem scorul cu 1
    score += 1

    # Actualizam textul scorului pe ecran
    canvas.itemconfig(score_text, text=f"Scor: {score}")

    # Aratam un cerc nou
    show_circle()


def update_timer():
    """Numara timpul inapoi, secunda cu secunda."""
    global time_left

    if time_left > 0:
        # Scadem o secunda
        time_left -= 1

        # Actualizam textul timerului pe ecran
        canvas.itemconfig(time_text, text=f"Timp: {time_left}s")

        # after(1000, ...) = asteapta 1000 milisecunde (1 secunda) apoi cheama din nou update_timer
        window.after(1000, update_timer)
    else:
        # Timpul s-a terminat! Jocul se incheie
        end_game()


def end_game():
    """Afiseaza mesajul de final si butonul de rejucare."""
    global start_btn

    # Stergem cercul ramas pe ecran
    if circle_id:
        canvas.delete(circle_id)

    # Afisam scorul final in centrul ecranului
    canvas.itemconfig(message_text, text=f"Timpul a expirat!\nScor final: {score}")

    # Cream butonul "Joaca din nou!"
    start_btn = tk.Button(
        window,
        text="Joaca din nou!",
        font=("Arial", 14, "bold"),
        bg="#4ECDC4",
        fg="#1a1a2e",
        command=start_game,  # apasand butonul, reporneste jocul
    )
    start_btn.place(x=WIDTH // 2 - 70, y=HEIGHT // 2 + 60)


# --- Aici incepe programul ---
# Afisam ecranul de start
show_start_screen()

# mainloop() tine fereastra deschisa si asteapta actiuni (click-uri, taste etc.)
# Fara aceasta linie, fereastra s-ar inchide imediat!
window.mainloop()
