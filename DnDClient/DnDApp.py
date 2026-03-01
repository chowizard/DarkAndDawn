#-*- coding: utf-8 -*-

from typing import override

from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Header, Footer, Static, RichLog
from textual.binding import Binding
from textual.screen import Screen

from Utilities.Logger import Logger
from Game.Game import Game

class GameScreen(Screen):
    """
    Screen for Game Output
    """
    BINDINGS = [Binding("escape", "app.toggle_mode", "System Mode")]

    @override
    def compose(self) -> ComposeResult:
        yield Header()
        yield Container(Static("Game Screen - Placeholder for Game Output", id="game_output"))
        yield Footer()

class SystemScreen(Screen):
    """
    Screen for System/Debug Output (Logs)
    """
    BINDINGS = [Binding("escape", "app.toggle_mode", "Game Mode")]

    @override
    def compose(self) -> ComposeResult:
        yield Header()
        yield RichLog(highlight=True, markup=True, id="system_log")
        yield Footer()

    @override
    def on_mount(self) -> None:
        """
        Called when screen is mounted.
        """
        # Connect Logger to this RichLog
        logToWidget = self.query_one("#system_log", RichLog)

        # Define a handler that writes to the widget
        def LogToWidget(message: str):
            logToWidget.write(message)

        # Initialize Logger with this handler
        # Note: In a real app, we might want to queue logs if screen isn't ready,
        # but for now we hook it up here.
        Logger.Initialize(LogToWidget)
        Logger.Log("System Screen Initialized. Logger connected.")

class DnDApp(App):
    """
    DarkAndDawn Client Application
    """
    CSS = """
    Screen
    {
        layout: vertical;
    }
    #game_output
    {
        height: 1fr;
        border: solid green;
    }
    #system_log
    {
        height: 1fr;
        border: solid yellow;
    }
    """

    SCREENS = {
        "game": GameScreen,
        "system": SystemScreen,
    }

    BINDINGS = [
        Binding("escape", "toggle_mode", "Switch Mode"),
        Binding("q", "quit", "Quit"),
    ]

    @override
    def on_mount(self) -> None:
        """
        App start
        """
        self.PushScreen("game")
        # Initialize Game Singleton (will remain as Singleton for now per plan)
        Game.Singleton().Initialize()

    @override
    def action_toggle_mode(self) -> None:
        """
        Toggle between Game and System screens.
        """
        current = self.screen
        if isinstance(current, GameScreen):
            self.SwitchScreen("system")
        else:
            self.SwitchScreen("game")

    def PushScreen(self, screen_name: str) -> None:
        """
        Wrapper to push screen (PascalCase alias)
        """
        self.push_screen(screen_name)

    def SwitchScreen(self, screen_name: str) -> None:
        """
        Wrapper to switch screen (PascalCase alias)
        """
        self.switch_screen(screen_name)
