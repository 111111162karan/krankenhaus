from ._anvil_designer import Termin_DetailsTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Termin_Details(Termin_DetailsTemplate):
  def __init__(self,termin_id=None ,**properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    daten = anvil.server.call('get_termin_details', termin_id)
  
    self.label_datum.text = f"Datum: {daten[0]} {daten[1]}"
    self.label_art.text = f"Art: {daten[2]}"
    self.label_status.text = f"Status: {daten[3]}"
    self.label_patient.text = f"Patient: {daten[4]} {daten[5]}"
    self.label_arzt.text = f"Arzt: {daten[6]} {daten[7]} ({daten[8]})"

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

  @handle("button_5", "click")
  def button_5_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("Startseite.Termine")
