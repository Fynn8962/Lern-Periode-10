# Lern-Periode-10
25.04 bis 27.06

&nbsp;

## Grob-Planung

**1. Welche Programmiersprache möchten Sie verwenden? Was denken Sie, wo Ihre Zeit und Übung am sinnvollsten ist?**               
       - Ich würde gerne mein wissen in Python mehr vertiefen, da ich die Möglichkeiten sehr spannend finde, vor allem in Bezug auf ML.
    
**2. Welche Datenbank-Technologie möchten Sie üben? Fühlen Sie sich sicher mit SQL und möchten etwas Neues ausprobieren; oder möchten Sie sich weiter mit SQL beschäftigen?**   
        - Da ich ein Projekt mit ML machen will, möchte ich eine neue Datenbank-Technologie verwenden wie z. B. MongoDB.
    
**3. Was wäre ein geeignetes Abschluss-Projekt?**                                         
        - Ein Projekt mittels Python in Bezug auf ML. Es soll eine Art 'Auto Akinator' sein. Das Modell hat einen Datensatz über Auto Modelle.
               Der Benutzer wird über Merkmale des Autos abgefragt, an den er denkt. Findet das System ein Auto, kann man eine Positive oder
              Negative Bewertung geben. Das System trainiert dadurch den Empfehlungs-Algorithmus.              

&nbsp;
 
## 25.04

Welche 3 *features* sind die wichtigsten Ihres Projektes? Wie können Sie die Machbarkeit dieser in jeweils 45' am einfachsten beweisen?

- [x] *make or break feature* 1:
      Fragesystem (mit GUI) zum Modell, mit JA/NEIN Möglichkeit oder Multiple Choice.                                 
      Umsetzung: Kleine Konsolen-Applikation mit ein paar Fragen, welche beantwortet werden können. Gesammelte Merkmale werden am Schluss ausgegeben.      
- [x] *make or break feature* 2: Anhand Antworten ein oder mehrere Modelle herausfiltern.                             
      Umsetzung: Ein einfaches Datenset mit 5-10 Auto Modellen und gewissen Merkmalen. Einen Filteralgorithmus, welcher nach 10 Fragen das passendste Modell ausgibt.
- [x] *make or break feature* 3: Das Datenset der Auto Modelle enthält einheitliche und brauchbare Informationen über jedes Modell.                            
      Umsetzung: Datenset finden und die Daten überprüfen auf ihre Konsistenz und Einheitlichkeit.

 &nbsp;

**Heute habe ich...**                
Zuerst habe ich die Grobplanung verfasst. Danach habe ich mir drei "make or break feature" überlegt, passend zu meinem Projekt. Das erste Feature, das ich angehen wollte, war das Multiple Choice Feature. Ich habe ganz simpel in einem Python File ein dictionary erstellt, in welchem Fragen und Antworten drinnen sind. Dann habe ich für jeden Fragetyp eine Abfrage und Antwortfunktion geschrieben. Am Schluss werden die gegebenen Antworten einfach nochmal ausgegeben.          
Als Nächstes ich mir ein Bild davon gemacht, wie der Datensatz aussehen könnte. Ich habe passend zu den Fragen, die ich am Anfang definiert habe Attribute in einem Dictionary verfasst und diese mit Werten passend zum Auto Modell versehrt. 
Als Letztes habe ich das Herausfiltern aus dem dictionary mithilfe gegebener Merkmale angeschaut. Ich habe mithilfe von KI die Filterfunktion erstellt, welche anhand von gegebenen Merkmalen ein Model aus dem Dictionary erkennt. Ich finde das Ergebnis nicht perfekt da es nicht viel Toleranz erlaubt aber für den Anfang zeigt es mir wie es gehen könnte.

(Vergessen Sie nicht, den Code von heute auf github hochzuladen. Ggf. bietet es sich an, für die Code-Schnipsel einen eigenen Ordner `exploration` zu erstellen.)

&nbsp;

&nbsp;

## 02.05

Ausgehend von Ihren Erfahrungen vom 25.04, welche *features* brauchen noch mehr Recherche? (Sie können auch mehrere AP für ein *feature* aufwenden.)

- [x] Attribute, die nützlich wären, um die Auto Modelle zu identifizieren (📵)
- [x] F2, passenen Modell finden, gewisse Modelle Testen auf Umsetzbarkeit
- [ ] F1 und F2, beim Filter was, wenn der Benutzer bei zwei Attributen z. B. "Ja" macht, wird das alte irgendwie überschrieben?
- [x] F3, wie erstelle ich den Datensatz mit wenig Aufwand und woher bekomme ich die Daten?
 
 &nbsp;

