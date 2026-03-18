from ._anvil_designer import Patient_DetailsTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Patient_Details(Patient_DetailsTemplate):
  def __init__(self, patient_id=None, **properties):
    self.init_components(**properties)

    daten = anvil.server.call('get_patient_details', patient_id)
  
    name = f"{daten[0]} {daten[1]}"
    geburt = daten[2]
    vers = daten[3]
  
    
    from datetime import datetime
    alter = datetime.now().year - int(geburt[:4])
  
    self.label_name.text = name
    self.label_alter.text = f"Alter: {alter}"
    self.label_vers.text = f"VersNr: {vers}"

  @handle("button_1", "click")
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("Startseite")

  @handle("button_2", "click")
  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("Startseite.Dashboard")

  @handle("button_3", "click")
  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("Startseite.Patienten")

  @handle("button_4", "click")
  def button_4_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("Startseite.Termine")
