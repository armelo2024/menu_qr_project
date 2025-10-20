from fpdf import FPDF
import os

os.makedirs("static/menus", exist_ok=True)

class PDFMenu(FPDF):
    def header(self):
        self.set_font("Arial", 'B', 24)
        self.set_text_color(212, 175, 55)
        self.cell(0, 15, "SmartMenu Africa", ln=True, align='C')
        self.ln(5)

def create_menu_pdf(filename, title, sections):
    pdf = PDFMenu()
    pdf.add_page()

    # Fond doré léger
    pdf.set_fill_color(255, 244, 200)
    pdf.rect(0, 0, 210, 297, 'F')

    pdf.set_font("Arial", 'B', 20)
    pdf.set_text_color(50, 50, 50)
    pdf.cell(0, 12, title, ln=True, align='C')
    pdf.ln(5)

    pdf.set_font("Arial", '', 14)
    for section, items in sections.items():
        pdf.set_font("Arial", 'B', 16)
        pdf.set_text_color(150, 100, 0)
        pdf.cell(0, 10, section, ln=True)

        pdf.set_font("Arial", '', 14)
        pdf.set_text_color(0, 0, 0)
        for item, price in items.items():
            pdf.cell(0, 8, f"{item} - {price} FCFA", ln=True)
        pdf.ln(4)

    pdf.output(filename, "F")

restaurant_menu = {
    "Entrees": {"Salade ivoirienne": "2000", "Pastels de poisson": "2500"},
    "Plats": {"Attieke au poulet braise": "3500", "Poisson thon grille": "4000", "Riz sauce graine": "3000"},
    "Desserts": {"Banane flambee": "2000", "Salade de fruits": "1500"},
    "Boissons": {"Jus naturels": "1000", "Eau minerale": "500", "Vin rouge": "5000"}
}

bar_menu = {
    "Cocktails": {"Mojito": "4000", "Caipirinha": "4500", "Pina Colada": "5000"},
    "Bieres": {"Heineken": "2000", "Flag": "1500", "Guinness": "2000"},
    "Snacks": {"Ailes de poulet": "3000", "Brochettes": "2500", "Plantains grilles": "2000"}
}

hotel_menu = {
    "Petit-dejeuner": {"Omelette complete": "2500", "Croissants et cafe": "2000"},
    "Dejeuner": {"Poulet sauce arachide": "4000", "Poisson braise": "4500"},
    "Diner": {"Soupe de legumes": "3000", "Spaghetti bolognaise": "3500"},
    "Boissons": {"Eau minerale": "500", "Jus naturel": "1500", "Vin rouge": "5000"}
}

create_menu_pdf("static/menus/resto1_menu.pdf", "Le Prestige - Restaurant", restaurant_menu)
create_menu_pdf("static/menus/bar1_menu.pdf", "Sky Lounge - Bar", bar_menu)
create_menu_pdf("static/menus/hotel1_menu.pdf", "Hotel Riviera - Hotel et Suites", hotel_menu)

print("✅ Menus PDF créés dans static/menus/")
