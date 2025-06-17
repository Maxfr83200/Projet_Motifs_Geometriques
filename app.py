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
            
            
            style = request.form.get("style", "normal")  
            
            options = [style]
            if "spirale" in request.form:
                options.append("spirale")
            if "miroir" in request.form:
                options.append("miroir")
            if "coins" in request.form:
                options.append("coins")
            
            image_filename = generer_motif(n_sides, taille, repetitions, angle, couleur, options)
        except Exception as e:
            
            print("Erreur lors de la génération :", e)
    return render_template('index.html', image_filename=image_filename, timestamp=time.time())


if __name__ == "__main__":
    app.run(debug=True)
