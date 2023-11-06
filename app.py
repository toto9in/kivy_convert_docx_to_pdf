from kivy.app import App
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from pdf_convert import convert_to_pdf


class Convert2Pdf(App):
    def build(self):
        """Builds the app"""
        Window.clearcolor = (1, 0, 0, 1) # set window color to red
        Window.bind(on_dropfile=self.on_file_drop)
        layout = BoxLayout(orientation='vertical')
        title = Label(text='Convert Docx to PDF', font_size=40, size_hint=(1, 0.5))
        layout.add_widget(title)
        subtitle = Label(text='Drag and drop archive', font_size=30, size_hint=(1, 0.5))
        layout.add_widget(subtitle)
        return layout

    def show_popup(self, text):
        """Shows a popup with a message"""
        box = BoxLayout(orientation='vertical')
        box.add_widget(Label(text=text))
        mybutton = Button(text='Close')
        box.add_widget(mybutton)
        popup = Popup(title='Warning', content=box, size_hint=(None, None), size=(400, 400))
        popup.separator_color = (0, 0, 0, 1)
        mybutton.bind(on_press=popup.dismiss)
        popup.open()
       
    def on_file_drop(self, window, filename):
        """Called when a file is dropped on the app window"""
        filename = filename.decode("utf-8")
        convertion = convert_to_pdf(filename)
        if convertion:
            self.show_popup('File converted successfully')
        else:
            self.show_popup('Error converting file')
        return

    
def main():
    Convert2Pdf().run()

if __name__ == '__main__':
    main()
