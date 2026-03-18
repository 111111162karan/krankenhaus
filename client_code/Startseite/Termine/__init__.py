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


