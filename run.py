# exec(open("gui.py").read(), globals())
import sys
from foldercount import numfile

import gui

exec(open('gatherimages.py').read())

train_q = gui.QApplication([])
train_app = gui.App('train')
# Continue training while there are images left in /images
while numfile('./training_data/like') + numfile('./training_data/dislike') < numfile('./images/'):
	train_app.photoChange('./images/')
train_q.quit()

predict_q = gui.QApplication([])
predict_app = gui.App('predict')

# sys.argv = ['gui.py','train']
# exec(open('gui.py').read())

# sys.argv = ['gui.py','predict']
# exec(open('gui.py').read())