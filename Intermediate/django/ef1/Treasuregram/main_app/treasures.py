'''
Created on Jun 18, 2019

@author: mrfox
'''

class Treasures:
    '''
    The Treasures class will be used for the index.html
    to use a lot of complex data.
    '''


    def __init__(self, name, value, material, location, img_url):
        '''
        Constructor
        '''
        self.name = name
        self.value = value
        self.material = material
        self.location = location
        self.img_url = img_url

        