from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen


class ClickWindow(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
class ClickerApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(ClickWindow(name="click_window"))

        return sm


ClickerApp().run()