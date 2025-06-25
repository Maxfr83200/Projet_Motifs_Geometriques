# Projet Motifs Géométriques

Ce projet permet de générer des motifs géométriques via une interface web construite avec Flask, et de les sauvegarder au format image.

---

## Prérequis

- Python 3.8 ou plus
- pip (installé avec Python)
- Accès à Internet (pour installer les bibliothèques)
- Ghostscript (pour enregistrer certaines images)

---

## Installation des dépendances

Ouvrir un terminal, se placer dans le dossier du projet, puis exécuter :

```bash
pip install flask pillow
```

---

## Installation de Ghostscript (Windows)

1. Aller sur le site officiel :  
    [https://ghostscript.com/download/gsdnld.html](https://ghostscript.com/download/gsdnld.html)

2. Télécharger et installer la version **Windows 64-bit** :


## Lancer l'application

Toujours dans le terminal:

```bash
python app.py
```

Puis ouvrir le navigateur et se rendre à l’adresse suivante :

```
http://127.0.0.1:5000/
```

---

## Arborescence typique

```
Projet_Motifs_Geometriques-main/
│
├── app.py
├── motif_generator.py
├── static/
│   ├── images/
│   │  └── motif.png
│   └── css/
│      └── style.css
├── templates/
│   └── index.html
└── README.md
```


## Auteur

Maxence Mounier – ISEN Toulon
