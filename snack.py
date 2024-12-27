import tkinter as tk
from tkinter import ttk

produits = {
    "Pizza": {"prix": 40.00,},
    "Tacos": {"prix": 49.00,},
    "Sandwich": {"prix": 30.00,},
    "Burger": {"prix": 32.00,},
    "Frites": {"prix": 15.00,},
    "Nuggets": {"prix": 35.00,},
    "Soda": {"prix": 15.00,},
    "Limonade": {"prix": 18.00,}
}

def calculer_total():
    """Calcule le total des produits sélectionnés."""
    total = 0
    for produit, details in produits.items():
        quantite = spinboxes[produit].get()
        try:
            total += int(quantite) * details["prix"]
        except ValueError:
            pass
    total_label.config(text=f"Total: {total:.2f} DH")

def reinitialiser():
    """Réinitialise la sélection et le total."""
    for spinbox in spinboxes.values():
        spinbox.delete(0, tk.END)
        spinbox.insert(0, 0)
    total_label.config(text="Total: 0.00 DH")

fenetre = tk.Tk()
fenetre.title("MENU d'UN Snacks")
fenetre.geometry("1000x1000")
fenetre.config(bg="#560319")

label = tk.Label(fenetre, text= "Bienvenue dans notre snack, où des saveurs simples et délicieuses vous attendent à chaque bouchée !", font=("Arial", 13, "italic"), bg="#560319", fg="#FAF5EF")
label.pack(pady=10)

produit_frame = tk.Frame(fenetre, bg="#B38481")
produit_frame.pack()

spinboxes = {}

for i, (produit, details) in enumerate(produits.items()):
    if i % 2 == 0: 
        ligne_frame = tk.Frame(produit_frame, bg="#FAF5EF")
        ligne_frame.pack(fill="x", padx=15, pady=15)

    frame = tk.Frame(ligne_frame, bg="#FAF5EF")
    frame.pack(side="left", padx=(15, 40)) 

    info_frame = tk.Frame(frame, bg="#FAF5EF")
    info_frame.pack(side="left", padx=15) 
    tk.Label(info_frame, text=f"{produit} - {details['prix']:.2f} DH", font=("Arial", 12), bg="#FAF5EF").pack(anchor="w")

    spinbox = tk.Spinbox(info_frame, from_=0, to=100, width=5, font=("Arial", 12), justify="center")
    spinbox.pack(anchor="w", pady=10) 
    spinbox.delete(0, tk.END)
    spinbox.insert(0, 0)
    spinboxes[produit] = spinbox

calculer_button = tk.Button(fenetre, text="Calculer le total", command=calculer_total, font=("Arial", 12, "bold"), bg="#B38481", fg="WHITE", activebackground="#DCDCDC")
calculer_button.pack(pady=15) 

total_label = tk.Label(fenetre, text="Total: 0.00 DH", font=("Arial", 14, "bold"), bg="white", fg="#560319")
total_label.pack(pady=15)

reinitialiser_button = tk.Button(fenetre, text="Réinitialiser", command=reinitialiser, font=("Arial", 12, "bold"), bg="#B38481", fg="WHITE", activebackground="#DCDCDC")
reinitialiser_button.pack(pady=10) 

footer_label = tk.Label(fenetre, text="Bon appétit !😋 merci de votre visite !", font=("Arial", 12, "italic"), bg="#560319", fg="#DCDCDC")
footer_label.pack(pady=15)  

fenetre.mainloop()
