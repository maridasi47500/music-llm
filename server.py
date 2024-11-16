from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Bienvenue au serveur des Large Language Models pour les Performances et Capacités Musicales des Musiciens ! Découvrez comment ces modèles peuvent améliorer vos compétences et performances musicales."

# Route pour Musicien Globe-trotter
@app.route('/musicien_globe_trotter')
def musicien_globe_trotter():
    return jsonify({"musicien": "Musicien Globe-trotter", "description": "En tant que musicien globe-trotter, vous pouvez utiliser la musique pour explorer de nouvelles cultures, connecter des gens de différentes parties du monde, et inspirer des audiences variées avec vos voyages mélodieux."})

# Routes pour la Performance Musicale

@app.route('/llm/performance/generatif')
def llm_performance_generatif():
    return jsonify({"llm": "LLM Génératif en Performance Musicale", "description": "Les modèles de langage génératifs peuvent créer des compositions musicales autonomes et improviser des performances en direct, offrant de nouvelles possibilités pour les musiciens globe-trotters."})

@app.route('/llm/performance/traduction')
def llm_performance_traduction():
    return jsonify({"llm": "LLM de Traduction de Paroles en Performance", "description": "Les modèles de langage de traduction aident les musiciens globe-trotters à traduire leurs paroles et leurs performances dans différentes langues, facilitant la connexion avec des audiences internationales."})

@app.route('/llm/performance/qa')
def llm_performance_qa():
    return jsonify({"llm": "LLM de Réponse à des Questions pour Performances", "description": "Ces modèles aident les musiciens globe-trotters en répondant à leurs questions sur les meilleures pratiques de performance, les cultures locales et les conseils de voyage."})

@app.route('/llm/performance/analyse_de_sentiments')
def llm_performance_analyse_de_sentiments():
    return jsonify({"llm": "LLM d'Analyse de Sentiments sur Performances", "description": "Ces modèles analysent les réactions et les commentaires des fans sur les performances musicales, aidant les musiciens globe-trotters à comprendre l'impact émotionnel de leurs concerts."})

@app.route('/llm/performance/resume')
def llm_performance_resume():
    return jsonify({"llm": "LLM de Résumé de Journaux de Performances", "description": "Les modèles de résumé de texte peuvent condenser les journaux de performances et les blogs des musiciens globe-trotters en résumés courts et informatifs, idéaux pour partager leurs aventures et concerts avec leurs abonnés."})

# Routes pour les Compétences Musicales

@app.route('/llm/competence/composition')
def llm_composition():
    return jsonify({"llm": "LLM Génératif en Composition", "description": "Les modèles de langage génératifs peuvent aider les musiciens à composer des mélodies et des harmonies, offrant de nouvelles possibilités créatives pour leurs œuvres musicales."})

@app.route('/llm/competence/traduction')
def llm_traduction():
    return jsonify({"llm": "LLM de Traduction de Paroles", "description": "Les modèles de langage de traduction aident les musiciens à traduire leurs paroles de chansons dans différentes langues, facilitant la connexion avec des audiences internationales."})

@app.route('/llm/competence/qa')
def llm_qa():
    return jsonify({"llm": "LLM de Réponse à des Questions sur la Théorie Musicale", "description": "Ces modèles aident les musiciens en répondant à leurs questions sur la théorie musicale, les techniques de composition et les pratiques de performance."})

@app.route('/llm/competence/analyse_de_sentiments')
def llm_analyse_de_sentiments():
    return jsonify({"llm": "LLM d'Analyse de Sentiments sur les Paroles", "description": "Ces modèles analysent les réactions et les commentaires des fans sur les paroles des chansons, aidant les musiciens à comprendre l'impact émotionnel de leurs œuvres."})

@app.route('/llm/competence/resume')
def llm_resume():
    return jsonify({"llm": "LLM de Résumé de Livres de Musique", "description": "Les modèles de résumé de texte peuvent condenser des livres et des articles sur la musique en résumés courts et informatifs, idéaux pour aider les musiciens à apprendre rapidement de nouvelles connaissances."})

# Routes pour les Capacités Musicales des Musiciens

@app.route('/llm/musicien/composition')
def llm_musicien_composition():
    return jsonify({"llm": "LLM pour Composition Musicale", "description": "Les modèles de langage peuvent aider les musiciens à composer des mélodies et des harmonies, en offrant des suggestions et des variations pour enrichir leurs œuvres musicales."})

@app.route('/llm/musicien/traduction')
def llm_musicien_traduction():
    return jsonify({"llm": "LLM pour Traduction de Paroles", "description": "Les modèles de langage peuvent aider les musiciens à traduire leurs paroles de chansons dans différentes langues, facilitant ainsi la connexion avec des audiences internationales."})

@app.route('/llm/musicien/technique')
def llm_musicien_technique():
    return jsonify({"llm": "LLM pour Amélioration Technique", "description": "Les modèles de langage peuvent fournir des conseils personnalisés et des exercices pratiques pour améliorer la technique instrumentale et vocale des musiciens."})

@app.route('/llm/musicien/education')
def llm_musicien_education():
    return jsonify({"llm": "LLM pour Éducation Musicale", "description": "Les modèles de langage peuvent enseigner la théorie musicale, l'histoire de la musique et les techniques de composition, offrant une formation complète aux musiciens."})

@app.route('/llm/musicien/recommendation')
def llm_musicien_recommendation():
    return jsonify({"llm": "LLM pour Recommandation Musicale", "description": "Les modèles de langage peuvent recommander des morceaux et des styles de musique à explorer, aidant les musiciens à découvrir de nouvelles inspirations et à élargir leur répertoire."})

@app.route('/llm/musicien/analyse')
def llm_musicien_analyse():
    return jsonify({"llm": "LLM pour Analyse de Performances", "description": "Les modèles de langage peuvent analyser les enregistrements de performances musicales et fournir des commentaires constructifs pour aider les musiciens à s'améliorer."})

if __name__ == '__main__':
    app.run(debug=True)
