@echo off
set objshell = createobject("wscript.shell")
objshell.run "FLASHCopy.cmd",vbhide

start python3 cli.py