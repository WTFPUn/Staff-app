import kivy
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.network.urlrequest import UrlRequest
from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.graphics import Color
import webbrowser
from oauth2client.service_account import ServiceAccountCredentials
import gspread
from kivy.uix.screenmanager import Screen,ScreenManager,FadeTransition
scope = ["https://www.googleapis.com/auth/spreadsheets.readonly"] 
credentials = ServiceAccountCredentials.from_json_keyfile_name('cre.json', scope)
gc = gspread.authorize(credentials)
sheet = gc.open_by_url("https://docs.google.com/spreadsheets/d/1cjdOui5vTFHKUdI7oEW6tqim3fM9eerMfFaBxfP0atc/edit#gid=0")
from kivy.core.text import LabelBase
LabelBase.register(name= "angsana",fn_regular="angsana.ttc")
from kivy.core.window import Window
from kivy.clock import Clock
from plyer import notification
Window.clearcolor = (1, 1, 1, 0.2)


bgc = {"normal":[1,.50,.50,1],"3D":[.5, 1,.5,0.7],"mark":[.3,.3,1,1],"feed":[1, .5, 0, 1]}
class MScreen(ScreenManager):
    def __init__(self, **kwargs):
        super(MScreen, self).__init__(**kwargs)
        
    
        
import time

class GPS1Screen(Screen):
    def __init__(self,**kwargs):
        super(GPS1Screen,self).__init__(**kwargs)
        self.Grd = GridLayout()
        self.Grd.cols = 1
        self.inGrd = GridLayout(size_hint = (1,1.2))
        self.inGrd.rows = 1
        self.ininGrd = GridLayout()
        self.ininGrd.cols= 3
        


        self.btn = Button(text = "แสดงมุมมองดาวเทียม",font_name = "angsana",font_size=40,color = [255,255,255,1],background_color = bgc["3D"])
        self.btn2 = Button(text = 'ไปหาเป้าหมาย',font_name = "angsana",font_size=40,color = [255,255,255,1],background_color = bgc["mark"])
        self.LabA = Label(text = 'คลิกเพื่อแสดงพิกัด',font_name = "angsana",font_size=40,color = [255,255,255,1])
        self.btnA = Button(text = "แสดงพิกัด",on_press = self.getco,font_name = "angsana",font_size=40,color = [255,255,255,1])
        self.feed = Button(text = "ให้คำแนะนำ\nรายงานปัญหา",on_press = self.pressf3,background_color =bgc["feed"],font_name = "angsana",font_size=40,color = [255,255,255,1])

    
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
        self.Lat = self.worksheet.cell(6,11).value
        self.Lng = self.worksheet.cell(7,11).value
        

        webbrowser.open(f"http://maps.google.com/maps?t=m&q=loc:{self.Lat}+{self.Lng}")
        
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
        self.inGrd = GridLayout(size_hint = (1,1.2))
        self.inGrd.rows = 1
        self.ininGrd = GridLayout()
        self.ininGrd.cols= 3
        

        self.btn = Button(text = 'แสดงพิกัดปกติ',font_name = "angsana",font_size=40,color = [255,255,255,1],border =[10,10,10,10],background_color = bgc["normal"])
        self.btn2 = Button(text = 'ไปหาเป้าหมาย',font_name = "angsana",font_size=40,color = [255,255,255,1],border =[10,10,10,10],background_color = bgc["mark"])
        self.Lab = Label(text = 'คลิกเพื่อแสดงพิกัดแบบ3มิติ',font_name = "angsana",font_size=40,color = [255,255,255,1])
        self.btt = Button(text = 'แสดงมุมมองดาวเทียม',font_name = "angsana",font_size=40,color = [255,255,255,1],on_press = self.getco)
        self.feed = Button(text = 'ให้คำแนะนำ\nรายงานปัญหา',on_press = self.pressf3,background_color =bgc["feed"],font_name = "angsana",font_size=40,color = [255,255,255,1])

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
        self.Lat = self.worksheet.cell(6,11).value
        self.Lng = self.worksheet.cell(7,11).value
        webbrowser.open(f"http://maps.google.com/maps?t=k&q=loc:{self.Lat}+{self.Lng}")
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
        self.inGrd = GridLayout(size_hint = (1,1.2))
        self.inGrd.rows = 1
        self.ininGrd = GridLayout()
        self.ininGrd.cols= 3
        

        self.btn = Button(text = 'แสดงพิกัดปกติ',font_name = "angsana",font_size=40,color = [255,255,255,1],background_color = bgc["normal"])
        self.btn2 = Button(text = 'แสดงมุมมองดาวเทียม',font_name = "angsana",font_size=40,color = [255,255,255,1],background_color = bgc["3D"])
        self.btt = Button(text = 'แสดงเส้นทางการเดินทาง',font_name = "angsana",font_size=40,color = [255,255,255,1],on_press = self.getco)
        self.Lab = Label(text = 'คลิกเพื่อแสดงเส้นทางการเดินทาง',font_name = "angsana",font_size=40,color = [255,255,255,1])
        self.feed = Button(text = 'ให้คำแนะนำ\nรายงานปัญหา',on_press = self.pressf3,background_color =bgc["feed"],font_name = "angsana",font_size=40,color = [255,255,255,1])

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
        self.Lat = self.worksheet.cell(6,11).value
        self.Lng = self.worksheet.cell(7,11).value
        webbrowser.open(f"https://www.google.co.th/maps/dir/Current+Location/{self.Lat},{self.Lng}")
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
        Clock.schedule_interval(self.call,10)

        return ms
    def call(self,instance):    
        self.worksheet =sheet.get_worksheet(0)
        self.check = self.worksheet.cell(8,11).value
        if self.check == "1":
            notification.notify(title = "Warning",message ="ผู้ใช้ไม้เท้ากำลังเดือดร้อนเข้าไปกดเพื่อดูตำแหน่ง",timeout=5)
        
            


IntelligenceStaffApp().run()
  