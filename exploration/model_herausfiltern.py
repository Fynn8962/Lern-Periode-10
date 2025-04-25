
porsche_daten = [
    {
        "modell": "Porsche 911 Carrera",
        "heckspoiler": "Ja",
        "tueren": "2",
        "coupé": "Ja",
        "suv": "Nein",
        "limousine": "Nein",
        "spoiler_art": "Feststehender Rennspoiler",
        "turbo_aufgeladen": "Nein",
        "motorisierung": "Sechszylinder Boxer",
        "baujahr": 2021,
        "leistung": "379 PS",
        "preis": "100.000 EUR"
    },
    {
        "modell": "Porsche 911 Turbo S",
        "heckspoiler": "Ja",
        "tueren": "2",
        "coupé": "Ja",
        "suv": "Nein",
        "limousine": "Nein",
        "spoiler_art": "Ausfahrbarer Spoiler",
        "turbo_aufgeladen": "Ja",
        "motorisierung": "Sechszylinder Boxer Turbo",
        "baujahr": 2022,
        "leistung": "650 PS",
        "preis": "200.000 EUR"
    },
    {
        "modell": "Porsche Cayenne",
        "heckspoiler": "Ja",
        "tueren": "4",
        "coupé": "Nein",
        "suv": "Ja",
        "limousine": "Nein",
        "spoiler_art": "Heckspoilerlippe",
        "turbo_aufgeladen": "Ja",
        "motorisierung": "V6 Turbo",
        "baujahr": 2023,
        "leistung": "335 PS",
        "preis": "85.000 EUR"
    },
    {
        "modell": "Porsche Taycan",
        "heckspoiler": "Ja",
        "tueren": "4",
        "coupé": "Nein",
        "suv": "Nein",
        "limousine": "Ja",
        "spoiler_art": "Heckspoilerlippe",
        "turbo_aufgeladen": "Nein",
        "motorisierung": "Elektrisch",
        "baujahr": 2023,
        "leistung": "616 PS",
        "preis": "90.000 EUR"
    },
    {
        "modell": "Porsche Panamera",
        "heckspoiler": "Ja",
        "tueren": "4",
        "coupé": "Nein",
        "suv": "Nein",
        "limousine": "Ja",
        "spoiler_art": "Ausfahrbarer Spoiler",
        "turbo_aufgeladen": "Ja",
        "motorisierung": "V6 Turbo",
        "baujahr": 2021,
        "leistung": "440 PS",
        "preis": "115.000 EUR"
    },
    {
        "modell": "Porsche Macan",
        "heckspoiler": "Ja",
        "tueren": "4",
        "coupé": "Nein",
        "suv": "Ja",
        "limousine": "Nein",
        "spoiler_art": "Heckspoilerlippe",
        "turbo_aufgeladen": "Ja",
        "motorisierung": "V4 Turbo",
        "baujahr": 2020,
        "leistung": "252 PS",
        "preis": "55.000 EUR"
    },
    {
        "modell": "Porsche 718 Cayman",
        "heckspoiler": "Nein",
        "tueren": "2",
        "coupé": "Ja",
        "suv": "Nein",
        "limousine": "Nein",
        "spoiler_art": "Keine der genannten",
        "turbo_aufgeladen": "Ja",
        "motorisierung": "V4 Turbo",
        "baujahr": 2021,
        "leistung": "300 PS",
        "preis": "60.000 EUR"
    },
    {
        "modell": "Porsche 718 Cayman GOLD",
        "heckspoiler": "Nein",
        "tueren": "2",
        "coupé": "Ja",
        "suv": "Nein",
        "limousine": "Nein",
        "spoiler_art": "Keine der genannten",
        "turbo_aufgeladen": "Ja",
        "motorisierung": "V4 Turbo",
        "baujahr": 2021,
        "leistung": "300 PS",
        "preis": "200.000 EUR"
    }
]

def filter_porsche_modelle(merkmal):
    """
    Funktion zum Filtern der Porsche-Modelle basierend auf den gesammelten Merkmalen.
    """
    gefilterte_modelle = []

    for porsche in porsche_daten:

        treffer = True
        for merkmal_name, merkmal_wert in merkmal.items():
            if porsche[merkmal_name] != merkmal_wert:
                treffer = False
                break

        if treffer:
            gefilterte_modelle.append(porsche["modell"])
    
    return gefilterte_modelle




# Beispiel gefilterte Merkmale anhand den Fragen: 
gesammelte_merkmale = {
    "heckspoiler": "Nein",
    "tueren": "2",
    "coupé": "Ja",
    "suv": "Nein",
    "limousine": "Nein",
    "turbo_aufgeladen": "Ja",
    "motorisierung": "V4 Turbo",
    "preis": "200.000 EUR"
}

gefilterte_modelle = filter_porsche_modelle(gesammelte_merkmale)

print("Mögliche Modelle:", gefilterte_modelle)
