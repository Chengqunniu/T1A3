from rich.console import Console
from rich.style import Style
from rich.text import Text


class text:
    base_style = Style(color='cyan', blink=True,)

  
    def __init__(self, content):
        self.content = content


    def color_input(self):
        self.color()
        self.collect_input()


    def color(self):
        console = Console()
        style_text = Text(self.content)
        style_text.stylize(self.base_style)     
        console.print(style_text, justify='center')


    def collect_input(self):
        input()


class display_message(text):
    base_style = Style(color='purple')


    def __init__(self, message):
        super().__init__(message)
        self.message = message
