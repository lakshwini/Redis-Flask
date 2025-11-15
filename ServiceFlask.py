from flask import Flask, request, jsonify
import redis
import json

# création de l'application Flask
app = Flask(__name__)

#connexion à Redis
r = redis.Redis(host='localhost', port=6379, db=0, password='sivayanama')

# FONCTION POUR GENERER UN NOUVEL ID UTILISATEUR UNIQUE

def generateUserId():
    return r.incr('user_id_counter')


# FONCTION POUR CREER UN UTILISATEUR AVEC NOM ET PRENOM
@app.route('/create_user', methods=['POST'])

def create_user():
    data = request.json
    
    # Vérification que les champs nom et prénom sont présents
    if not data.get('nom') or not data.get('prenom'):
        return jsonify({"error": "Les champs 'nom' et 'prenom' sont obligatoires"}), 400

    # Génération d'un nouvel ID utilisateur
    user_id = generateUserId()

    # Création des données utilisateur
    user_data = {
        'id': user_id,
        'nom': data['nom'],
        'prenom': data['prenom']
    }

    # Stockage des données dans Redis sous forme JSON
    r.set(f"user:{user_id}", json.dumps(user_data))

    # Retour de la réponse avec l'ID créé
    return jsonify({"message": "Utilisateur créé", "user_id": user_id}), 201

# FONCTION POUR RECUPERER UN UTILISATEUR PAR SON ID
@app.route('/get_user/<int:user_id>', methods=['GET'])

def get_user(user_id):
    # Récupération des données dans Redis
    user_data = r.get(f"user:{user_id}")

    # Vérification si l'utilisateur existe
    if not user_data:
        return jsonify({"error": "Utilisateur non trouvé"}), 404

    # Retour des données utilisateur en JSON
    return jsonify(json.loads(user_data)), 200

# FONCTION POUR SUPPRIMER UN UTILISATEUR PAR SON ID
@app.route('/delete_user/<int:user_id>', methods=['DELETE'])

def delete_user(user_id):
    # Suppression de l'utilisateur dans Redis
    result = r.delete(f"user:{user_id}")

    # Vérification si un utilisateur a bien été supprimé
    if result == 0:
        return jsonify({"error": "Utilisateur non trouvé"}), 404

    # Retour de la confirmation
    return jsonify({"message": "Utilisateur supprimé"}), 200

# FONCTION POUR LISTER TOUS LES UTILISATEURS
@app.route('/list_users', methods=['GET'])

def list_users():
    # Récupération de toutes les clés d'utilisateurs
    user_keys = r.keys('user:*')

    users = []
    for key in user_keys:
        user_data = r.get(key)
        if user_data:
            users.append(json.loads(user_data))

    # Retour de la liste des utilisateurs en JSON
    return jsonify(users), 200


# FONCTION POUR CREER UNE SESSION AVEC EXPIRATION
@app.route('/create_session', methods=['POST'])
def create_session():
    data = request.json

    if not data.get("session_id"):
        return jsonify({"error": "session_id manquant"}), 400

    session_data = data.get("data", {})

    # On stocke la session pendant 1h 
    r.setex(f"session:{data['session_id']}", 3600, json.dumps(session_data))

    return jsonify({"message": "Session enregistrée"}), 201

# FONCTION POUR LIRE UNE SESSION
@app.route('/get_session/<session_id>', methods=['GET'])
def get_session(session_id):
    session_data = r.get(f"session:{session_id}")

    if not session_data:
        return jsonify({"error": "Session introuvable ou expirée"}), 404

    return jsonify(json.loads(session_data)), 200




# Démarrage de l'application Flask
if __name__ == '__main__':
    app.run(debug=True)
    
    