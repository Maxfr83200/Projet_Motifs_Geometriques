from flask import Flask, render_template, request, url_for
from motif_generator import generer_motif

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            n_sides = int(request.form["n_sides"])
            taille = int(request.form["taille"])
            repetitions = int(request.form["repetitions"])
            angle = float(request.form["angle"])
            couleur = request.form["couleur"]
            options_str = request.form["options"]
            options = [opt.strip() for opt in options_str.split(",") if opt.strip()]
            generer_motif(n_sides, taille, repetitions, angle, couleur, options)
            return render_template("index.html", image_url="motif.png")
        except Exception as e:
            return f"Erreur : {e}"
    return render_template("index.html", image_url="static/motif.png")


if __name__ == "__main__":
    app.run(debug=True)
