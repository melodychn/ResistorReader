#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 12:17:42 2019

@author: melodychen
"""

class colorIdentifier:
    from clarifai.rest import ClarifaiApp
    from clarifai.rest import Image as ClImage
    def __init__(self,path):
        self.path = path
        self.app = ClarifaiApp(api_key='3fbee996b23d4094b14d0ffe2b8f96e2')
        self.model = self.app.models.get('color')
        self.response = self.model.predict_by_filename(self.path)
        self.colorlist = []
    def convertToRGB(self, hex):
        h = hex.lstrip('#')
        return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
    def setList(self):
        colors = self.response['outputs'][0]['data']['colors']
        length = len(colors)
        for x in range(length):
            rgb_tup = self.convertToRGB(colors[x]['raw_hex'])
            processed_tup=(rgb_tup,colors[x]['value'])
            self.colorlist.append(processed_tup)
    def getRGB(self):
        self.setList()
        #convert to our own dictionary
        return self.colorlist
    def getDominant(self):
        self.setList()
        maxV = 0;
        maxC = self.colorlist[0][0]
        for x in range(len(self.colorlist)):
            current = self.colorlist[x][1]
            if(current>maxV):
               maxV=current
               maxC=self.colorlist[x][0]
        return maxC
            



    
