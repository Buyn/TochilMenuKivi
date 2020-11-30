import kivy
kivy.require(kivy.__version__)
from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
        def build(self):
                return Label(text = "Guido Van Rossum", font_size = 90)

def main():
        MyApp().run()

if __name__ == "__main__":
        main()

# main()
