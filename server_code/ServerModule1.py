import anvil.files
from anvil.files import data_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import sqlite3

@anvil.server.callable
def query_database(query: str):
  with sqlite3.connect(data_files["krankenhaus.db"]) as conn:
    cur = conn.cursor()
    result = cur.execute(query).fetchall()
  return result
  
@anvil.server.callable
def get_patienten():
  daten = query_database("SELECT * FROM Patienten")
  return daten
  
@anvil.server.callable
def get_aerzte():
  daten = query_database("SELECT * FROM Aerzte")
  return daten
  
@anvil.server.callable
def get_termine():
  daten = query_database("SELECT * FROM Termine")
  return daten

@anvil.server.callable
def get_termine_status():
  query = """
        SELECT Status, COUNT(*)
        FROM Termine
        GROUP BY Status
    """

  keys = ["geplant", "abgeschlossen", "abgesagt"]
  status_dict = query_to_dict(query, keys)
  return list(status_dict.values())


@anvil.server.callable
def query_to_dict(query, keys):
  with sqlite3.connect(data_files["krankenhaus.db"]) as conn:
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    data_dict = {k: 0 for k in keys}
    for key, value in result:
      if key in data_dict:
        data_dict[key] = value
    return data_dict


@anvil.server.callable
def get_behandlungen():
  daten = query_database("SELECT * FROM Behandlungen")
  return daten

@anvil.server.callable
def get_zimmer():
  daten = query_database("SELECT * FROM Zimmer")
  return daten

@anvil.server.callable
def get_patienten_pro_station():
  stationen_query = "SELECT DISTINCT Stationsname FROM Zimmer"
  stationen = query_database(stationen_query)
  keys = [s[0] for s in stationen]

  query = """
    SELECT z.Stationsname, COUNT(*)
    FROM Zimmerbelegung zb
    JOIN Zimmer z ON zb.ZimmerID = z.ZimmerID
    GROUP BY z.Stationsname
  """

  station_dict = query_to_dict(query, keys)
  return keys, list(station_dict.values())

@anvil.server.callable
def get_patienten_liste():
  return query_database("""
    SELECT PatientenID, Vorname, Nachname, Geburtsdatum, Geschlecht
    FROM Patienten
  """)
@anvil.server.callable
def get_patient_details(patient_id):
  return query_database(f"""
    SELECT Vorname, Nachname, Geburtsdatum, Versicherungsnummer
    FROM Patienten
    WHERE PatientenID = {patient_id}
  """)[0]
