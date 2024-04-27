from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

from pytube import YouTube

class main_app(MDApp):
        
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10)
        label=MDLabel(text="welcome to Tanuj 's app ",font_size=30, halign="justify" )
        text_input = TextInput(text='', multiline=False, font_size=16,size_hint_y=None,halign="center", height=40)
        # Create a button
        button = Button(text='Download video!',size_hint_y=None,height=40, background_color=(0.2, 0.6, 1, 1),valign="center")

        # Bind the button to a function
        button.bind(on_press=self.on_button_press)

        # Add the button to the layout
        layout.add_widget(label)
        layout.add_widget(text_input)
        layout.add_widget(button)

        return layout

    def on_button_press(self, instance):
        print("Button pressed!")
        self.Video_download()
    # def build(self):
    #     btn = Button(text ="Download video",font_size ="20sp",background_color =(1, 1, 1, 1),color =(1, 1, 1, 1), size =(32, 32)
    #                  )
    #     btn.bind(on_press = self.callback)
    #     return btn   
    # def callback(self, event):
    #     print("button pressed")
    #     print('Yoooo !!!!!!!!!!!')
    def Video_download(self):
        yt=YouTube("https://www.youtube.com/watch?v=PJWemSzExXs&list=RDkJOGN-w12Qo&index=2")
        print(yt)
        print(" Title -> ", yt.title)
        print(" views -> ", yt.views)
        yd=yt.streams.get_highest_resolution()
        
        return "done"
    
    
	
	# callbackis the function tells which when button pressed
	
        # yd.download(r'C:\Users\Dell\Videos\videos')  
    
    # def btn_clk(self):
    #     self.lbl.text = "You have been pressed"
    
if __name__ == "__main__":
    main_app().run()
    