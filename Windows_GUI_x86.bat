@echo off
set objshell = createobject("wscript.shell")
objshell.run "FLASHCopy.cmd",vbhide

start main_gui.pyw