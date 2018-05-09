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

if api.authverif() == True:
        print("Gathering Data on your matches...")
        # print(api.get_self())
        y = 1
        repeats = []
        while y<500:

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
            
            y = y + 1

            



else:
        print("Something went wrong. You were not authorized.")