from datetime import date, datetime
from random import random
from time import sleep, time

import os
import config
import tinder_api as api
import features as feat
# import cv2
from PIL import Image
import urllib
from io import StringIO
import config
import json
import foldercount
import progressbar

if api.authverif() == True:
        print("Gathering images from nearby users for training...")
        # print(api.get_self())
        y = 1
        repeats = []

        while foldercount.numfile("./images/") < 1000:

            search =  api.get_recs_v2()
            ppl= search['data']['results']

            for i in range(len(ppl)):
                if foldercount.numfile("./images/") < 1000:
                    break
                else:

                    progressbar.printProgressBar(foldercount.numfile("./images/"), 1000)
                
                if ppl[i]['user']['_id'] in repeats:
                    pass
                else:
                    pics = feat.get_photos(ppl[i]['user'])
                    path = './images/'
                    for j in pics:
                        x = foldercount.numfile(path)+1
                        file = urllib.request.urlopen(j)
                        img = Image.open(file)
                        img.save(path+'userpic'+str(x)+".jpg",'JPEG')
                    repeats.append(ppl[i]['user']['_id'])
            
        print("Gathering images for predictions")

        while foldercount.numfile("./prediction/") < 100:

            search =  api.get_recs_v2()
            ppl= search['data']['results']

            for i in range(len(ppl)):
                
                if ppl[i]['user']['_id'] in repeats:
                    pass
                else:
                    pics = feat.get_photos(ppl[i]['user'])
                    path = './prediction/'
                    for j in pics:
                        x = foldercount.numfile(path)+1
                        file = urllib.request.urlopen(j)
                        img = Image.open(file)
                        img.save(path+'userpic'+str(x)+".jpg",'JPEG')
                    repeats.append(ppl[i]['user']['_id'])

            



else:
        print("Something went wrong. You were not authorized.")