from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDFillRoundFlatButton
from kivy.core.window import Window
from kivy.uix.carousel import Carousel
from kivy.uix.image import AsyncImage
from kivy.lang import Builder

import pyrebase
import random

Email_Box = '''
MDTextField:
    hint_text: 'Enter email'
    helper_text: 'example@gmail.com'
    helper_text_mode: 'on_focus'
    pos_hint: {'center_x': 0.5, 'center_y': 0.4}
    size_hint_x: None
    width: 250
'''
Password_Box = '''
MDTextField:
    hint_text: 'Password'
    pos_hint: {'center_x': 0.5, 'center_y': 0.3}
    size_hint_x: None
    width: 250
'''
Password_Check_Box = '''
MDTextField:
    hint_text: 'Repeat password'
    pos_hint: {'center_x': 0.5, 'center_y': 0.2}
    size_hint_x: None
    width: 250
'''

Image = '''
MDBoxLayout:
    Image:
        source: 'first_image.png'
        allow_stretch: False
        keep_ratio: True
        size_hint_y: None
        height: dp(200)
        pos_hint: {'center_x': 0.5, 'center_y': 0.7}
'''

Text1 = '''
Screen:
    FloatLayout:
        MDLabel:
            text: 'Get mentorship im one click!'
            font_style: 'H6'
            theme_text_color: 'Custom'
            text_color: (0, 0, 0, 1)
            pos_hint: {'x': 0.08, 'y': -0.1}
'''
Text2 = '''
Screen:
    FloatLayout:
        MDLabel:
            text: "Find yourself a friend, mentor, tutor"
            font_style: 'Subtitle1'
            theme_text_color: 'Secondary'
            text_color: (0, 0, 0, 1)
            pos_hint: {'x': 0.08, 'y': -0.2}
'''

Icon = '''
MDIconButton:
    icon: 'man.jpg'
    allow_stretch: False
    keep_ratio: True
    user_font_size: "90sp"
    pos_hint: {'center_x': 0.5, 'center_y': 0.88}

'''

Name_Box = """
MDTextField:
    hint_text: 'Enter nick'
    helper_text_mode: 'on_focus'
    pos_hint: {'center_x': 0.5, 'center_y': 0.7}
    size_hint_x: None
    width: 250
"""

Info_Box = """
MDTextFieldRect:
    hint_text: 'Tell about yourself'
    helper_text_mode: 'on_focus'
    pos_hint: {'center_x': 0.5, 'center_y': 0.6}
    size_hint: 0.85, None
    height: "40dp"
"""

Check_Boxes = """
MDFloatLayout:
    MDCheckbox:
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        size_hint: 0.1, 0.1
        on_active: app.check("program", self.active)
    MDLabel:
        text: "Programming"
        pos_hint: {'center_x': 0.6, 'center_y': 0.5}
    MDCheckbox:
        pos_hint: {'center_x': 0.9, 'center_y': 0.5}
        size_hint: 0.1, 0.1
        on_active: app.check("draw", self.active)
    MDLabel:
        text: "Drawing"
        pos_hint: {'center_x': 1.1, 'center_y': 0.5}

    MDCheckbox:
        pos_hint: {'center_x': 0.5, 'center_y': 0.4}
        size_hint: 0.1, 0.1
        on_active: app.check("math", self.active)
    MDLabel:
        text: "Math"
        pos_hint: {'center_x': 0.6, 'center_y': 0.4}
    MDCheckbox:
        pos_hint: {'center_x': 0.9, 'center_y': 0.4}
        size_hint: 0.1, 0.1
        on_active: app.check("art", self.active)
    MDLabel:
        text: "Art"
        pos_hint: {'center_x': 1.1, 'center_y': 0.4}

    MDCheckbox:
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        size_hint: 0.1, 0.1
        on_active: app.check("languages", self.active)
    MDLabel:
        text: "Languages"
        pos_hint: {'center_x': 0.6, 'center_y': 0.3}
    MDCheckbox:
        pos_hint: {'center_x': 0.9, 'center_y': 0.3}
        size_hint: 0.1, 0.1
        on_active: app.check("hand work", self.active)
    MDLabel:
        text: "Hand work"
        pos_hint: {'center_x': 1.1, 'center_y': 0.3}

    MDCheckbox:
        pos_hint: {'center_x': 0.5, 'center_y': 0.2}
        size_hint: 0.1, 0.1
        on_active: app.check("music", self.active)
    MDLabel:
        text: "Music"
        pos_hint: {'center_x': 0.6, 'center_y': 0.2}
"""

