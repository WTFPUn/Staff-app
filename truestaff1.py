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
from kivy.uix.screenmanager import Screen,ScreenManager,FadeTransition
scope = ["https://www.googleapis.com/auth/spreadsheets.readonly"] 
credentials = ServiceAccountCredentials.from_json_keyfile_name('cre.json', scope)
gc = gspread.authorize(credentials)
sheet = gc.open_by_url("https://docs.google.com/spreadsheets/d/1cjdOui5vTFHKUdI7oEW6tqim3fM9eerMfFaBxfP0atc/edit#gid=0")


class MScreen(ScreenManager):
    def __init__(self, **kwargs):
        super(MScreen, self).__init__(**kwargs)

class GPS1Screen(Screen):
    def __init__(self,**kwargs):
        super(GPS1Screen,self).__init__(**kwargs)
        self.Grd = GridLayout()
        self.Grd.cols = 1
        self.inGrd = GridLayout(size_hint = (.2,None))
        self.inGrd.rows = 1
        self.ininGrd = GridLayout()
        self.ininGrd.cols= 3
        

        self.btn = Button(text = 'Click to 3D menu!')
        self.btn2 = Button(text = 'Click to Directory menu!')
        self.LabA = Label(text="Click to view curren coordinate!")
        self.btnA = Button(text = "Click!",on_press = self.getco)
        self.feed = Button(text = "Feed back",on_press = self.pressf3)

    
        self.Grd.add_widget(self.LabA)
        self.Grd.add_widget(self.ininGrd)
        for i in range(4):
            self.ininGrd.add_widget(Label(text = " "))
        self.ininGrd.add_widget(self.btnA)
        self.Grd.add_widget(self.inGrd)
        self.inGrd.add_widget(self.btn)
        self.inGrd.add_widget(self.btn2)
        self.inGrd.add_widget(self.feed)
        self.add_widget(self.Grd)
        

        self.btn.bind(on_press = self.pressf)
        self.btn2.bind(on_press = self.pressf2)
    def getco(self,instance):
        self.worksheet =sheet.get_worksheet(0)
        self.Lat = self.worksheet.cell(6,5).value
        self.Lng = self.worksheet.cell(7,5).value
        webbrowser.open(f"https://www.google.co.th/maps/@{self.Lat},{self.Lng},17.25z")
    def pressf(self,*args):
        self.manager.current = 'gps2'
    def pressf2(self,*args):
        self.manager.current = 'gps3'
    def pressf3(self,*args):
        self.manager.current = 'Feed'


class GPS2Screen(Screen):
    def __init__(self,**kwargs):
        super(GPS2Screen,self).__init__(**kwargs)
        self.Grd = GridLayout()
        self.Grd.cols = 1
        self.inGrd = GridLayout(size_hint = (.2,None))
        self.inGrd.rows = 1
        self.ininGrd = GridLayout()
        self.ininGrd.cols= 3
        

        self.btn = Button(text = 'Click to get coordinate!')
        self.btn2 = Button(text = 'Click to Directory menu!')
        self.Lab = Label(text ="Click to view 3D map")
        self.btt = Button(text = '3D Map!',on_press = self.getco)
        self.feed = Button(text = 'Feed back',on_press = self.pressf3)

        self.Grd.add_widget(self.Lab)
        self.Grd.add_widget(self.ininGrd)
        self.ininGrd.add_widget(Label(text = " "))
        self.ininGrd.add_widget(self.btt)
        for i in range(4):
            self.ininGrd.add_widget(Label(text = " "))
        self.Grd.add_widget(self.inGrd)
        self.inGrd.add_widget(self.btn)
        self.inGrd.add_widget(self.btn2)
        self.inGrd.add_widget(self.feed)
        self.add_widget(self.Grd)

        self.btn.bind(on_press = self.pressf)
        self.btn2.bind(on_press = self.pressf2)
    def getco(self,instance):
        self.worksheet =sheet.get_worksheet(0)
        self.Lat = self.worksheet.cell(6,5).value
        self.Lng = self.worksheet.cell(7,5).value
        webbrowser.open(f"https://www.google.co.th/maps/@{self.Lat},{self.Lng},1000m/data=!3m1!1e3")
    def pressf(self,*args):
        self.manager.current = 'gps1'
    def pressf2(self,*args):
        self.manager.current = 'gps3'
    def pressf3(self,*args):
        self.manager.current = 'Feed'

