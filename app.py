from flask import Flask, render_template, send_from_directory, jsonify, request
import qrcode
import os

app = Flask(__name__)

# === CONFIGURATION ===
QR_FOLDER = "static/qr_codes"
os.makedirs(QR_FOLDER, exist_ok=True)

PUBLIC_URL = "https://menu-qr-project.onrender.com"
qr_path = os.path.join(QR_FOLDER, "menu_global.png")

# === GÉNÉRATION DU QR CODE ===
qr = qrcode.QRCode(version=1, box_size=4, border=2)
qr.add_data(PUBLIC_URL)
qr.make(fit=True)
img = qr.make_image(fill='black', back_color='white')
img.save(qr_path)

# === DONNÉES SIMULÉES (bientôt remplaçables par une base) ===
establishments = [
    {
        "id": "resto1",
        "name": "Le Prestige",
        "type": "Restaurant",
        "description": "Cuisine africaine et européenne raffinée.",
        "menu_url": "/menus/resto1_menu.pdf",
        "image_url": "/static/images/le-prestige.png",
        "location": "Abidjan, Cocody"
    },
    {
        "id": "bar1",
        "name": "Sky Bar Lounge",
        "type": "Bar",
        "description": "Cocktails maison et musique live chaque week-end.",
        "menu_url": "/menus/bar1_menu.pdf",
        "image_url": "/static/images/download sky.png",
        "location": "Yopougon, Sideci"
    },

    
    {
        "id": "hotel1",
        "name": "Hôtel Oasis",
        "type": "Hôtel",
        "description": "Hôtel 4 étoiles avec piscine, spa et restaurant panoramique.",
        "menu_url": "/menus/hotel1_menu.pdf",
        "image_url": "/static/images/oasis1.jpg",
        "location": "Grand-Bassam"
    }

    
]

# === ROUTES WEB ===
@app.route("/")
def qr_page():
    return render_template("qr_page.html")

@app.route("/main")
def main_page():
    return render_template("index.html")

@app.route("/menus/<path:filename>")
def download_menu(filename):
    return send_from_directory("static/menus", filename)

# === ROUTES API ===
@app.route("/api/establishments")
def get_all_establishments():
    """Retourne la liste complète des établissements."""
    return jsonify(establishments)

@app.route("/api/establishments/<est_id>")
def get_establishment(est_id):
    """Retourne les détails d’un établissement spécifique."""
    est = next((e for e in establishments if e["id"] == est_id), None)
    if est:
        return jsonify(est)
    return jsonify({"error": "Établissement non trouvé"}), 404

@app.route("/api/search")
def search_establishments():
    """Filtre les établissements par type ou nom."""
    est_type = request.args.get("type")
    name = request.args.get("name")

    results = establishments

    if est_type:
        results = [e for e in results if e["type"].lower() == est_type.lower()]
    if name:
        results = [e for e in results if name.lower() in e["name"].lower()]

    return jsonify(results)


@app.route("/establishment/<est_id>")
def establishment_detail(est_id):
    """Affiche la page de détails d’un établissement."""
    est = next((e for e in establishments if e["id"] == est_id), None)
    if est:
        return render_template("details.html", establishment=est)
    return "Établissement non trouvé", 404


if __name__ == "__main__":
    app.run(debug=True)


# app = Flask(__name__)

# QR_FOLDER = "static/qr_codes"
# os.makedirs(QR_FOLDER, exist_ok=True)


# global_qr_path = os.path.join(QR_FOLDER, "menu_global.png")
# url = "https://thumblike-unactionable-tawanna.ngrok-free.dev"  

# qr = qrcode.QRCode(version=1, box_size=10, border=5)
# qr.add_data(url)
# qr.make(fit=True)
# img = qr.make_image(fill='black', back_color='white')
# img.save(global_qr_path)


# @app.route("/")
# def index():
#     return render_template("index.html", establishments=establishments, global_qr="qr_codes/menu_global.png")

# @app.route("/menu/<est_id>")
# def menu(est_id):
#     est = next((e for e in establishments if e["id"] == est_id), None)
#     if est:
#         return render_template("menu.html", establishment=est)
#     return "Établissement non trouvé", 404

# @app.route("/menus/<path:filename>")
# def download_menu(filename):
#     return send_from_directory("static/menus", filename)

# if __name__ == "__main__":
#     app.run(debug=True)








# app = Flask(__name__)

# QR_FOLDER = "static/qr_codes"
# os.makedirs(QR_FOLDER, exist_ok=True)

# def get_ngrok_url():
#     """
#     Récupère automatiquement le lien ngrok public actif
#     depuis l'API locale de ngrok.
#     """
#     try:
#         response = requests.get("http://127.0.0.1:4040/api/tunnels")
#         data = response.json()
#         public_url = data["tunnels"][0]["public_url"]
#         return public_url
#     except Exception as e:
#         print("⚠️ Impossible de récupérer le lien ngrok :", e)
#         return None

# global_qr_path = os.path.join(QR_FOLDER, "menu_global.png")
# url = get_ngrok_url()

# if url:
#     print(f"✅ Lien public détecté : {url}")
# else:
#     url = "https://thumblike-unactionable-tawanna.ngrok-free.dev"
#     print("ℹ️ Aucun tunnel ngrok trouvé, utilisation du lien local.")

# qr = qrcode.QRCode(version=1, box_size=10, border=5)
# qr.add_data(url)
# qr.make(fit=True)
# img = qr.make_image(fill="black", back_color="white")
# img.save(global_qr_path)

# @app.route("/")
# def index():
#     return render_template("index.html", establishments=establishments, global_qr="qr_codes/menu_global.png")

# @app.route("/menu/<est_id>")
# def menu(est_id):
#     est = next((e for e in establishments if e["id"] == est_id), None)
#     if est:
#         return render_template("menu.html", establishment=est)
#     return "Établissement non trouvé", 404

# @app.route("/menus/<path:filename>")
# def download_menu(filename):
#     return send_from_directory("static/menus", filename)

# if __name__ == "__main__":
#     app.run(debug=True)




