from ._anvil_designer import RowTemplate2Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class RowTemplate2(RowTemplate2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  @handle("button_1", "click")
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Startseite.Termine.RowTemplate2.Termin_Details', termin_id=self.item['id'])

  @handle("button_2", "click")
  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('update_termin_status', self.item['id'], "abgeschlossen")
    alert("Termin abgeschlossen")
    self.parent.raise_event("x-refresh")
    open_form("Startseite.Termine")

  @handle("button_3", "click")
  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('update_termin_status', self.item['id'], "abgesagt")
    alert("Termin abgesagt")
    self.parent.raise_event("x-refresh")
    open_form("Startseite.Termine")
