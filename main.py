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
from datetime import date, datetime, timedelta 
from random import randrange


# ----------------------------------------------
# * modul global id values:
# print("-------modul global id-----------")
main_menu_timer_label = False 
progress_menu_start_progress = False 
# ----------------------------------------------
# * def start_sharpening : 
def start_sharpening(): 
    if not progress_menu_start_progress:
        print ("No Function to run sharpening Progress")
        return
    progress_menu_start_progress()
    
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
        # info = StringProperty()
        # global main_menu_timer_label
        # main_menu_timer_label = self.label_timerid
        self.event_time_update = Clock.schedule_interval(
                            self.update_time, 0.5)


# ----------------------------------------------
# ** def update_time(self): : 
    def update_time(self, cb):
        # only after StringProperty() in init class
        self.label_dateid.text = datetime.now().strftime("%d/%m/%Y")
        self.label_timeid.text = datetime.now().strftime("%H:%M:%S")
        global main_menu_timer_label
        if not main_menu_timer_label:
          main_menu_timer_label = self.label_timerid


# ----------------------------------------------
# ** def do_action(self): : 
    def do_action(self):
        self.label_dateid.text = datetime.now().strftime("%d/%m/%Y")
        self.label_timeid.text = datetime.now().strftime("%H:%M:%S")
        main_menu_timer_label.text = datetime.now().strftime("%d/%m/%Y")
        # self.info = "hello world"
        # print("Time = ", time.time())
        # print("date = ", datetime.now().strftime("%d/%m/%Y"))
        # print("Time = ", datetime.now().strftime("%H:%M:%S"))


# ----------------------------------------------
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
# ** def Start : 
    def start(self): 
        start_sharpening()
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
        self.progress_value = 0
        self.event_progress = 0
        self.event_time_update = Clock.schedule_interval(
                            self.update_time, 0.5)
        global progress_menu_start_progress 
        progress_menu_start_progress = self.progressbar_Start
        # self.event_progress = Clock.schedule_interval(
        #                     self.progressbar_Update, 0.01)

# ----------------------------------------------
# ** def update_time(self): : 
    def update_time(self, cb):
        # only after StringProperty() in init class
        self.label_dateid.text = datetime.now().strftime("%d/%m/%Y")
        self.label_timeid.text = datetime.now().strftime("%H:%M:%S")
        # self.progressbar_Update()


# ----------------------------------------------
# ----------------------------------------------
# ** def progressbar_Update(self): : 
    def progressbar_Update(self, cb):
        if self.progress_value >=100 : self.progressbar_Finish()
        # self.progress_value += randrange(0, 3)
        self.progress_value += 0.1
        self.progressbarid.value = self.progress_value
        # only after StringProperty() in init class
        # self.label_timeid.text = datetime.now().strftime("%H:%M:%S")


# ----------------------------------------------
# ----------------------------------------------
# ** def progressbar_Finish : 
    def progressbar_Finish(self): 
        self.finishButton.background_color = [1, 200, 1, 1]
        self.finishButton.text = "Finished"
        Clock.unschedule(self.progressbar_Update)


#  ----------------------------------------------:
# ** def progressbar_Start : 
    def progressbar_Start(self): 
        self.finishButton.background_color = [200, 1, 1, 1]
        self.finishButton.text = "Cancel"
        self.progress_value = 0
        if self.event_progress : Clock.unschedule(self.progressbar_Update)
        self.event_progress = Clock.schedule_interval(
                            self.progressbar_Update, 0.01)


#  ----------------------------------------------:
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
    def __init__(self, **kwargs):
        super(TimerScreen, self).__init__(**kwargs)
        self.runing_Timer = None
        self.timerEnd = None
        # ----------------------------------------------


# ** def update_Timer(self, cb): : 
    def update_Timer(self, cb):
        if not self.timerEnd : return print ("timer no started error")
        # print(( self.timerEnd).strftime("%d/%m/%Y %H:%M:%S"))
        # print(( self.timerEnd - datetime.now()).strftime("%d/%m/%Y %H:%M:%S"))
        # self.timerEnd - datetime.now())
        delta =  self.timerEnd - datetime.now()
        # print(str(delta).split("."))
        # print(str(delta).split(".")[0])
        if (delta.seconds < 1) : self.stop_Timer()
        main_menu_timer_label.text = str(delta).split(".")[0]
        # ----------------------------------------------


# ** start_timer(self, d_hours=0, d_minutes=0, d_seconds=0): : 
    def start_timer(self, d_hours=0, d_minutes=0, d_seconds=0):
        self.timerEnd =     datetime.now() + timedelta(
                                  # days=50,
                                  hours=d_hours,
                                  minutes=d_minutes,
                                  seconds=d_seconds,
                                  # microseconds=10,
                                  # milliseconds=29000,
                                  # weeks=2
                              )
        if self.runing_Timer: Clock.unschedule(self.update_Timer) 
        self.runing_Timer = Clock.schedule_interval(
                                self.update_Timer, 0.5)
        # ----------------------------------------------


# ** def stop_Timer : 
    def stop_Timer(self): 
        Clock.unschedule(self.update_Timer) 
        self.runing_Timer = False
        main_menu_timer_label.text = '--'


# ----------------------------------------------
# ** def do_action(self): : 
# ----------------------------------------------
    def do_action(self):
        main_menu_timer_label.text = datetime.now().strftime("%d/%m/%Y")
        # ----------------------------------------------
# ** defs : 
    def isTimerRuning(self):
        pass


# ----------------------------------------------
# ** ----------------------------------------------:


# * class OptionScreen(Screen): : 
# ** OptionScreen------------------------------------:
class OptionScreen(Screen):
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
        return root_widget


# ----------------------------------------------
# ** ----------------------------------------------:
# * def main(argv): : 
# ----------------------------------------------
def main(argv):
    print (argv)
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
