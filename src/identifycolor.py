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
        app = ClarifaiApp(api_key='c74551e84dce4f2aa6528c43e24dc050')
        model = app.models.get('color')
        response = model.predict_by_filename(path)
        
    def convertToRGB(self, hex):
        h = hex.lstrip('#')
        return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
    def getRGB(self):
        #convert to our own dictionary
        colors = response['outputs'][0]['data']['colors']
        length = len(colors)
        for x in range(length):
            rgb_tup = convertToRGB(colors[x]['raw_hex'])
            processed_tup=(rgb_tup,colors[x]['value'])
            colorlist.append(processed_tup)
        return colorlist



    