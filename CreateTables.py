import sqlite3

conn = sqlite3.connect("krankenhaus.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Patienten (
    PatientenID INTEGER PRIMARY KEY AUTOINCREMENT,
    Vorname TEXT NOT NULL,
    Nachname TEXT NOT NULL,
    Geburtsdatum DATE NOT NULL,
    Geschlecht TEXT,
    Versicherungsnummer TEXT NOT NULL
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Aerzte (
    ArztID INTEGER PRIMARY KEY AUTOINCREMENT,
    Vorname TEXT NOT NULL,
    Nachname TEXT NOT NULL,
    Fachgebiet TEXT NOT NULL
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Arbeitszeiten (
    ArbeitszeitID INTEGER PRIMARY KEY AUTOINCREMENT,
    ArztID INTEGER NOT NULL,
    Wochentag TEXT NOT NULL,
    Beginn TIME NOT NULL,
    Ende TIME NOT NULL
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Zimmer (
    ZimmerID INTEGER PRIMARY KEY AUTOINCREMENT,
    Stationsname TEXT NOT NULL,
    Zimmernummer TEXT NOT NULL,
    Belegungsstatus TEXT NOT NULL,
    Bettenanzahl INTEGER NOT NULL
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Zimmerbelegung (
    BelegungID INTEGER PRIMARY KEY AUTOINCREMENT,
    PatientenID INTEGER NOT NULL,
    ZimmerID INTEGER NOT NULL,
    Einzugsdatum DATE NOT NULL,
    Auszugsdatum DATE
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Termine (
    TerminID INTEGER PRIMARY KEY AUTOINCREMENT,
    PatientenID INTEGER NOT NULL,
    ArztID INTEGER NOT NULL,
    Uhrzeit TIME NOT NULL,
    Datum DATE NOT NULL,
    Terminart TEXT NOT NULL,
    Status TEXT NOT NULL
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Behandlungen (
    BehandlungID INTEGER PRIMARY KEY AUTOINCREMENT,
    PatientenID INTEGER NOT NULL,
    ArztID INTEGER NOT NULL,
    Diagnose TEXT NOT NULL,
    Beschreibung TEXT,
    Behandlungsdatum TIMESTAMP NOT NULL
);
""")

conn.commit()
conn.close()

print("Datenbank erfolgreich erstellt!")

import sqlite3
import random
from datetime import datetime, timedelta

conn = sqlite3.connect("krankenhaus.db")
cursor = conn.cursor()

# -----------------------------
# Hilfsdaten
# -----------------------------
vornamen = ["Max", "Anna", "Lukas", "Laura", "Tim", "Sophie", "Leon", "Emma", "Paul", "Mia"]
nachnamen = ["Müller", "Schmidt", "Schneider", "Fischer", "Weber", "Wagner", "Becker", "Hoffmann"]
fachgebiete = ["Chirurgie", "Innere Medizin", "Kardiologie", "Neurologie", "Orthopädie"]
diagnosen = ["Grippe", "Bruch", "Bluthochdruck", "Migräne", "Infektion"]
terminarten = ["Untersuchung", "Operation", "Beratung"]
statusliste = ["geplant", "abgeschlossen", "abgesagt"]
wochentage = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag"]

# -----------------------------
# Patienten
# -----------------------------
for i in range(50):
    cursor.execute("""
        INSERT INTO Patienten (Vorname, Nachname, Geburtsdatum, Geschlecht, Versicherungsnummer)
        VALUES (?, ?, ?, ?, ?)
    """, (
        random.choice(vornamen),
        random.choice(nachnamen),
        f"{random.randint(1960, 2015)}-0{random.randint(1,9)}-{random.randint(10,28)}",
        random.choice(["m", "w"]),
        f"VNR{random.randint(100000,999999)}"
    ))

# -----------------------------
# Ärzte
# -----------------------------
for i in range(15):
    cursor.execute("""
        INSERT INTO Aerzte (Vorname, Nachname, Fachgebiet)
        VALUES (?, ?, ?)
    """, (
        random.choice(vornamen),
        random.choice(nachnamen),
        random.choice(fachgebiete)
    ))

# -----------------------------
# Arbeitszeiten
# -----------------------------
for arzt_id in range(1, 16):
    for tag in wochentage:
        cursor.execute("""
            INSERT INTO Arbeitszeiten (ArztID, Wochentag, Beginn, Ende)
            VALUES (?, ?, ?, ?)
        """, (
            arzt_id,
            tag,
            "08:00",
            "16:00"
        ))

# -----------------------------
# Zimmer
# -----------------------------
for i in range(30):
    cursor.execute("""
        INSERT INTO Zimmer (Stationsname, Zimmernummer, Belegungsstatus, Bettenanzahl)
        VALUES (?, ?, ?, ?)
    """, (
        f"Station {random.randint(1,5)}",
        str(100 + i),
        "frei",
        random.randint(1,4)
    ))

# -----------------------------
# Termine
# -----------------------------
for i in range(120):
    cursor.execute("""
        INSERT INTO Termine (PatientenID, ArztID, Uhrzeit, Datum, Terminart, Status)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        random.randint(1, 50),
        random.randint(1, 15),
        f"{random.randint(8,16)}:00",
        (datetime.now() + timedelta(days=random.randint(-30,30))).strftime("%Y-%m-%d"),
        random.choice(terminarten),
        random.choice(statusliste)
    ))

# -----------------------------
# Behandlungen
# -----------------------------
for i in range(150):
    cursor.execute("""
        INSERT INTO Behandlungen (PatientenID, ArztID, Diagnose, Beschreibung, Behandlungsdatum)
        VALUES (?, ?, ?, ?, ?)
    """, (
        random.randint(1, 50),
        random.randint(1, 15),
        random.choice(diagnosen),
        "Standardbehandlung durchgeführt",
        (datetime.now() - timedelta(days=random.randint(0,365))).strftime("%Y-%m-%d %H:%M:%S")
    ))

# -----------------------------
# Zimmerbelegung
# -----------------------------
for i in range(200):
    start = datetime.now() - timedelta(days=random.randint(1,100))
    end = start + timedelta(days=random.randint(1,20))

    cursor.execute("""
        INSERT INTO Zimmerbelegung (PatientenID, ZimmerID, Einzugsdatum, Auszugsdatum)
        VALUES (?, ?, ?, ?)
    """, (
        random.randint(1, 50),
        random.randint(1, 30),
        start.strftime("%Y-%m-%d"),
        end.strftime("%Y-%m-%d")
    ))

conn.commit()
conn.close()

print("Viele Testdaten erfolgreich eingefügt!")