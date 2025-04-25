fragen_liste = [
    {
        "frage": "Hat der Porsche einen Heckspoiler?",
        "typ": "ja_nein",
        "antworten": ["Ja", "Nein"]
    }, 
    {
        "frage": "Wie viel Türen hat der Porsche?",
        "typ": "multiple_choice",
        "antworten": ["2 Türen", "4 Türen"]
    },
     {
        "frage": "Ist der Porsche ein coupé?",
        "typ": "ja_nein",
        "antworten": ["Ja", "Nein"]
    },
    {
        "frage": "Ist der Porsche ein SUV?",
        "typ": "ja_nein",
        "antworten": ["Ja", "Nein"]
    },
    {
        "frage": "Ist der Porsche eine Limousine?",
        "typ": "ja_nein",
        "antworten": ["Ja", "Nein"]
    },
    {
        "frage": "Welche Art von Heckspoiler hat der Porsche",
        "typ": "multiple_choice",
        "antworten": ["feststehender Rennspoler", "Entenbürzel-Spoiler", "Ausfahrbarer Spoiler", "Heckspoilerlippe", "keine der genannten"]
    },
    {
        "frage": "Ist der Porsche Turbo aufgeladen",
        "typ": "ja_nein",
        "antworten": ["Ja", "Nein"]
    }
]
  
antworten_benutzer = {}

for frage in fragen_liste:

    print(frage["frage"])
    
    if frage["typ"] == "ja_nein":
        eingabe = input("Antwort (Ja oder Nein):")

        eingabe.strip()
        eingabe.capitalize()

        antworten_benutzer[frage["frage"]] = eingabe

    elif frage["typ"] == "multiple_choice":
        for index in range(len(frage["antworten"])):
            antwort_text =  frage["antworten"][index]
            print(str(index + 1) + ". " + antwort_text)

        auswahl = input("Bitte gib die Zahl deiner Antwort ein: ")

        ausgewaehlt_antwort = frage["antworten"][int(auswahl) -1]
        antworten_benutzer[frage["frage"]] = ausgewaehlt_antwort


print("Antworten")
for frage_text in antworten_benutzer:
    antwort_text = antworten_benutzer[frage_text]
    print(frage_text + " " + antwort_text)