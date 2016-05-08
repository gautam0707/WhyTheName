from Serializers.BasicContentModelSerializer import ContentSerializer
from WhyTheName.ORMClasses.BasicContentModel import *


def add_post():
    result = Content(searchText="Hyderabad", whyTheName="Why The Name")
    return ContentSerializer(result)
