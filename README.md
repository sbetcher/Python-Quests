Fragestellung: Quest#py-00-0001

🧙‍♂️ Objektorientiertes Python-Konsolenspiel: „Finde das Drachenei“

🎯 Aufgabenstellung

Erstelle ein textbasiertes Abenteuerspiel in Python. Ziel des Spiels ist es, durch verschiedene Räume zu reisen, mit Figuren zu interagieren, Gegenstände zu sammeln und schließlich das „Drachenei“ und den „Zauberspruch“ zu finden. Das Spiel ist gewonnen, sobald beide Objekte im Inventar sind.

Dabei soll ein objektorientierter Ansatz verwendet werden, um Räume, Figuren, Gegenstände und das Spielgeschehen strukturiert abzubilden.

🧩 Kernanforderungen
1. Klassenstruktur

    CObject: Repräsentiert einen Gegenstand, der in einem Raum liegt.

    CFigure: Repräsentiert eine Figur (z. B. Magier, Bär), die den Zugang zu bestimmten Räumen nur erlaubt, wenn man einen bestimmten Gegenstand besitzt.

    CRoom: Repräsentiert einen Raum mit:

        Beschreibung

        Nachbarräumen (verkettet)

        evtl. einem Gegenstand oder einer Figur

        Möglichkeit, eine Sonderregel für den Ausgang zu definieren

    BColors: Einfache Klasse zur farblichen Konsolenausgabe.

2. Spielstart

    Das Spiel beginnt in der „Heimatstadt“.

    Alle Räume, Gegenstände und Figuren werden beim Start definiert.

    Räume sind durch Nachbarschaften miteinander verbunden.

3. Spielverlauf

    Der Spieler kann sich durch Räume bewegen, Gegenstände aufnehmen und diese im Inventar verwalten.

    Einige Figuren blockieren den Weg, wenn ein benötigter Gegenstand fehlt.

    Spieler dürfen dann nur zu einem definierten „Ausweichraum“ weitergehen.

4. Steuerung

    Eingabe erfolgt über Konsolenbefehle:

        z → Zeige aktuellen Raum

        i → Zeige Inventar

        0-9 → Wähle Nachbarraum

        q → Spiel verlassen

🛠️ Technische Anforderungen

    Verwendung von objektorientierter Programmierung (Klassen, Objekte, Kapselung).

    Nutzung von Python-spezifischen Features wie:

        Konstruktoren (__init__)

        Zugriffskontrolle via Properties oder Namenskonvention (__attribute)

        Fehlerbehandlung bei Typprüfungen

    Übersichtliche Ausgabe über das Terminal mithilfe von ANSI-Farbcodes (BColors).

🚀 Erweiterungsmöglichkeiten (optional)

    Speichersystem für Spielstand.

    Einführung eines Lebenspunktsystems und Kämpfen.

    Mehrere Level mit zufälligen Karten.

    Interaktive Dialoge mit Figuren.

    GUI mit tkinter oder pygame.
