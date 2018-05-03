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


if api.authverif() == True:
        print("Gathering Data on your matches...")
        # print(api.get_self())
        search =  api.get_recs_v2()
        ppl= search['data']['results']
        # print(feat.get_photos(ppl[0]['user']['photos'].key()))
        # pics = feat.get_photos(ppl[0])
        pics = feat.get_photos(ppl[0]['user'])

        for i in pics:
            file = urllib.request.urlopen(i)
            img = Image.open(file)
            img.save("./images/"+str(time()),'JPEG')
            # img
            # img.show()

        # for x in ppl:
        #     pics = x
        #     pics = feat.get_photos()
        #     for i in pics:
        #         file = urllib.request.urlopen(i)
        #         img = Image.open(file)

            



else:
        print("Something went wrong. You were not authorized.")