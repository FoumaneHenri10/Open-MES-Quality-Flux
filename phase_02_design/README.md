# Phase 2 : Modélisation & Complexité de la Base de Données

Cette phase démontre l'aptitude à structurer des relations complexes entre les entités industrielles.

### 🏗 Architecture des Relations
Pour répondre au besoin, la base de données est structurée autour de 3 axes :
1. **L'Actif (Asset) :** Identification précise du poste de travail ou de la machine sur la ligne GMP.
2. **Le Référentiel (Check-list) :** Définition des points de contrôle métier (Maintenance, Qualité, Sécurité).
3. **L'Événement (Inspection) :** Lien temporel entre un opérateur, une machine et un résultat de contrôle.

### 🧩 Justification de la Complexité
Le modèle gère l'historisation des versions de check-lists et l'intégrité référentielle des matricules opérateurs. Cette structure est optimisée pour être connectée nativement à **Dataverse** ou **SharePoint**.

### 🔗 Intégration Power Platform
Cette structure SQL est conçue pour être portée sur **Microsoft Dataverse**. Les tables `postes_travail` et `templates_checklist` serviront de sources pour les menus déroulants de la **Power App**, garantissant l'intégrité des données dès la saisie terrain.