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
from kivy.uix.screenmanager import ScreenManager, Screen
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
    def __init__(self, **kwargs):
        super(Interface, self).__init__(**kwargs)
        # self.label_dateid.text = datetime.now().strftime("%d/%m/%Y")
        # self.label_timeid.text = datetime.now().strftime("%H:%M:%S")
        # self.event_time_updaaate = Clock.schedule_interval(
        #                     self.update_time, 0.5)
        # print ("*******ids-interfase*******")
        # for key, val in self.ids.items():
        #     print("key={0}, val={1}".format(key, val))


# ----------------------------------------------
# ** ----------------------------------------------:


# * class MainScreen(Screen): : 
# ** -MainScreen------------------------------------:
class MainScreen(Screen):
# class Interface(FloatLayout):
    """ Стартовый экран выводит значения таймера
        и значения текушего времени и даты
        перобразование времени можно проследить на этих функциях
        # curent_time_label = ObjectProperty()
        # label_dateid = ObjectProperty(datetime.now().strftime("%d/%m/%Y"))
        # label_timeid = ObjectProperty(datetime.now().strftime("%H:%M:%S"))
        info = StringProperty() производит опрос переменых из кв
        для дальнейшего испльзования
    """
    info = StringProperty()

# ----------------------------------------------
# ** def __init__(self, **kwargs): : 
    def __init__(self, **kwargs):
        """ Инициалзация стартого экран с
        примерами ковертации времени для переменых
         из кв дезайна
        # self.curent_time_label.text = datetime.now().strftime("%d/%m/%Y")
        # self.curent_date_label.text = datetime.now().strftime("%H:%M:%S")
        # self.label_dateid.text = datetime.now().strftime("%d/%m/%Y")
        # self.label_timeid.text = datetime.now().strftime("%H:%M:%S")
        один из методов нахождения айди из кв
        # print ("self.info = " , self.info)
        #no ids found
        # for key, val in self.ids.items():
        #     print("key={0}, val={1}".format(key, val))
        """
        # print ("*******ids-mainscreen*******")
        super(MainScreen, self).__init__(**kwargs)
        #  self.event_time_update for late use
        self.event_time_update = Clock.schedule_interval(
                            self.update_time, 0.5)


# ----------------------------------------------
# ** def update_time(self): : 
    def update_time(self, cb):
        # only after StringProperty() in init class
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


# * class SharpScreen(Screen): : 
# ** -SharpScreen------------------------------------:
class SharpScreen(Screen):
# class Interface(FloatLayout):
    # curent_time_label = ObjectProperty()
    # curent_date_label = ObjectProperty()
    # label_dateid = ObjectProperty(datetime.now().strftime("%d/%m/%Y"))
    # label_timeid = ObjectProperty(datetime.now().strftime("%H:%M:%S"))
    info = StringProperty()

# ----------------------------------------------
# ** def __init__(self, **kwargs): : 
    # def __init__(self, **kwargs):
    #     super(SharpScreen, self).__init__(**kwargs)
        # self.curent_time_label.text = datetime.now().strftime("%d/%m/%Y")
        # self.curent_date_label.text = datetime.now().strftime("%H:%M:%S")
        # self.label_dateid.text = datetime.now().strftime("%d/%m/%Y")
        # self.label_timeid.text = datetime.now().strftime("%H:%M:%S")
        # self.event_time_updaaate = Clock.schedule_interval(
        #                     self.update_time, 0.5)


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


# * class ConformSharpeningScreen(Screen): : 
# ** -ConformSharpeningScreen------------------------------------:
class ConformSharpeningScreen(Screen):
    info = StringProperty()

# ----------------------------------------------
# ** def __init__(self, **kwargs): : 
    # def __init__(self, **kwargs):
    #     super(SharpScreen, self).__init__(**kwargs)
        # self.curent_time_label.text = datetime.now().strftime("%d/%m/%Y")
        # self.curent_date_label.text = datetime.now().strftime("%H:%M:%S")
        # self.label_dateid.text = datetime.now().strftime("%d/%m/%Y")
        # self.label_timeid.text = datetime.now().strftime("%H:%M:%S")
        # self.event_time_updaaate = Clock.schedule_interval(
        #                     self.update_time, 0.5)


# ----------------------------------------------
# ** ----------------------------------------------:


# * class ProcessScreen(Screen): : 
# ** ProcessScreen------------------------------------:
class ProcessScreen(Screen):
    info = StringProperty()

# ** def __init__(self, **kwargs): : 
    def __init__(self, **kwargs):
        # print ("*******ids-ProcessScreen*******")
        super( ProcessScreen, self).__init__(**kwargs)
        #  self.event_time_update for late use
        # self.event_time_update = Clock.schedule_interval(
        #                     self.update_time, 0.5)


# ----------------------------------------------
# ** def update_time(self): : 
    def update_time(self, cb):
        # only after StringProperty() in init class
        self.label_dateid.text = datetime.now().strftime("%d/%m/%Y")
        self.label_timeid.text = datetime.now().strftime("%H:%M:%S")


# ----------------------------------------------
# ----------------------------------------------
# ** ----------------------------------------------:


# * class TimerScreen(Screen): : 
# ** TimerScreen------------------------------------:
class TimerScreen(Screen):
# class Interface(FloatLayout):
    # curent_time_label = ObjectProperty()
    # curent_date_label = ObjectProperty()
    # label_dateid = ObjectProperty(datetime.now().strftime("%d/%m/%Y"))
    # label_timeid = ObjectProperty(datetime.now().strftime("%H:%M:%S"))
    info = StringProperty()

# ----------------------------------------------
# ** def __init__(self, **kwargs): : 
    # def __init__(self, **kwargs):
    #     super(SharpScreen, self).__init__(**kwargs)
        # self.curent_time_label.text = datetime.now().strftime("%d/%m/%Y")
        # self.curent_date_label.text = datetime.now().strftime("%H:%M:%S")
        # self.label_dateid.text = datetime.now().strftime("%d/%m/%Y")
        # self.label_timeid.text = datetime.now().strftime("%H:%M:%S")
        # self.event_time_updaaate = Clock.schedule_interval(
        #                     self.update_time, 0.5)


# ----------------------------------------------
# ** ----------------------------------------------:


# * class OptionScreen(Screen): : 
# ** OptionScreen------------------------------------:
class OptionScreen(Screen):
# class Interface(FloatLayout):
    # curent_time_label = ObjectProperty()
    # curent_date_label = ObjectProperty()
    # label_dateid = ObjectProperty(datetime.now().strftime("%d/%m/%Y"))
    # label_timeid = ObjectProperty(datetime.now().strftime("%H:%M:%S"))
    info = StringProperty()

# ----------------------------------------------
# ** def __init__(self, **kwargs): : 
    # def __init__(self, **kwargs):
    #     super(SharpScreen, self).__init__(**kwargs)
        # self.curent_time_label.text = datetime.now().strftime("%d/%m/%Y")
        # self.curent_date_label.text = datetime.now().strftime("%H:%M:%S")
        # self.label_dateid.text = datetime.now().strftime("%d/%m/%Y")
        # self.label_timeid.text = datetime.now().strftime("%H:%M:%S")
        # self.event_time_updaaate = Clock.schedule_interval(
        #                     self.update_time, 0.5)


# ----------------------------------------------
# ** ----------------------------------------------:


# * class TochilMenuApp(App): 
# ** ------TochilMenuApp-----------------------:
class TochilMenuApp(App):

# ** def build(self): : 
    def build(self):
        root_widget = Interface()
        # root_widget = SharpScreen()
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
