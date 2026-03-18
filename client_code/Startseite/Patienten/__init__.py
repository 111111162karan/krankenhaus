from ._anvil_designer import PatientenTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Patienten(PatientenTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.load_patienten()


def load_patienten(self):
  daten = anvil.server.call('get_patienten_liste')

  self.Patienten_Grid.items = [
    {
      "id": row[0],
      "name": f"{row[1]} {row[2]}",
      "geburtsdatum": row[3],
      "geschlecht": row[4]
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

