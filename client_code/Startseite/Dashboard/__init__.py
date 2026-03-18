from ._anvil_designer import DashboardTemplate
from anvil import *
import plotly.graph_objects as go
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import plotly.graph_objects as go

class Dashboard(DashboardTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
   

    # Any code you write here will run before the form opens.

  @handle("drop_down_1", "change")
  def drop_down_1_change(self, **event_args):
    """This method is called when an item is selected"""
    if self.drop_down_1.selected_value == "Termin Status":
      self.show_termine_status_pie()
    elif self.drop_down_1.selected_value == "Patienten pro Station":
      self.show_Patienten_pro_Station_Bar()

  @handle("plot_1", "show")
  def plot_1_show(self, **event_args):
    """This method is called when the Plot is shown on the screen"""
    self.show_termine_status_pie()

  def show_termine_status_pie(self):
    daten = anvil.server.call('get_termine_status')
    self.plot_1.data = [
    go.Pie(
      labels=["geplant", "abgeschlossen", "abgesagt"],
      values=daten
      )
    ]
  def show_Patienten_pro_Station_Bar(self):
    labels, values = anvil.server.call('get_patienten_pro_station')
    self.plot_1.data = [
      go.Bar(
        x=labels,
        y=values
      )
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


    
    