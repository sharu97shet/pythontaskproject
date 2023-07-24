from rest_framework import serializers
from taskApp.models import Blog,Task,User
from rest_framework.response import Response
import re


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields ='__all__'
        # fields = ('BlogName',
        #           'city')
        
   