#! /usr/bin/env python
# -*- encoding: utf-8 -*-

from textual.app import App, ComposeResult
from textual.containers import Vertical, Container
from textual.screen import Screen
from textual.widgets import Static, Input, Button

from ...core.engines import BaseEngine


class MainScreen(Screen):
    """主界面，选择游戏选项"""

    name = "main"

    def compose(self) -> ComposeResult:
        with Vertical(id="main-container", classes="container"):
            yield Static("欢迎来到 三国杀 模拟器", id="game-info")
            yield Button("开始游戏", id="start-game")

    def on_mount(self) -> None:
        self.main_container = self.get_widget_by_id("main-container")
        self.main_container.border_title = "[ 三 国 杀 模 拟 器 ]"

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.notify(f'{event.button} button pressed')


class SgsCliApp(App):
    CSS = """
    .container {
        height: 1fr; 
        border: solid green;
        border-title-color: white;
        /* border-title-background: black; */
        border-title-align: center;
        padding: 1;
    }
    """

    BINDINGS = [
        ("ctrl+q", "quit", "Quit"),
    ]

    def __init__(self, engine: BaseEngine):
        super().__init__()

        self.engine = engine

    def on_mount(self) -> None:
        self.push_screen(MainScreen())


class SgsCliAppLegacy(App):
    CSS = """
    #main-area {
        height: 1fr; 
        border: solid green;
        border-title-color: white;
        /* border-title-background: black; */
        border-title-align: center;
        padding: 1;
    }
    #input-line {
        height: 5;
        padding: 0 1;
        background: #1e1e1e;
        border-top: wide #555;
    }
    #prompt {
        dock: left;
        width: 4;
        height: 3;
        content-align: left middle;
        color: #0f0;
    }
    #command-input {
        height: 3;
        padding-left: 0;
        background: #1e1e1e;
        color: #fff;
        border: blank;
    }
    """

    BINDINGS = [
        ("ctrl+q", "quit", "Quit"),
    ]

    def __init__(self, engine: BaseEngine):
        super().__init__()

        self.engine = engine

    def compose(self) -> ComposeResult:
        with Vertical(id="main-container"):
            yield Static("Welcome to Vim-like Textual App\nUse commands like: echo <text>, clear, help", id="main-area")
            with Container(id="input-line"):
                yield Static(">>>", id="prompt")
                yield Input(placeholder="输入命令 (help获取帮助)", id="command-input")

    def on_mount(self) -> None:
        self.main_area = self.get_widget_by_id("main-area")
        self.main_area.border_title = "[ 三 国 杀 模 拟 器 ]"
        self.command_input = self.get_widget_by_id("command-input")
        self.command_input.focus()

    def on_input_changed(self, event: Input.Changed) -> None:
        self.command_input.value = event.value

    def on_input_submitted(self, event: Input.Submitted) -> None:
        cmd = event.value.strip()
        self.handle_command(cmd)
        self.command_input.value = ""

    def handle_command(self, cmd: str) -> None:
        if not cmd:
            return

        output = ""

        if cmd == "help":
            output = "Available commands:\n  echo <text>\n  clear\n  exit\n  help"
        elif cmd.startswith("echo "):
            output = cmd[5:]
        elif cmd == "clear":
            self.main_area.content = ""
            return
        elif cmd in ("exit", "quit"):
            self.action_quit()
        else:
            output = f"Unknown command: {cmd}\nType 'help' for available commands."

        # Append new input to main area
        current = self.main_area.content
        new_content = f"{current}\n$ {cmd}\n{output}"
        self.main_area.content = new_content
