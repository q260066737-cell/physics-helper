from flask import Flask, render_template, request

app = Flask(__name__)

TOPICS = {
    "leggi_e_grandezze": {
        "title": "1. Leggi e Grandezze Fisiche",
        "explanation": "👶 <b>Versione Bambino:</b> Una legge fisica è una 'regola del gioco' che la natura segue sempre (es. se lasci andare una palla, cade giù). Una grandezza fisica è una cosa che si può misurare con un numero (altezza, peso, tempo). 'Bello' non si misura, quindi non è una grandezza!<br><br>🎓 <b>Versione Liceo:</b> Una legge fisica è un enunciato che descrive una regolarità della natura in forma sintetica e verificabile (spesso tramite formule come F = ma). Una grandezza fisica è una proprietà misurabile definibile in modo operativo; il risultato di una misura è sempre una coppia: valore numerico + unità di misura.<br><br>💼 <i>Esempio Economico:</i> La legge della domanda e dell'offerta è un modello che descrive regolarità e permette previsioni, proprio come una legge fisica!",
        "question": "Quale di queste affermazioni è vera?",
        "options": ["Una grandezza fisica si può misurare con un numero e un'unità di misura", "La bellezza è una grandezza fisica", "Le leggi fisiche sono inventate dagli scienziati per divertirsi", "Una grandezza fisica è solo un numero"],
        "answer": "Una grandezza fisica si può misurare con un numero e un'unità di misura"
    },
    
    "sistema_si": {
        "title": "2. Il Sistema Internazionale (SI)",
        "explanation": "👶 <b>Versione Bambino:</b> Il SI è il 'linguaggio comune' degli scienziati di tutto il mondo. Ci sono 7 'mattoncini' di base (grandezze fondamentali) e tutte le altre (derivate) sono costruite con questi.<br><br>🎓 <b>Versione Liceo:</b> Il SI si basa su 7 grandezze fondamentali indipendenti: Lunghezza (m), Massa (kg), Tempo (s), Temperatura (K), Corrente elettrica (A), Quantità di sostanza (mol), Intensità luminosa (cd). Le grandezze derivate si ottengono moltiplicando o dividendo quelle fondamentali.<br><br>📏 <i>Esempi Derivate:</i> Area (m²), Volume (m³), Velocità (m/s), Forza (Newton).",
        "question": "Quante sono le grandezze fondamentali nel Sistema Internazionale?",
        "options": ["3", "7", "10", "100"],
        "answer": "7"
    },
    
    "multipli_e_notazione": {
        "title": "3. Multipli, Sottomultipli e Notazione Scientifica",
        "explanation": "👶 <b>Versione Bambino:</b> A volte i numeri sono troppo grandi o piccoli, quindi usiamo prefissi 'magici' (kilo = x1000, milli = ÷1000). La notazione scientifica è un trucco per scrivere numeri enormi usando le potenze del 10 (es. 3000 = 3 × 10³).<br><br>🎓 <b>Versione Liceo:</b> I prefissi SI permettono di esprimere multipli e sottomultipli tramite potenze di 10. La notazione scientifica esprime un numero nella forma a × 10ⁿ (con 1 ≤ |a| < 10). L'ordine di grandezza è la potenza di 10 più vicina al valore.<br><br>💼 <i>Esempio Economico:</i> Il debito pubblico italiano si esprime in notazione scientifica (es. 2,9 × 10¹² €) per renderlo leggibile.",
        "question": "Come si scrive 5000 in notazione scientifica?",
        "options": ["5 × 10³", "50 × 10²", "5 × 10²", "0,5 × 10⁴"],
        "answer": "5 × 10³"
    },
    
    "equivalenze_liceo": {
        "title": "4. Le Equivalenze",
        "explanation": "👶 <b>Versione Bambino:</b> Cambiare unità di misura senza cambiare la quantità. 1 metro = 100 centimetri: è sempre la stessa lunghezza!<br><br>🎓 <b>Versione Liceo:</b> Un'equivalenza è una conversione tra unità omogenee che conserva il valore della grandezza. Si opera moltiplicando per un fattore di conversione unitario.<br><br>📐 <i>Esempio:</i> 2,5 m = 2,5 × 10² cm = 250 cm.<br><br>💼 <i>Esempio Economico:</i> Convertire euro in dollari è un'equivalenza: cambia l'unità, non il valore reale (a parità di cambio).",
        "question": "Quanti metri ci sono in 350 centimetri?",
        "options": ["3,5 m", "35 m", "0,35 m", "3500 m"],
        "answer": "3,5 m"
    },

    "grandezze_fondamentali": {
        "title": "5. Le Grandezze Fondamentali (Spiegate)",
        "explanation": "👶 <b>Versione Bambino:</b> Sono le 7 cose base che possiamo misurare. <br>1. Lunghezza (quanto è lungo). <br>2. Massa (quanta 'roba' c'è dentro). <br>3. Tempo (quanto dura). <br>4. Temperatura (quanto è caldo/freddo). <br><br>🎓 <b>Versione Liceo:</b> Ognuna ha un simbolo e un'unità SI: Lunghezza (l, m), Massa (m, kg), Tempo (t, s), Temperatura (T, K).<br><br>💡 <i>Nota:</i> La Massa (kg) non è il Peso! La massa è la quantità di materia, il peso è una forza (si misura in Newton).",
        "question": "Qual è la differenza tra Massa e Peso?",
        "options": ["Sono la stessa identica cosa", "La massa si misura in kg, il peso è una forza e si misura in Newton", "La massa si misura in metri, il peso in kg", "Il peso è la quantità di materia"],
        "answer": "La massa si misura in kg, il peso è una forza e si misura in Newton"
    },

    "grandezze_derivate": {
        "title": "6. Le Grandezze Derivate (Spiegate)",
        "explanation": "👶 <b>Versione Bambino:</b> Sono grandezze che si costruiscono combinando insieme quelle fondamentali. <br>• Area (superficie) <br>• Volume (spazio occupato) <br>• Velocità (rapidità di spostamento) <br>• Forza (spingere un carrello) <br>• Densità (quanto è compatto, es. ferro vs cotone) <br><br>🎓 <b>Versione Liceo:</b> Derivano da prodotti/rapporti di grandezze fondamentali. <br>Area (m²), Volume (m³), Velocità (m/s), Forza (N = kg·m/s²), Accelerazione (m/s²).<br><br>💼 <i>Esempio Economico:</i> La densità abitativa (abitanti/km²) è una densità. Il PIL pro capite è un rapporto tra grandezze. La fisica fornisce il linguaggio della misura usato anche in economia!",
        "question": "La velocità (m/s) è una grandezza...",
        "options": ["Fondamentale", "Derivata", "Economica", "Immaginaria"],
        "answer": "Derivata"
    }
}

@app.route("/")
def home():
    return render_template("index.html", topics=TOPICS)

@app.route("/topic/<topic_id>")
def topic(topic_id):
    topic_data = TOPICS.get(topic_id)
    if not topic_data:
        return "Argomento non trovato", 404
    return render_template("topic.html", topic=topic_data, topic_id=topic_id)

@app.route("/check", methods=["POST"])
def check():
    topic_id = request.form["topic_id"]
    chosen = request.form["answer"]
    topic_data = TOPICS[topic_id]
    correct = (chosen == topic_data["answer"])
    return render_template("result.html", correct=correct, chosen=chosen, topic=topic_data, topic_id=topic_id)

if __name__ == "__main__":
    import os
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)