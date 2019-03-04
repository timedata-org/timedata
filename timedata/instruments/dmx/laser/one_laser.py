import tkinter as tk
from .toggle_button import ToggleButton
from .dmx_levels import DMXLevels
from .resizable import Resizable


class OneLaser(tk.Frame, Resizable):
    OFF, ON = 'X', 'O'

    def __init__(self, master, text, on_enable=None, **kwds):
        super().__init__(master, **kwds)
        self._on_enable = on_enable

        top = tk.Frame(self)
        top.pack(fill=tk.X, expand=tk.YES)

        enable = ToggleButton(top, self.OFF, self.ON, self.on_enable)

        enable.pack(side=tk.LEFT)
        label = tk.Label(top, text=text, font=('Helvetica', 24))
        label.pack(side=tk.RIGHT)

        self.levels = DMXLevels(self)
        self.levels.pack(fill=tk.BOTH, expand=tk.YES)
        self._init()

    def on_enable(self, text):
        self._on_enable and self._on_enable(text == self.ON)