from flask import Flask, render_template, request, url_for
from motif_generator import generer_motif

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
            options_str = request.form["options"]
            options = [opt.strip() for opt in options_str.split(",") if opt.strip()]
            image_filename = generer_motif(n_sides, taille, repetitions, angle, couleur, options)
        except Exception as e:
            
            print("Erreur lors de la génération :", e)
    return render_template("index.html", image_filename=image_filename)


if __name__ == "__main__":
    app.run(debug=True)
