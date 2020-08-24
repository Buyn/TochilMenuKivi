# ----------------------------------------------
# * Imports :
# ----------------------------------------------
import kivy
kivy.require('1.0.5')
from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock
from functools import partial
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, StringProperty
import time
from datetime import date, datetime


# ----------------------------------------------
# * class FirstKivy(App): :
# ** ----------------------------------------------:
class FirstKivy(App):
# ** __init__ : 
    def __init__(self):
        super().__init__()
        self.newtext = "New!"


# ----------------------------------------------
# ** build : 
    def build(self):
        button = Button(text="Welcome to LikeGeeks!",
                        # pos=(300,350), 
                        # size_hint = (.25, .18))
                        )
        button.bind(on_press = partial(self.udateButton, button) )
        button.bind(on_press = partial(self.updateText, button) )
        label = Label(text="Hello Kivy!"
                      # , size_hint = (.25, .18)
                        )
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(label)
        layout.add_widget(button)
        return layout


# ----------------------------------------------
# ** def updateText : 
    def updateText(self, inst, *args):
        self.newtext = self.newtext + "- Even Newer! "


# ----------------------------------------------
# ** def udateButton : 
    def udateButton(self, inst, *args): 
        inst.text = self.newtext
                

# ----------------------------------------------
# ** ----------------------------------------------:
# * class Main_Windows :
# ** ----------------------------------------------:
class Main_Windows():
# ** def __init__(self): : 
    def __init__(self):
        self.temp_A = 11
        self.temp_B = 14


# ----------------------------------------------
# ** ----------------------------------------------:
# * class Interface(BoxLayout): : 
# ** -Interface------------------------------------:
class Interface(BoxLayout):
# class Interface(FloatLayout):
    # label_wid = ObjectProperty()
    # info = StringProperty()

# ----------------------------------------------
# ** def __init__(self, **kwargs): : 
    # def __init__(self, **kwargs):
    #     super(Interface, self).__init__(**kwargs)
        # self.label_dateid.text = datetime.now().strftime("%d/%m/%Y")
        # self.label_timeid.text = datetime.now().strftime("%H:%M:%S")
        # self.event_time_updaaate = Clock.schedule_interval(
        #                     self.update_time, 0.5)


# ----------------------------------------------
# ** def update_time(self): : 
    def update_time(self, cb):
        self.label_timeid.text = datetime.now().strftime("%H:%M:%S")


# ----------------------------------------------
# ** def do_action(self): : 
    def do_action(self):
        self.label_dateid.text = datetime.now().strftime("%d/%m/%Y")
        self.label_timeid.text = datetime.now().strftime("%H:%M:%S")
        # self.info = "hello world"
        # print("Time = ", time.time())
        # print("date = ", datetime.now().strftime("%d/%m/%Y"))
        # print("Time = ", datetime.now().strftime("%H:%M:%S"))


# ----------------------------------------------
# ** ----------------------------------------------:


# * class MainScreen(BoxLayout): : 
# ** -MainScreen------------------------------------:
class MainScreen(BoxLayout):
# class Interface(FloatLayout):
    # curent_time_label = ObjectProperty()
    # curent_date_label = ObjectProperty()
    # label_dateid = ObjectProperty(datetime.now().strftime("%d/%m/%Y"))
    # label_timeid = ObjectProperty(datetime.now().strftime("%H:%M:%S"))
    info = StringProperty()

# ----------------------------------------------
# ** def __init__(self, **kwargs): : 
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        # self.curent_time_label.text = datetime.now().strftime("%d/%m/%Y")
        # self.curent_date_label.text = datetime.now().strftime("%H:%M:%S")
        # self.label_dateid.text = datetime.now().strftime("%d/%m/%Y")
        # self.label_timeid.text = datetime.now().strftime("%H:%M:%S")
        self.event_time_updaaate = Clock.schedule_interval(
                            self.update_time, 0.5)


# ----------------------------------------------
# ** def update_time(self): : 
    def update_time(self, cb):
        self.label_dateid.text = datetime.now().strftime("%d/%m/%Y")
        self.label_timeid.text = datetime.now().strftime("%H:%M:%S")


# ----------------------------------------------
# ** def do_action(self): : 
    def do_action(self):
        self.label_dateid.text = datetime.now().strftime("%d/%m/%Y")
        self.label_timeid.text = datetime.now().strftime("%H:%M:%S")
        # self.info = "hello world"
        # print("Time = ", time.time())
        # print("date = ", datetime.now().strftime("%d/%m/%Y"))
        # print("Time = ", datetime.now().strftime("%H:%M:%S"))


# ----------------------------------------------
# ** ----------------------------------------------:


# * class TochilMenuApp(App): 
# ** ------TochilMenuApp-----------------------:
class TochilMenuApp(App):

# ** def build(self): : 
    def build(self):
        root_widget = Interface()
        return root_widget


# ----------------------------------------------
# ** ----------------------------------------------:
# * def main(argv): : 
# ----------------------------------------------
def main(argv):
    print ("hello world!")
    print (argv)
    # FirstKivy().run()
    print("date.today = ", date.today())
    TochilMenuApp().run()


# ----------------------------------------------
# * if __name__ == "__main__":  
# ----------------------------------------------
if __name__ == "__main__": 
    import sys
    # sys.argv = ['', 'Test.testName']
    main(sys.argv)
# ----------------------------------------------
# * ----------------------------------------------:
