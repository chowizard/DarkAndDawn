#-*- coding: utf-8 -*-

from time import sleep
from rich import print
from rich.console import Console

console = Console(width = 120, height = 50)
console.print([1, 2, 3])
console.print("[blue underline]Look like a link")
console.print(locals())
console.print("FOO", style = "white on blue")
console.log("[LOG] Test log")
console.rule(title = "Line Test", style = "rule.line", align = "left")

console2 = Console(width = 120, height = 50)
console2.print("Another console")
with console2.screen():
    #console2.print("aaa")
    sleep(3)

