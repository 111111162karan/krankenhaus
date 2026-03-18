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
      