class GPS3Screen(Screen):
    def __init__(self,**kwargs):
        super(GPS3Screen,self).__init__(**kwargs)
        self.Grd = GridLayout()
        self.Grd.cols = 1
        self.inGrd = GridLayout(size_hint = (.2,None))
        self.inGrd.rows = 1
        self.ininGrd = GridLayout()
        self.ininGrd.cols= 3
        

        self.btn = Button(text = 'Click to get coordinate!')
        self.btn2 = Button(text = 'Click to 3D menu!')
        self.btt = Button(text = 'directory to target!',on_press = self.getco)
        self.Lab = Label(text = 'Ckick to directory to target')
        self.feed = Button(text = 'Feed back',on_press = self.pressf3)

        self.Grd.add_widget(self.Lab)
        
        self.Grd.add_widget(self.ininGrd)
        self.ininGrd.add_widget(Label(text = " "))
        self.ininGrd.add_widget(self.btt)
        for i in range(4):
            self.ininGrd.add_widget(Label(text = " "))
        self.Grd.add_widget(self.inGrd)
        self.inGrd.add_widget(self.btn)
        self.inGrd.add_widget(self.btn2)
        self.inGrd.add_widget(self.feed)
        self.add_widget(self.Grd)

        self.btn.bind(on_press = self.pressf)
        self.btn2.bind(on_press = self.pressf2)
    def getco(self,instance):
        self.worksheet =sheet.get_worksheet(0)
        self.Lat = self.worksheet.cell(6,5).value
        self.Lng = self.worksheet.cell(7,5).value
        print(self.Lat)
        webbrowser.open(f"https://www.google.co.th/maps/dir/_/{self.Lat},{self.Lng}")
    def pressf(self,*args):
        self.manager.current = 'gps1'
    def pressf2(self,*args):
        self.manager.current = 'gps2'
    def pressf3(self,*args):
        self.manager.current = 'Feed'

from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
class Feedback(Screen):
    def __init__(self,**kwargs):
        super(Feedback,self).__init__(**kwargs)
        self.Grd = GridLayout()
        self.Grd.cols = 1
        self.inGrd = GridLayout(size_hint = (.2,None))
        self.inGrd.rows = 1
        self.textinp = TextInput(text = "Input your Feedback!")
        self.btback = Button(text="Back",on_release = self.previous)
        
        self.btn = Button(text= "submit!",on_press = self.sendback,size_hint =(0.2,None))
        self.Grd.add_widget(self.textinp)
        self.Grd.add_widget(self.btn)
        
        self.Grd.add_widget(self.inGrd)
        self.add_widget(self.Grd)
        self.inGrd.add_widget(Label(text ="",size_hint=(None,0.5)))
        self.inGrd.add_widget(self.btback)
        self.inGrd.add_widget(Label(text ="",size_hint=(None,0.5)))
        
    def sendback(self,instance):
        self.con = Button(text="Close",size_hint=(.2, None))
        self.pop = Popup(title='You are already sent', content=self.con)
        self.con.bind(on_press = self.pop.dismiss)
        self.pop.open()
        self.textinp.text = ""
    def previous(self,instance):
        self.manager.current = "gps1"


class IntelligenceStaffApp(App):
    def build(self):
        ms = MScreen(transition=FadeTransition())
        ms.add_widget(GPS1Screen(name = 'gps1'))
        ms.add_widget(GPS2Screen(name = 'gps2'))
        ms.add_widget(GPS3Screen(name = 'gps3'))
        ms.add_widget(Feedback(name = 'Feed'))

        return ms

IntelligenceStaffApp().run()  