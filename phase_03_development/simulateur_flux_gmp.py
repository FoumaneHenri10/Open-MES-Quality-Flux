import sqlite3
import pandas as pd
from datetime import datetime

class GMPQualityEngine:
    def __init__(self, db_name="../data/industrial_quality.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._setup_database()

    def _setup_database(self):
        """Crée l'architecture complexe demandée par l'offre"""
        # Table des Actifs Industriels
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS assets (
            id INTEGER PRIMARY KEY, code_poste TEXT, label TEXT, criticite INT)''')
        
        # Table des Check-lists (Le cœur de l'outil Power Platform)
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS check_lists (
            id INTEGER PRIMARY KEY, asset_id INT, operateur TEXT, 
            statut TEXT, date_valid TIMESTAMP,
            FOREIGN KEY(asset_id) REFERENCES assets(id))''')
        
        self.conn.commit()

    def injecter_donnees_terrain(self, code_poste, operateur, statut):
        """Simule une saisie via Power Apps qui arrive dans la base"""
        query = "INSERT INTO check_lists (asset_id, operateur, statut, date_valid) VALUES ((SELECT id FROM assets WHERE code_poste=?), ?, ?, ?)"
        self.cursor.execute(query, (code_poste, operateur, statut, datetime.now()))
        self.conn.commit()
        
    def generer_rapport_avancement(self):
        """La fonction qui prouve ton aptitude à l'analyse (KPIs)"""
        return pd.read_sql_query("SELECT statut, COUNT(*) as nb FROM check_lists GROUP BY statut", self.conn)
    
    def verifier_alertes_critiques(self):
        """Analyse des processus et identification d'opportunités d'automatisation"""
        self.cursor.execute("SELECT code_poste FROM check_lists JOIN assets ON assets.id = check_lists.asset_id WHERE statut='Bloqué'")
        alertes = self.cursor.fetchall()
        for alerte in alertes:
            print(f"⚠️ ALERT POWER AUTOMATE : La ligne {alerte[0]} est à l'arrêt. Notification envoyée au Manager.")

# --- INSTANCIATION POUR L'ENTRETIEN ---
engine = GMPQualityEngine()
# Simulation de saisies réelles
engine.injecter_donnees_terrain('VAL-GMP-L1', 'M. FOUMANE', 'Validé')
engine.injecter_donnees_terrain('VAL-GMP-L2', 'M. FOUMANE', 'Bloqué')

print("📊 TABLEAU DE BORD DE L'AVANCEMENT :")
print(engine.generer_rapport_avancement())