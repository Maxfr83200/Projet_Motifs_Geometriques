from flask import Flask, render_template, request, url_for
from motif_generator import generer_motif
import time

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    
    image_filename = None
    
    if request.method == "POST":
        try:
            n_sides = int(request.form["n_sides"])
            taille = int(request.form["taille"])
            repetitions = int(request.form["repetitions"])
            angle = float(request.form["angle"])
            couleur = request.form["couleur"]
            
            
            style = request.form.get("style", "normal")  # valeur par défaut : normal
            spirale = "spirale" in request.form  # True si coché
            
            options = [style]
            if spirale:
                options.append("spirale")
            
            image_filename = generer_motif(n_sides, taille, repetitions, angle, couleur, options)
        except Exception as e:
            
            print("Erreur lors de la génération :", e)
    return render_template('index.html', image_filename=image_filename, timestamp=time.time())


if __name__ == "__main__":
    app.run(debug=True)
