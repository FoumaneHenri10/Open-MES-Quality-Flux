-- Phase 2 : Modélisation de la base de données pour l'outil Power Platform

-- 1. Référentiel des Postes de Travail (Localisation usine)
CREATE TABLE postes_travail (
    poste_id SERIAL PRIMARY KEY,
    code_poste VARCHAR(20) UNIQUE NOT NULL, -- ex: VAL-GMP-L1
    nom_zone VARCHAR(100), -- ex: Atelier Montage Boîtes
    responsable_zone VARCHAR(100)
);

-- 2. Référentiel des Check-lists par Métier
CREATE TABLE templates_checklist (
    template_id SERIAL PRIMARY KEY,
    nom_metier VARCHAR(100) NOT NULL, -- ex: Industrialisation GMP
    version_outil VARCHAR(10) DEFAULT 'V1.0',
    description_processus TEXT
);

-- 3. Table de suivi de l'avancement (La "Complexité" demandée)
CREATE TABLE suivi_implementation (
    suivi_id SERIAL PRIMARY KEY,
    poste_id INT REFERENCES postes_travail(poste_id),
    template_id INT REFERENCES templates_checklist(template_id),
    date_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    statut_avancement VARCHAR(50) CHECK (statut_avancement IN ('Initialisé', 'En cours', 'Validé', 'Bloqué')),
    score_conformite DECIMAL(5,2), -- Calculé par l'outil
    matricule_technicien VARCHAR(20) NOT NULL -- Pour la traçabilité
);