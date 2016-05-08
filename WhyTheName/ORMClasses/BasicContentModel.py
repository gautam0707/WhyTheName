from mongoengine import *


class Content(Document):
    searchText = StringField(max_length=20)
    whyTheName = StringField(max_length=300)
