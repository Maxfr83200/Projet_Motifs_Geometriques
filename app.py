from flask import Flask, render_template, request, url_for
from motif_generator import generer_motif
import time
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    
    image_filename = None
    
    # Traitement du formulaire envoyé par l'utilisateur
    if request.method == "POST":
        try:
            n_sides = int(request.form["n_sides"])
            taille = int(request.form["taille"])
            repetitions = int(request.form["repetitions"])
            angle = float(request.form["angle"])
            couleur = request.form["couleur"]
            
            
            style = request.form.get("style", "normal")  
            
            options = [style]
            if "spirale" in request.form:
                options.append("spirale")
            if "miroir" in request.form:
                options.append("miroir")
            if "coins" in request.form:
                options.append("coins")
            
            # Génération du motif et récupération du nom du fichier image
            image_filename = generer_motif(n_sides, taille, repetitions, angle, couleur, options)
        except Exception as e:   
            print("Erreur lors de la génération :", e)  
               
    else:  # Méthode GET → supprimer motif.png s'il existe
        motif_path = "static/images/motif.png"
        if os.path.exists(motif_path):
            os.remove(motif_path)
            
    # Si le motif a été généré, on passe le nom du fichier à la template# Affichage de la page avec le nom de l'image générée (ou None) et un timestamp pour éviter le cache navigateur   
    return render_template('index.html', image_filename=image_filename, timestamp=time.time())


if __name__ == "__main__":
    # Lancement de l'application Flask en mode debug
    app.run(debug=True)
