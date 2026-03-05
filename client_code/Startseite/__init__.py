from ._anvil_designer import StartseiteTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Startseite(StartseiteTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  @handle("drop_down_1", "change")
  def drop_down_1_change(self, **event_args):
    """This method is called when an item is selected"""
    if self.drop_down_1.selected_value == "Startseite":
      open_form('Startseite')
    elif self.drop_down_1.selected_value == "Medizin":
      open_form('Startseite.Medizin')
    elif self.drop_down_1.selected_value == "Organisation":
      open_form('Startseite.Organisation')
    elif self.drop_down_1.selected_value == "Statistik":
      open_form('Startseite.Statistik')

  @handle("Dashboard_Button", "click")
  def Dashboard_Button_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Startseite.Dashboard')

  @handle("Patienten_Button", "click")
  def Patienten_Button_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Startseite.Patienten')

  @handle("Termin_Button", "click")
  def Termin_Button_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Startseite.Termine')
      
