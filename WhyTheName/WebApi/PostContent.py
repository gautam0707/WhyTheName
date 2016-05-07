from WhyTheName.ORMClasses.BasicContent import Content
from mongoengine import connect

def AddPost(content):
    connect('whyTheNameInstance',host='127.0.0.1',port=27017,username='admin',password='whyapassword')


