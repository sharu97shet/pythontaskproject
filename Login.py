from .models import User,Task
from django.db.models import Q

def registerlogin(email,password):

    if email!='':
     
        userlogin=User.objects.filter(
                    Q(Email=email) & Q(Password=password))

        return userlogin

