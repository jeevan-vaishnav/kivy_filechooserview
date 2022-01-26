from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.filechooser import FileChooserIconView

Builder.load_file('ui.kv')


class MyLayout(Widget):

    def selected(self, filename):
        try:
            self.ids.my_image_id.source = filename[0]
        except:
            pass


class AwsomeApp(App):
    def build(self):
        # Window.clearcolor = (1, 1, 1, 1)
        return MyLayout()


if __name__ == "__main__":
    AwsomeApp().run()