**Heute habe ich...**                  
Zuerst habe ich mir einen Datensatz ausgesucht, welcher eine gute Grundlage bildet, um mit dem Projekt anzufangen. Die Attribute darin entsprachen einigermassen meiner Vorstellungen. Diesen Datensatz kann ich später auch noch abändern. Anschliessend habe ich zusammen mit dem Datensatz ein Modell zum Testen trainiert. Dieses Modell habe ich noch ohne jegliche Benutzerinteraktion erstellt. Die Genauigkeit lag bei ca. 98,80 % was sehr gut ist. 

&nbsp;

&nbsp;

## 09.05

Planen Sie nun Ihr Projekt, sodass die *Kern-Funktionalität* in 3 Sitzungen realisiert ist. Schreiben Sie dazu zunächst 3 solche übergeordneten Kern-Funktionalitäten auf: 

1. Frage und Antwort Ablauf zwischen Benutzer und Programm
2. Filter Algorithmus (herausfinden des passenden Modells, fortlaufende Anpassung des Modells)
4. Datenbank mit Auto Modelldaten (Datensatz erstellen/generieren)

Diese Kern-Funktionalitäten brechen Sie nun in etwa 4 AP je herunter. Versuchen Sie jetzt bereits, auch die Sitzung vom 16.5 und 23.5 zu planen (im Wissen, dass Sie kleine Anpassungen an Ihrer Planung vornehmen können).

- [x] Mit Flask vertraut machen für das GUI
- [x] Mithilfe von Flask eine Web bassierte abfrage von Beispielfragen erstellen
- [x] Speichern der Antwroten des Benutzers
- [ ] Bewertung der Ausgabe ob richtig oder Falsch

&nbsp;

**Heute habe ich...**                                            
Ich habe mich zuerst mit Flask versucht vertraut zu machen und zu verstehen wie es funktioniert. Ich hatte Probleme, was das Grundkonstrukt war, also wie die Kommunikation zwischen Python und HTML funktioniert, doch durch ein Tutorial habe ich es Stück für Stück verstanden. Ich habe noch gewisse Testprojekte erstellt, um das gelernte direkt umzusetzen. Anschliessend habe ich angefangen mit meiner Umgebung, die ich brauche. Ich habe drei HTML Files erstellt und ein Python File. Das "fertige" Produkt funktioniert schon einigermassen, jedoch sieht es noch nicht schön.

&nbsp;

&nbsp;

## 16.05

- [x] Datensatz finden welcher grundsätzlich passende Features hat
- [x] Datensatz einlesen und sich mit diesem Vertraut machen (welche Werte sind wichtig etc.)
- [ ] Den Datensatz bearbeiten, vorbereiten um mit diesem Arbeiten zu können (ML)


&nbsp;

**Heute habe ich...**                          
 Ich habe nach einem passenden Auto Datensatz gesucht, welcher es möglich macht, Autos anhand simpler Kriterien zu definieren. Das Problem ist, die meisten Datensätze haben zu viele ähnliche Autos mit zu spezifischen Daten. Nicht jeder weis wie viel PS, Hubraum oder Nm das Auto hat oder welches Getriebe es hat. Schlussendlich war das Ergebnis für mich nicht gut genug und ich musste neu anfangen. Ich hatte die Idee, den Akinator mit Pokémon zu machen. Dies ist zwar sehr ähnlich zum echten Akinator, aber geht viel einfacher als mit Autos. Ich habe einen Pokémon Datensatz auf Kaggle gefunden, der sich perfekt für diese Idee eignen würde. Ich behalte dies jedoch nur im Hinterkopf und fahre vorerst mit einem nicht so passenden Auto Datensatz fort. 

&nbsp;

&nbsp;

## 23.05

- [x] Passt das gewählte Modell. Dieses Testen mit dem Datensatz
- [x] Modell in die restliche Umgebung integrieren
- [ ] Modell anpassen damit es gut Funktioniert
- [ ] Fortlaufende Anpassung des Models indem das Resultat vom Benutzer bewertet wird.
  

&nbsp;

**Heute habe ich...**                   
Ich habe mit dem Datensatz, den ich vorbereitet habe, ein ML-Model erstellt. Dieses funktionierte überhaupt nicht. Am Schluss habe ich den Datensatz nochmal neu bearbeitet, habe gewisse Zeilen herausgelöscht und das Model neu trainiert. Anschliessend funktionierte das Model angemessen. Danach habe ich zuerst mal in der Konsole versucht, das Abfragesystem zu implementieren. Ich hatte Probleme, die Fragen an das ML-Model weiterzugeben, mithilfe von KI habe ich es anschliessend geschafft. Nun kann man Fragen beantworten und anhand dessen wird ein Auto vorhergesagt. Ich bin jedoch noch nicht zufrieden, da es sehr oberflächlich ist und irgendwie nichts Intelligentes dabei herumkommt. Ausserdem habe ich es auch nicht geschafft, das Ganze in Flask zu implementieren. 

