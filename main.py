import json

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen



player_data = {
    "score": 0,
    "pover": 1
}

def read_data():
    global player_data
    try:
        with open("play.json", "r", encoding="utf-8") as file:
            player_data = json.load(file)
    except:
        print("невдача")


def save_data():
    global player_data
    try:
        with open("play.json", "w", encoding="utf-8") as file:
            json.dump(player_data, file, indent=4, ensure_ascii=True)
    except:
        print("невдача")




users = {
    'user1': 'password',
    'user2': 'qwerty',
    'admin': 'secret'

}

class LoginWindow(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

    def go_login(self):
        username_input = input("Введіть логін")
        password_input = input("Введіть пароль")
        if username_input in users:
            if password_input in users:
                self.manager.current = "click_window"
            else:
                print("неправельний пароль")
        else:
            print("неправельний логін")










class ClickWindow(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)


    def on_enter(self, *args):
        read_data()
        self.ids.score_lbl.text = str(player_data['score'])

    def click(self):
        player_data['score'] += player_data['pover']
        self.ids.score_lbl.text = str(player_data['score'])
        self.ids.ball_img.size_hint = (1,1)
        save_data()



    def unclick(self):
        self.ids.ball_img.size_hint = (0.25, 0.5)

    def go_to_shop(self):
        self.manager.current = "shop"



class ShopWindow(Screen):
    def __init__(self,**kw):
        super(). __init__(**kw)


    def go_to_exit(self):
        self.manager.current = "click_window"

    def buy(self,price,bonus):
        read_data()
        if player_data['score'] >= price:
            player_data['score']-= price
            player_data['pover'] += bonus
        else:
            print("не достатньо грошей")
        save_data()



class ClickerApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(ClickWindow(name="click_window"))
        sm.add_widget(ShopWindow(name="shop"))
        return sm


ClickerApp().run()