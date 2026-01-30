# Open-MES: Flux-Qualité-GMP 🚀
### Digitalisation de l'Assurance Qualité & Industrialisation (Prototype Power Platform)

## 📌 Présentation du Projet
Ce projet est une **Preuve de Concept (POC)** complète visant à digitaliser les check-lists métiers au sein d'un département d'industrialisation spécialisé dans les **GMP (Groupe Moto-Propulseur)** et châssis (Secteur Automobile).

L'objectif est de remplacer les processus manuels par un écosystème robuste sous **Microsoft Power Platform** afin d'assurer le suivi de l'avancement de l'implémentation industrielle en temps réel.

---

## 🛠️ Méthodologie & Réalisation (Cycle de vie du projet)

### 1️⃣ Phase d'Analyse (Ingénierie des besoins)
* **Interviews Utilisateurs :** Réalisation de l'histoire utilisateur (User Stories) pour identifier les besoins des opérationnels terrain (Qualité & Production).
* **Analyse de Processus :** Identification des opportunités d'automatisation pour réduire les temps de cycle entre le contrôle et le reporting décisionnel.
* **Livrable :** Voir `phase_01_analyse_besoins/`.

### 2️⃣ Phase de Conception (Data Architecture)
* **Relations Entités :** Modélisation des interactions entre les intervenants, les actifs industriels et les référentiels de contrôle.
* **Complexité de la Base de Données :** Conception d'un schéma SQL relationnel optimisé pour une migration vers **Dataverse** ou **SharePoint**.
* **Maquettage UX/UI :** Design d'une interface Power Apps ergonomique pour terminaux mobiles en usine.
* **Livrable :** Voir `phase_02_conception_donnees/`.

### 3️⃣ Phase de Développement & Test (Moteur de Données)
* **Simulation de Flux :** Développement d'un moteur en Python pour valider l'intégrité de l'architecture avant le déploiement.
* **Logique d'Automatisation :** Configuration conceptuelle de workflows **Power Automate** (Notifications de blocage et escalade managériale).
* **Stratégie de Déploiement :** Plan de transition vers l'environnement collaboratif **MS365**.
* **Livrable :** Voir `phase_03_development/`.

---

## 📖 Comment explorer ce projet ?
1. **Architecture :** Parcourir les dossiers `phase_01` à `phase_03` pour suivre la logique projet.
2. **Démonstration Technique :** Lancer `python phase_03_development/simulateur_flux_gmp.py` pour générer les indicateurs (KPIs) en temps réel.
3. **Vision Cible :** Consulter `DEPLOYMENT_PLAN.md` pour comprendre l'intégration finale dans l'écosystème Power Platform.