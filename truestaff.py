import kivy
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.network.urlrequest import UrlRequest
from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.base import runTouchApp
from kivy.lang import Builder
import webbrowser
from oauth2client.service_account import ServiceAccountCredentials
import gspread
scope = ["https://www.googleapis.com/auth/spreadsheets.readonly"] 
credentials = ServiceAccountCredentials.from_json_keyfile_name('cre.json', scope)
gc = gspread.authorize(credentials)
sheet = gc.open_by_url("https://docs.google.com/spreadsheets/d/1cjdOui5vTFHKUdI7oEW6tqim3fM9eerMfFaBxfP0atc/edit#gid=0")

class Mygrid(GridLayout):
    def __init__(self,**kwargs):
        super(Mygrid,self).__init__(**kwargs)
        self.cols = 2
        self.Tellcoor = Label(text="Pres to view Lattitude LongTitude")
        self.add_widget(self.Tellcoor)
        self.bt = Button(text = "Press!",on_release = self.press)
        self.add_widget(self.bt)
    def press(self,instance):
        self.worksheet =sheet.get_worksheet(0)
        self.Lat = self.worksheet.cell(6,5).value
        self.Lng = self.worksheet.cell(7,5).value
        webbrowser.open(f"https://www.google.co.th/maps/@{self.Lat},{self.Lng},20z")

    


class MyaApp(App):
    def build(self):
        return Mygrid()

MyaApp().run()