&nbsp;

&nbsp;


## 06.06
Ihr Projekt sollte nun alle Funktionalität haben, dass man es benutzen kann. Allerdings gibt es sicher noch Teile, welche "schöner" werden können: Layout, Code, Architektur... beschreiben Sie kurz den Stand Ihres Projekts, und leiten Sie daraus 6 solche "kosmetischen" AP für den 6.6 und den 13.6 ab.

- [x] **Fortschritt aufholen**: ML-Model in Flask implementieren
- [x] CSS für die Flask umgebung machen
- [x] Grob: Code Formatieren, Layout, Variablen etc. 


&nbsp;

**Heute habe ich...**           
Heute habe ich zuerst mein Machine-Learning-Modell in eine Flask Umgebung eingebunden. Dies konnte ich mit meinen Grundkenntnissen und mithilfe von KI über die Struktur meiner Dateien schnell umsetzen. Anschliessend wollte ich ein CSS für die Website machen. Ich habe angefangen, jedoch war ich überhaupt nicht zufrieden wie es aussah und ich hatte keine Übersicht mehr in meinem CSS File. Also habe ich geschaut, wie gut das Design rauskommt, wenn ich es von Claude erstellen lasse und es war um einiges besser als mein erstelltes. Deshalb habe ich mich für das KI erstelle Design entschieden, dies noch etwas abgeändert und war zufrieden. Am Schluss bin ich noch kurz über alle Files drübergegangen und hab grobe Unschönheiten korrigiert, bin jedoch noch nicht in die Tiefe gegangen. 

&nbsp;

&nbsp;

## 13.06

- [x] Code Layout feinschliff, (flake8, W3C)
- [x] Github überarbeiten, File Struktur etc. 

&nbsp;

**Heute habe ich...**               
Ich habe das Projekt aus der Coding Sicht fertig gemacht. Habe mittels Flake8 noch meine Python Files überprüft und mittels W3C die HTML Files gecheckt. Anschliessend habe ich das Projekt auf GitHub hochgeladen (`Car_Akinator`). Das einzige Problem, welches von Anfang an besteht, ist dass ich keinen guten Datensatz habe. Denn die Vorhersage funktioniert zwar, aber nur, wenn man die genauen Daten des Autos aus der Datenbank hat. Für das Akinatormässige Vorhersagen eines zufälligen Autos ist das Modell nicht imstande (durch zu ungenau Prediction und nicht guten Datensatz). Dies möchte ich nächste Woche noch angehen.  

&nbsp;

&nbsp;

## 20.06
Was fehlt Ihrem fertigen Projekt noch, um es auszuliefern? Reicht die Zeit für ein *nice-to-have feature*?

- [ ] Passender Datensatz für mein Use Case finden.
- [x] Diesen Datensatz anpassen.

&nbsp;

**Heute habe ich...**             
Ich habe versucht einen passenden Datensatz zu finden, wobei ich nicht erfolgreich war, da diese nie die richtigen Features hatten oder zu komplex waren. Anschliessend habe ich versucht, mit KI Datensätze zu erstellen, was funktionierte jedoch nur in kleinerer Menge. Das Training meines Models mit den Datensätzen war überhaupt nicht erfolgreich, ich hatte eine accuray von 30%-50% und bei jeder Vorhersage war es ein falsches Auto.
Ich habe versucht die Abfrage zu verbessern, indem die Antworten eine kleine Range ergaben (statt 3 mögliche Antworten bei PS, 6) jedoch hat dies auch nichts gebracht. Dann habe ich versucht den Datensatz zu erweitern, wieder mithilfe von KI, leider ergab das dann kein schönes Resultat mehr, welches ich benutzen könnte. 

Nach ewigen Herumprobieren suchen und testen habe ich mich dazu entschieden das mein Use-Case keinen Erfolg mehr haben wird auf dem jetzigen Weg. Das Model war einfach zu ungenau. Ich habe mithilfe von KI einen normalen Filter Algorithmus erstellt, um vielleicht noch etwas zu retten, dieser gibt jetzt die Top 3 Fahrzeuge anhand der Antworten des Benutzers aus, was natürlich nicht so spektakulär ist wie eine richtige Antwort. Dieses "Notfall Projekt" welches ich erstellt habe, damit ich während er Präsentation etwas zum Vorstellen habe, habe ich unter `Car_Filter` hochgeladen.


 Vergessen Sie nicht, die Unterlagen für Ihre Präsentation auf github hochzuladen.

## 27.06          
...

