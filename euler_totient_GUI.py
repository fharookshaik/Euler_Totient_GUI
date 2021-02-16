from kivy.app import App 
from kivy.uix.floatlayout import FloatLayout
from euler_totient import Euler_totient

class MainWindow(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def on_btn_click(self):
        try:
            if self.ids.input.text != '':
                num = int(self.ids.input.text)
                print('Captured Number : ',num)
                self.ids.input.text = ''
                count, values = Euler_totient(num)
                self.ids.output.text = 'Output:\n\nThe number {} has {} euler totient values.\nValues = {}'.format(num,count,values)


            else:
                print("Input can't be empty")
                self.ids.output.text = "Input can't be empty."
        except Exception as e:
            self.ids.output.text = 'Unexpected Error. Re-run the program.'    

class EulerTotientApp(App):
    def build(self):
        return MainWindow()

if __name__ == '__main__':
    EulerTotientApp().run()