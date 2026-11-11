from flask import Flask, render_template, request
import os

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
        "explanation": "👶 <b>Versione Bambino:</b> Il SI è il 'linguaggio comune' degli scienziati di tutto il mondo. Ci sono 4 'mattoncini' di base (grandezze fondamentali) e tutte le altre (derivate) sono costruite con questi.<br><br>🎓 <b>Versione Liceo:</b> Il SI si basa su 4 grandezze fondamentali indipendenti: Lunghezza (m), Massa (kg), Tempo (s), Temperatura (K). Le grandezze derivate si ottengono moltiplicando o dividendo quelle fondamentali.<br><br>📏 <i>Esempi Derivate:</i> Area (m²), Volume (m³), Velocità (m/s), Forza (Newton).",
        "question": "Quante sono le grandezze fondamentali nel Sistema Internazionale?",
        "options": ["3", "7", "10", "100"],
        "answer": "7"
    },
    
    "multipli_parte1": {
        "title": "3. Multipli, Sottomultipli e Notazione Scientifica",
        "explanation": "👶 <b>Versione Bambino:</b> A volte i numeri sono troppo grandi o piccoli, quindi usiamo prefissi 'magici' (kilo = x1000, milli = ÷1000). La notazione scientifica è un trucco per scrivere numeri enormi usando le potenze del 10 (es. 3000 = 3 × 10³).<br><br>🎓 <b>Versione Liceo:</b> I prefissi SI permettono di esprimere multipli e sottomultipli tramite potenze di 10. La notazione scientifica esprime un numero nella forma a × 10ⁿ (con 1 ≤ |a| < 10). L'ordine di grandezza è la potenza di 10 più vicina al valore.<br><br>💼 <i>Esempio Economico:</i> Il debito pubblico italiano si esprime in notazione scientifica (es. 2,9 × 10¹² €) per renderlo leggibile.",
        "question": "Clicca Prosegui per vedere la tabella",
        "options": ["Prosegui"],
        "answer": "Prosegui",
        "next_topic": "multipli_parte2" 
    },
    
    "multipli_parte2": {
        "title": "3b. La Tabella dei Prefissi",
        "hidden": True,
        "explanation": "<b>Ecco la tabella completa dei prefissi SI:</b><br><br><table style='width:100%; border-collapse: collapse; margin-top: 15px; color: white;'> <tr style='border-bottom: 2px solid #ff69b4;'><th style='padding: 8px; text-align: left;'>Prefisso</th><th style='padding: 8px; text-align: left;'>Simbolo</th><th style='padding: 8px; text-align: left;'>Fattore</th></tr> <tr style='border-bottom: 1px solid rgba(255,255,255,0.2);'><td style='padding: 8px;'>giga</td><td style='padding: 8px;'>G</td><td style='padding: 8px;'>10⁹</td></tr> <tr style='border-bottom: 1px solid rgba(255,255,255,0.2);'><td style='padding: 8px;'>mega</td><td style='padding: 8px;'>M</td><td style='padding: 8px;'>10⁶</td></tr> <tr style='border-bottom: 1px solid rgba(255,255,255,0.2);'><td style='padding: 8px;'>kilo</td><td style='padding: 8px;'>k</td><td style='padding: 8px;'>10³</td></tr> <tr style='border-bottom: 1px solid rgba(255,255,255,0.2);'><td style='padding: 8px;'>etto</td><td style='padding: 8px;'>h</td><td style='padding: 8px;'>10²</td></tr> <tr style='border-bottom: 1px solid rgba(255,255,255,0.2);'><td style='padding: 8px;'>deca</td><td style='padding: 8px;'>da</td><td style='padding: 8px;'>10¹</td></tr> <tr style='border-bottom: 1px solid rgba(255,255,255,0.2);'><td style='padding: 8px;'>deci</td><td style='padding: 8px;'>d</td><td style='padding: 8px;'>10⁻¹</td></tr> <tr style='border-bottom: 1px solid rgba(255,255,255,0.2);'><td style='padding: 8px;'>centi</td><td style='padding: 8px;'>c</td><td style='padding: 8px;'>10⁻²</td></tr> <tr style='border-bottom: 1px solid rgba(255,255,255,0.2);'><td style='padding: 8px;'>milli</td><td style='padding: 8px;'>m</td><td style='padding: 8px;'>10⁻³</td></tr> <tr style='border-bottom: 1px solid rgba(255,255,255,0.2);'><td style='padding: 8px;'>micro</td><td style='padding: 8px;'>µ</td><td style='padding: 8px;'>10⁻⁶</td></tr> <tr style='border-bottom: 1px solid rgba(255,255,255,0.2);'><td style='padding: 8px;'>nano</td><td style='padding: 8px;'>n</td><td style='padding: 8px;'>10⁻⁹</td></tr> </table><br><br><b>Ora che hai visto la tabella, mettiti alla prova con il quiz!</b>",
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
        "explanation": "👶 <b>Versione Bambino:</b> Sono le 7 cose base che possiamo misurare. <br>1. Lunghezza (quanto è lungo). <br>2. Massa (quanta 'roba' c'è dentro). <br>3. Tempo (quanto dura). <br>4. Temperatura (quanto è caldo/freddo). <br>5. Corrente elettrica (quanta elettricità scorre). <br>6. Quantità di sostanza (quanti 'pezzettini' ci sono). <br>7. Intensità luminosa (quanto è forte una luce).<br><br>🎓 <b>Versione Liceo:</b> Ognuna ha un simbolo e un'unità SI: Lunghezza (l, m), Massa (m, kg), Tempo (t, s), Temperatura (T, K), Corrente (I, A), Quantità di sostanza (n, mol), Intensità luminosa (Iv, cd).<br><br>💡 <i>Nota:</i> La Massa (kg) non è il Peso! La massa è la quantità di materia, il peso è una forza (si misura in Newton).",
        "question": "Qual è la differenza tra Massa e Peso?",
        "options": ["Sono la stessa identica cosa", "La massa si misura in kg, il peso è una forza e si misura in Newton", "La massa si misura in metri, il peso in kg", "Il peso è la quantità di materia"],
        "answer": "La massa si misura in kg, il peso è una forza e si misura in Newton"
    },

    "grandezze_derivate": {
        "title": "6. Le Grandezze Derivate (Spiegate)",
        "explanation": "👶 <b>Versione Bambino:</b> Sono grandezze che si costruiscono combinando insieme quelle fondamentali. <br>• Area (superficie) <br>• Volume (spazio occupato) <br>• Velocità (rapidità di spostamento) <br>• Forza (spingere un carrello) <br>• Densità (quanto è compatto, es. ferro vs cotone) <br>• Pressione (forza su una superficie)<br><br>🎓 <b>Versione Liceo:</b> Derivano da prodotti/rapporti di grandezze fondamentali. <br>Area (m²), Volume (m³), Velocità (m/s), Accelerazione (m/s²), Forza (N = kg·m/s²), Peso (N), Densità (kg/m³), Pressione (Pa), Lavoro/Energia (J), Potenza (W).<br><br>💼 <i>Esempio Economico:</i> La densità abitativa (abitanti/km²) è una densità. Il PIL pro capite è un rapporto tra grandezze. La fisica fornisce il linguaggio della misura usato anche in economia!",
        "question": "La velocità (m/s) è una grandezza...",
        "options": ["Fondamentale", "Derivata", "Economica", "Immaginaria"],
        "answer": "Derivata"
    },

    "misura_parte1": {
        "title": "7. Strumenti e Tipi di Misura",
        "explanation": "👶 <b>1. Strumenti:</b> Alcuni hanno la lancetta (analogici), altri i numeri (digitali). Tutti e due misurano!<br>🎓 <i>Liceo:</i> Analogici usano scala graduata (errore di lettura); digitali usano display (errore di quantizzazione).<br><br>👶 <b>2. Portata:</b> È il valore massimo. Se la bilancia arriva a 100 kg, non pesi un camion!<br>🎓 <i>Liceo:</i> Fondo scala, il massimo misurabile senza danni.<br><br>👶 <b>3. Sensibilità:</b> Quanto piccolo è il salto che vede. Se segna solo i kg, non vede 100 g.<br>🎓 <i>Liceo:</i> Minima variazione distinguibile (risoluzione).<br><br>👶 <b>4. Prontezza:</b> Quanto in fretta risponde.<br>🎓 <i>Liceo:</i> Tempo di risposta per una lettura stabile.<br><br>👶 <b>5. Misure indirette:</b> Misuri i lati del tavolo e li moltiplichi per l'area.<br>🎓 <i>Liceo:</i> Calcolo tramite relazione matematica (es. v = s/t). L'incertezza si propaga.",
        "question": "Clicca Prosegui per gli Errori di Misura",
        "options": ["Prosegui"],
        "answer": "Prosegui",
        "next_topic": "misura_parte2"
    },

    "misura_parte2": {
        "title": "8. Gli Errori di Misura",
        "explanation": "👶 <b>1. Errori:</b> Nessuna misura è perfetta, c'è sempre uno 'sbaglietto'.<br>🎓 <i>Liceo:</i> Si dividono in sistematici e casuali.<br><br>👶 <b>1.1. Sistematici:</b> Sbagliano sempre dalla stessa parte (bilancia +1kg).<br>🎓 <i>Liceo:</i> Spostano tutte le misure nella stessa direzione. Non si riducono ripetendo; si tara lo strumento.<br><br>👶 <b>1.2. Casuali:</b> Cambiano ogni volta (come lanciare i dadi).<br>🎓 <i>Liceo:</i> Oscillano attorno al valore vero. Si riducono con la media di più misure.<br><br>👶 <b>2. Incertezza:</b> È il 'più o meno' (10 cm ± 1 cm).<br>🎓 <i>Liceo:</i> Indica l'intervallo di fiducia. Per una misura singola è metà della sensibilità (analogico) o l'ultima cifra (digitale). Con più misure si usa la deviazione standard.<br><br>👶 <b>3. Precisione vs Accuratezza:</b> Precisione = frecce vicine tra loro. Accuratezza = frecce vicine al centro.<br>🎓 <i>Liceo:</i> Precisione = dispersione (errori casuali). Accuratezza = vicinanza al vero (errori sistematici).",
        "question": "Clicca Prosegui per Calcoli e Incertezze",
        "options": ["Prosegui"],
        "answer": "Prosegui",
        "next_topic": "misura_parte3"
    },

    "misura_parte3": {
        "title": "9. Calcoli, Incertezze e Cifre Significative",
        "explanation": "👶 <b>1. Incertezza relativa:</b> Quanto è grande lo sbaglietto rispetto alla misura (1 cm su 100 è poco, su 2 è tanto!).<br>🎓 <i>Liceo:</i> Δx/x₀ (adimensionale) o in percentuale. Serve a confrontare misure diverse.<br><br>👶 <b>2. Incertezza statica:</b> Dipende da quanto è 'bravo' lo strumento.<br>🎓 <i>Liceo:</i> Incertezza intrinseca dello strumento (tolleranze di fabbrica).<br><br>👶 <b>3. Misure indirette:</b> Se calcoli l'area, gli sbaglietti dei lati si sommano.<br>🎓 <i>Liceo:</i> Propagazione degli errori. Somme: si sommano le incertezze assolute. Prodotti: si sommano quelle relative. Potenze: si moltiplica per l'esponente.<br><br>👶 <b>4. Cifre significative:</b> Non inventarti numeri più precisi di quelli che hai misurato!<br>🎓 <i>Liceo:</i> Somme: stesso numero di decimali. Moltiplicazioni: stesso numero di cifre significative. Zeri iniziali non contano (0,0032 = 2 cifre).",
        "question": "Se devi sommare due misure, come gestisci le cifre decimali nel risultato?",
        "options": ["Metto tutti i decimali della calcolatrice", "Uso lo stesso numero di decimali della misura che ne ha meno", "Uso lo stesso numero di cifre significative", "Arrotondo sempre all'intero"],
        "answer": "Uso lo stesso numero di decimali della misura che ne ha meno"
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
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
