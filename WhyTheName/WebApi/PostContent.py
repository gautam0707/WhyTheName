from WhyTheName.ORMClasses.BasicContentModel import *
from WhyTheName.ORMClasses.BasicContentModelSerializer import ContentSerializer


def add_post():
    result = Content(searchText="Hyderabad", whyTheName="Why The Name")
    return ContentSerializer(result)
