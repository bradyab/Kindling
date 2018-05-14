# exec(open("gui.py").read(), globals())
import sys

exec(open('gatherimages.py').read())

sys.argv = ['gui.py','train']
exec(open('gui.py').read())

sys.argv = ['gui.py','predict']
exec(open('gui.py').read())