# Phase 3 : Développement & Validation du Flux

Développement de la logique "Back-end" simulant l'intelligence de l'outil Power Platform.

### ⚙️ Composants Techniques
* **Script Python :** Moteur de simulation de données pour tester la robustesse des calculs de taux de conformité.
* **Logique de Validation :** Scripts SQL assurant que les données transmises aux futurs tableaux de bord Power BI sont propres et cohérentes.

### 📋 Tests & Déploiement
* Simulation de tests de montée en charge (ingestion de 1000 check-lists simultanées).
* Préparation des fichiers d'export pour l'intégration finale dans l'environnement Microsoft 365.

### 🧪 Stratégie de Test et Validation
Pour valider la robustesse du modèle de données avant le déploiement sur la Power Platform, nous mettons en place :
1. **Un générateur de flux :** Simulation de saisies de check-lists provenant de différents ateliers.
2. **Un script de contrôle de cohérence :** Vérification automatisée que chaque "Check-list" est rattachée à un matricule opérateur valide.
3. **Export de données :** Préparation des jeux de données au format CSV/JSON pour l'importation directe dans SharePoint/Dataverse.