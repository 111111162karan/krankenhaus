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
def get_termine_status_count():
  daten = query_database(
    """SELECT Status, COUNT(*) 
      FROM Termine
      GROUP BY Status;""")
  
  return daten

@anvil.server.callable
def get_behandlungen():
  daten = query_database("SELECT * FROM Behandlungen")
  return daten

@anvil.server.callable
def get_zimmer():
  daten = query_database("SELECT * FROM Zimmer")
  return daten
