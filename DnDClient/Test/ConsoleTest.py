#-*- coding: utf-8 -*-

'''
Created on 2024. 1. 10.

@author: chowizard
'''

from textual.app import App, ComposeResult
from textual.widgets import Footer, Header

class TestApp(App):
    """
    Textual Test App
    """

    BINDINGS = [("d", "toggle-dark", "Toggle dark mode")]


    def compose(self) -> ComposeResult:
        """
        Create child widget for the app
        """
        yield Header()
        yield Footer()

    def action_toggle_dark(self) -> None:
        """
        Action toggle theme
        """
        return super().action_toggle_dark()


if __name__ == "__main__":
    app = TestApp()
    app.run()
