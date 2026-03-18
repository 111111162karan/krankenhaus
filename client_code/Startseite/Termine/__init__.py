from ._anvil_designer import TermineTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Termine(TermineTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.set_event_handler("x-refresh", self.load_termine)
    self.load_termine()

  def load_termine(self):
    daten = anvil.server.call('get_termine_liste')
  
    self.repeating_panel_1.items = [
      {
        "id": row[0],
        "datum": row[1],
        "uhrzeit": row[2],
        "art": row[3],
        "status": row[4],
        "patient": row[5],
        "arzt": row[6]
      }
      for row in daten
    ]
    
  @handle("button_1", "click")
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Startseite')

  @handle("button_2", "click")
  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Startseite.Dashboard')

  @handle("button_3", "click")
  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Startseite.Patienten')

  @handle("button_4", "click")
  def button_4_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Startseite.Termine')
    # Any code you write here will run before the form opens.


