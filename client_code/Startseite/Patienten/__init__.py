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