Main_menu = '''
Screen:
    MDNavigationLayout:
        ScreenManager:
            Screen:
                MDBoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: "Explore"
                        anchor_title: 'center'
                        specific_text_color: 0, 0, 0, 1
                        md_bg_color: 1, 1, 1, 1
                        left_action_items: [['man.jpg', lambda x: nav_drawer.set_state("open")]]
                        right_action_items: [["bell", lambda x: app.notifications()]]
                        background_color: (0, 0, 0, 1)
                    Widget:
                    MDToolbar:
                        elevation: 10
                        md_bg_color: 15 / 255, 4 / 255, 76 / 255, 1
                        type: 'bottom'
                        left_action_items: [['home', lambda x: app.home()], ["message", lambda x: app.message()]]
                        right_action_items: [['flag', lambda x: app.flag()], ['cog', lambda x: app.settings()]]
        MDNavigationDrawer:
            id: nav_drawer
'''
Card = '''
MDScreen:
    MDCard:
        orientation: "vertical"
        padding: "8dp"
        size_hint: None, None
        size: "280dp", "350.dp"
        pos_hint: {"center_x": .5, "center_y": .5}
        MDList:
            id: card_name
'''


class StudyMate(MDApp):
    def random_key(self):
        num = random.randint(0, 1000000)
        if num in self.lst_users:
            self.random_key()
        else:
            return num
    firebaseConfig = {
        'apiKey': "AIzaSyAvcw65aeiGDMuSqbDjREQJQ0Ldc6dWq6o",
        'authDomain': "kivy-53b4a.firebaseapp.com",
        'databaseURL': "https://kivy-53b4a-default-rtdb.firebaseio.com/",
        'projectId': "kivy-53b4a",
        'storageBucket': "kivy-53b4a.appspot.com",
        'messagingSenderId': "685502265511",
        'appId': "1:685502265511:web:da28a9310a174049930382",
        'measurementId': "G-154Q4WN8KC"
    }

    lst_users = []
    lst_mail = []
    lst_password = []

    firebase = pyrebase.initialize_app(firebaseConfig)
    db = firebase.database()
    users = db.child("users").get()
    for user in users.each():
        lst_users.append(user.key())

    for i in range(len(lst_users)):
        mails = db.child("users").child(lst_users[i]).child("gmail").get()
        lst_mail.append(mails.val())
        mails = db.child("users").child(lst_users[i]).child("password").get()
        lst_password.append(mails.val())

    def isvalid(self, mail, password1, password2):
        requirements = {1: lambda x: '@' in x and '.' in x,
                        2: lambda x: len(x) > 7,
                        3: lambda x, y: x == y}
        return all([requirements[1](mail), requirements[2](password1), requirements[3](password1, password2)])

    def build(self):
        Window.clearcolor = (197 / 255, 197 / 255, 197 / 255, 1)
        Window.size = (300, 500)
        self.theme_cls.primary_palette = 'Indigo'
        self.screen = MDScreen()
        self.screen.add_widget(Builder.load_string(Image))
        self.screen.add_widget(Builder.load_string(Text1))
        self.screen.add_widget(Builder.load_string(Text2))
        first_button = MDFillRoundFlatButton(text="Let's get started!",
                                             pos_hint={'center_x': 0.5, 'center_y': 0.1},
                                             on_release=self.First_Button)
        self.screen.add_widget(first_button)

        return self.screen

    def First_Button(self, *args):
        self.screen.clear_widgets()
        return self.Sign_Up_Menu()

    def Sign_Up_Menu(self):
        sign_button = MDFillRoundFlatButton(text='Sign up', pos_hint={'center_x': 0.3, 'center_y': 0.1},
                                            on_release=self.Sign_Up_Button)
        log_button = MDFillRoundFlatButton(text='Log In', pos_hint={'center_x': 0.7, 'center_y': 0.1},
                                           on_release=self.Log_In_Button1,
                                           text_color=(200 / 255, 200 / 255, 200 / 255, 1), )
        self.user_gmail_box = Builder.load_string(Email_Box)
        self.user_password_box = Builder.load_string(Password_Box)
        self.user_password_check_box = Builder.load_string(Password_Check_Box)
        self.screen.add_widget(Builder.load_string(Image))
        self.screen.add_widget(self.user_gmail_box)
        self.screen.add_widget(self.user_password_box)
        self.screen.add_widget(self.user_password_check_box)
        self.screen.add_widget(sign_button)
        self.screen.add_widget(log_button)
        return self.screen

    def Log_In_Menu(self):
        self.user_gmail_box = Builder.load_string(Email_Box)
        self.user_password_box = Builder.load_string(Password_Box)
        sign_button = MDFillRoundFlatButton(text='Sign up', pos_hint={'center_x': 0.3, 'center_y': 0.1},
                                            on_release=self.First_Button,
                                            text_color=(200 / 255, 200 / 255, 200 / 255, 1))
        log_button = MDFillRoundFlatButton(text='Log In', pos_hint={'center_x': 0.7, 'center_y': 0.1},
                                           on_release=self.Log_In_Button2)
        self.screen.add_widget(Builder.load_string(Image))
        self.screen.add_widget(self.user_gmail_box)
        self.screen.add_widget(self.user_password_box)
        self.screen.add_widget(log_button)
        self.screen.add_widget(sign_button)
        return self.screen

    def Sign_Up_Button(self, *args):
        dict = {"gmail": self.user_gmail_box.text, "password":self.user_password_box.text}
        if self.isvalid(self.user_gmail_box.text, self.user_password_box.text, self.user_password_check_box.text):
            self.db.child("users").child(str(self.random_key())).set(dict)
            self.screen.clear_widgets()
            return self.Person_Menu()
        else:
            dialog = MDDialog(text='Invalid email or password')
            dialog.open()

    def Log_In_Button1(self, *args):
        self.screen.clear_widgets()
        return self.Log_In_Menu()

    def Log_In_Button2(self, *args):
        if self.user_gmail_box.text in self.lst_mail:
            num = self.lst_mail.index(self.user_gmail_box.text)
            if self.user_password_box.text == self.lst_password[num]:
                self.screen.clear_widgets()
                return self.Main_Menu()
            else:
                dialog = MDDialog(text='Invalid password')
                dialog.open()
        else:
            dialog = MDDialog(text='Invalid email')
            dialog.open()

    def Person_Menu(self):
        self.screen.clear_widgets()

        image = Builder.load_string(Icon)
        self.screen.add_widget(image)

        self.nick = Builder.load_string(Name_Box)
        self.screen.add_widget(self.nick)

        self.info = Builder.load_string(Info_Box)
        self.screen.add_widget(self.info)

        check_box = Builder.load_string(Check_Boxes)
        self.screen.add_widget(check_box)

        save_button = MDFillRoundFlatButton(text="save",
                                            pos_hint={'center_x': 0.5, 'center_y': 0.1},
                                            on_release=self.show_data)
        self.screen.add_widget(save_button)
        return self.screen

    def check(self, id, active):
        if active:
            print(id)

    def show_data(self, obj):
        if self.nick.text is "":
            check_text = "Please, enter your username"
            close_button = MDFillRoundFlatButton(text="Close", on_release=self.close_dialog)
            self.dialog = MDDialog(title="Error", text=check_text, size_hint=(0.8, 1), buttons=[close_button])
        elif self.info.text is "":
            check_text = "Please, tell about yourself"
            close_button = MDFillRoundFlatButton(text="Close", on_release=self.close_dialog)
            self.dialog = MDDialog(title="Error", text=check_text, size_hint=(0.8, 1), buttons=[close_button])
        else:
            check_text = "Thanks , good luck"
            close_button = MDFillRoundFlatButton(text="Close", on_press=self.Main_Menu, on_release=self.close_dialog)
            self.dialog = MDDialog(title="Good", text=check_text, size_hint=(0.8, 1), buttons=[close_button])
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()

    def Main_Menu(self, *args):
        self.screen.clear_widgets()

        carousel = Carousel(direction='right')
        images = {'3.png': 'Human', '4.png': 'Some Dude', '5.png': 'Person'}
        for i, j in images.items():
            card = Builder.load_string(Card)
            card.add_widget(AsyncImage(source=i, allow_stretch=True))
            card.ids.card_name.add_widget(MDLabel(text=j, font_style='H5',
                                                  pos_hint={'center_x': 0.5, 'center_y': 0.5}))
            carousel.add_widget(card)
        self.screen.add_widget(carousel)
        self.screen.add_widget(Builder.load_string(Main_menu))
        return self.screen

    def home(self):
        print('home')

    def message(self):
        print('message')

    def settings(self):
        print('settings')

    def flag(self):
        print('flag')

    def notifications(self):
        print('notifications')


if __name__ == '__main__':
    app = StudyMate()
    app.run()
