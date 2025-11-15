# 📌 Flask + Redis — Gestion d'utilisateurs et de sessions

Ce dépôt contient un projet simple illustrant l'utilisation de **Redis** comme base de données clé-valeur pour stocker :
- des **utilisateurs** (nom, prénom, id auto-incrémenté)
- des **sessions utilisateurs** (session_id, user_id, informations diverses)

L'application expose une **API REST en Python (Flask)** permettant de créer, lire, supprimer et lister les utilisateurs, ainsi que d'enregistrer et récupérer des sessions.

Ce projet a été réalisé dans le cadre d'un **TP pédagogique sur Redis**.

---

## 🚀 Fonctionnalités

### **Gestion des utilisateurs**
- Génération automatique d'un ID (`INCR` Redis)
- Création d'un utilisateur (POST)
- Récupération d'un utilisateur (GET)
- Suppression d'un utilisateur (DELETE)
- Liste de tous les utilisateurs (GET)

### **Gestion des sessions**
- Création d'une session avec expiration (`SETEX`)
- Récupération d'une session

---

## 📦 Technologies utilisées

- **Python 3**
- **Flask**
- **Redis**
- **redis-py**
- **JSON**

---

## 📥 Installation

### 1️⃣ Cloner le projet
```bash
git clone https://github.com/lakshwini/Redis-Flask.git
cd Redis-Flask
```

### 2️⃣ Installer les dépendances
```bash
pip install flask redis
```

### 3️⃣ Démarrer Redis

**Sur Linux / WSL :**
```bash
sudo systemctl start redis-server
```

**Sur macOS (Homebrew) :**
```bash
brew services start redis
```

---

## 🔧 Configuration

**Connexion à Redis :**
```python
r = redis.Redis(
    host='localhost',
    port=6379,
    db=0,
    password='*****'   # Remplacer par votre mot de passe Redis
)
```

---

## ▶️ Lancer le serveur Flask
```bash
python ServiceFlask.py
```

L'API sera disponible sur :  
👉 **http://127.0.0.1:5000**

---

## 📡 Endpoints API

### ➤ Créer un utilisateur
```bash
curl -X POST http://127.0.0.1:5000/create_user \
    -H "Content-Type: application/json" \
    -d '{"nom": "Doe", "prenom": "John"}'
```

### ➤ Récupérer un utilisateur
```bash
curl http://127.0.0.1:5000/get_user/1
```

### ➤ Supprimer un utilisateur
```bash
curl -X DELETE http://127.0.0.1:5000/delete_user/1
```

### ➤ Lister les utilisateurs
```bash
curl http://127.0.0.1:5000/list_users
```

---

## 🧩 Sessions

### ➤ Créer une session
```bash
curl -X POST http://127.0.0.1:5000/create_session \
    -H "Content-Type: application/json" \
    -d '{"session_id": "1929", "data": {"user_id": 1, "username": "Siva"}}'
```

### ➤ Récupérer une session
```bash
curl http://127.0.0.1:5000/get_session/1929
```

---

## 📚 Objectif pédagogique

Ce projet vise à comprendre :
- le fonctionnement d'une base clé-valeur en mémoire
- la persistance optionnelle des données Redis
- la création d'une API REST avec Flask
- la gestion de sessions via Redis (`SETEX`)
- les commandes Redis essentielles : `SET`, `GET`, `SETEX`, `INCR`, `DEL`, etc.

---

