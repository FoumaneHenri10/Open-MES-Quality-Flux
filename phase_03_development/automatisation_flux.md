# Phase 3 : Logique d'Automatisation & Workflow

Pour répondre aux enjeux de réactivité du département Industrialisation, nous avons conçu un flux d'automatisation basé sur **Power Automate**.

### ⚡ Opportunité identifiée : Alerte de blocage temps réel
**Problème :** Lorsqu'une machine est "Bloquée" sur la ligne, le manager n'est informé que lors de la réunion du lendemain.
**Solution :** Automatisation du flux d'alerte.

### ⚙️ Description du Flux (Workflow)
1. **Déclencheur (Trigger) :** Modification du statut dans la table `suivi_implementation` (via l'App ou le script).
2. **Condition :** `SI Statut == 'Bloqué'`.
3. **Actions automatisées :**
    * Envoi d'une notification **Push** sur le mobile du Chef d'Atelier.
    * Création d'un ticket d'intervention automatique dans le planner de maintenance.
    * Mise à jour instantanée du dashboard **Power BI**.

### 📈 Bénéfice métier
* Réduction du temps de réaction (Lead Time) de **24h à moins de 5 minutes**.
* Suppression des erreurs de saisie manuelle entre le terrain et le reporting.

### 📊 Visualisation Power BI (Cible)
Le modèle de données permet de calculer automatiquement les indicateurs suivants :
* **Taux d'implémentation :** (Nombre de check-lists validées / Total prévu).
* **Analyse de Pareto :** Identification des 20% de causes générant 80% des blocages sur la ligne GMP.