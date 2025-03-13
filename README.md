# 🕵️‍♂️ Scraping des taux de change - Git, Linux & Python

 

## 📌 Objectif du projet

 

Ce projet a pour objectif de **scraper en temps réel les taux de change des principales paires de devises**

(`EUR/USD`, `GBP/USD`, `USD/JPY`, etc.) à partir d'une source web fiable. 

Les données récupérées sont stockées et affichées sur un **dashboard interactif** développé en **Python (Dash)**.

 

### 🔍 **Pourquoi ce projet ?**

Le marché des devises est l'un des plus volatils et réactifs. L'objectif ici est de :

- **Analyser les fluctuations des devises majeures**.

- **Mettre en place un outil de suivi des variations** de change.

- **Calculer des statistiques financières** pour comprendre l'évolution des cours.

 

Les taux de change sont extraits d'un site offrant des mises à jour fréquentes (toutes les minutes), garantissant des **données dynamiques et exploitables**.

 

---

 

## 🚀 Fonctionnalités

 

- **📡 Scraper Bash** : Récupère les taux de change en direct avec `curl` et `grep` (sans librairie avancée).

- **📊 Dashboard Python (Dash)** : Affichage des taux sous forme de courbes et d'indicateurs financiers.

- **📄 Génération de rapports** :

  - Calcul des **statistiques journalières** (volatilité, cours d'ouverture/fermeture).

  - Stockage des données pour analyse historique.

- **🔄 Mise à jour automatique** :

  - **Toutes les 5 minutes** via `cron` pour récupérer les nouveaux taux.

  - **À 20h chaque jour**, génération d’un **rapport synthétique**.

 

---

 

## 📂 Structure du projet

 

/scraping_dir │── /dashboard # Interface web du projet (Python Dash) │ ├── app.py # Code principal du dashboard │ ├── logs.txt # Journal des erreurs et mises à jour │── /data # Données scrappées stockées localement │ ├── exchange_rates.csv # Historique des taux de change │── /reports # Rapports quotidiens générés automatiquement │ ├── report_YYYY-MM-DD.txt # Rapports détaillés des variations │── /scripts # Scripts pour l'analyse des données │ ├── generate_report.py # Script Python pour générer les rapports │── extract_rates.sh # Script Bash pour récupérer les taux de change │── rates.html # Page HTML brute scrappée │── README.md # Documentation du projet │── .gitignore # Liste des fichiers à exclure du repo

 

 

---

 

## 🛠️ Technologies Utilisées

 

- **Bash** (`curl`, `grep`, `sed`, `awk`) → Scraping des données.

- **Python** (`Dash`, `Pandas`, `Plotly`) → Visualisation des taux de change.

- **Git & GitHub** → Versionnement et collaboration.

- **Linux** (`cron jobs`, `shell scripting`) → Automatisation des tâches.

 

---

 

## 🔧 Installation et Exécution

 

### **1️⃣ Cloner le repo**

```bash

git clone git@github.com:antoinechdc31/Python_Git_Linux.git

cd Python_Git_Linux
