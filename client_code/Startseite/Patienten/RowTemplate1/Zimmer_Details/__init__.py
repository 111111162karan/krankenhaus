from ._anvil_designer import Zimmer_DetailsTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Zimmer_Details(Zimmer_DetailsTemplate):
  def __init__(self,patient_id=None, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    daten = anvil.server.call('get_zimmer_von_patient', patient_id)
    if daten:
      z = daten[0]
      self.label_station.text = f"Station: {z[0]}"
      self.label_zimmer.text = f"Zimmer: {z[1]}"
      self.label_betten.text = f"Betten: {z[2]}"
    else:
      self.label_station.text = "Kein Zimmer zugewiesen"


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
    open_form("Startseite.Patienten")
