from django.shortcuts import render, HttpResponse, redirect
from .models import User,Task,Blog
from datetime import datetime, timedelta
from rest_framework import status
from rest_framework.response import Response

from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from taskApp.serializers import *
from django.db.models import Q
from django.http import JsonResponse
from .Login import *
from django.core.mail import send_mail
from django.conf import settings
import re
import requests
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.

def task(request):
     #return HttpResponse("Hello, world  !")

     return render(request, 'login.html')

def login(request):
     
    return render(request, 'login.html')
 
def register(request):
       
    return render(request, 'Register2.html')


# @api_view(['GET','POST'])
def addblog(request):
       
    if request.method=='GET':
     
      return render(request, 'blogpage.html')

@api_view(['POST'])    
def  ContactView(request):  
    if request.method=='POST': 
        try:
            resdata=request.data
            print(resdata['blog'])
            blogdata=Blog.objects.create(BlogName=resdata['blog'] ,city=resdata['city'])
            Blogserializer=BlogSerializer(blogdata, many=False)
            return JsonResponse("successfully done",safe=False) 
        #     return Response({  
        #             'status':True,
        #             'message':'Success To Do created',
        #             'data':Blogserializer.data
         
         
        #    })

        except Exception as e:
               return HttpResponse(e)      
                
        #     if Blogserializer.is_valid():
        #         #pass
        #         print("lion")
        #         Blogserializer.save()
                
        #         return Response({  
        #         'status':True,
        #         'message':'Success To Do created',
        #         'res':resdata,
        #         'data':Blogserializer.fields
            
            
        #              })
        #     else:
        #         print("else")
             
        #         return Response({  
        #         'status':False,
        #         'message':'wrong',
        #         'data':Blogserializer.error_messages
                
        #         })
   
        # except Exception as e:
        #         return HttpResponse(e)    
    
# class ContactView(APIView):
#     def post(self, request):
#         serializer = BlogSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
def userregister(request):

    if request.method == 'POST':

        firstname = request.POST['username']
        email = request.POST['email']
        mobile = request.POST['mobile']
        password = request.POST['password']

        if not re.search(r"^[A-Za-z0-9]+@[A-Za-z0-9.-]+$", email):

             print(f"The email address {email} is not valid")
             #return False

        existinguserrecord= User.objects.filter(Email=email).count()
        print(f"The email address {email} is  found already in database")
        print(existinguserrecord)
        #return False
    
        if existinguserrecord<1 :
         userrecord = User(
            Name=firstname, Email=email,  MobileNumber=mobile, Password=password )
         userrecord.save()

         ID = userrecord.id

         print('record user insert', ID)

         value=registerlogin(email,password)

         #return HttpResponse( value  )
        
         return redirect('dashboard')
        
        else:

            return HttpResponse( f"The email address {email} is   already there  in database")


    else:

        return HttpResponse(" something went wrong  ")

def profile(request):

    email = request.session.get('email')
    mydata2 = User.objects.filter(Email=email).values()

    #print(mydata2)
    mydata3 = User.objects.get(Email=email)

    logindata={
        'name':mydata3,
        'biodata':mydata2
    }

    return render(request, 'profile.html', logindata)  


def loginusername(request ,email):
    
    email = request.session.get('email')
    mydata2 = User.objects.get(Email=email)

    print(mydata2)

    logindata={
        'name':mydata2
    }

    return render(request, 'taskmenu.html', logindata)  

def useraccount(request):

    email = request.session.get('email')

    mydata2 = User.objects.get(Email=email)
    #return HttpResponse(mydata2)

    Join=Task.objects.select_related('user').filter(Assign=mydata2)
    print(Join)

    Fivrecords=Task.objects.all().filter(Assign=mydata2).order_by('-id')[:5].values_list('TaskName','Date','Status')

    print(Fivrecords)

    print(Join.query)  

    # for j in Join:
    #     temp=j.

    #print(mydata2)

    #print(Join.query)

    #return HttpResponse(temp)

    # depdata=requests.get( 'http://127.0.0.1:8000/empapi/department')

    # print(depdata.json())
    users=Task.objects.all()
    userdetail=[]

    #print(users)
    for i in users:
        userdetail.append(i)

    #print(userdetail)

    #return HttpResponse(users)

    #print(users.count())

    logindata={
        'name':mydata2,
        'taskdata':Join
    }


    return render(request, 'user.html', logindata)  

    return render(request, 'user.html' , {'userstask': users})

      

def tasklist(request):
      
    firstname = request.session.get('email')

    lastname = request.session.get('password')

    loginuserdetails = {
        'fname': firstname,
        'lname': lastname

    }
     
    return render(request, 'tasklist.html', {'loginuserdetails': loginuserdetails})   

def addtask(request):
      
    email = request.session.get('email')

    lastname = request.session.get('password')

    usersrecords=User.objects.all().exclude(Email=email)

    mydata2= User.objects.get(Email=email)
    # allrecords=User.objects.filter(Email=email).get(id)
    
    print(mydata2)

    #print(usersrecords)

    loginuserdetails = {
        'fname':usersrecords
    }
     
    logindata={
        'name':mydata2,
        'assigntouser':usersrecords
    }
    #print('yes',loginuserdetails)

    if request.method == 'POST':

        taskname = request.POST['task']
        taskdate = request.POST['taskdate']
        tasktime = request.POST['tasktime']
        assign = request.POST['assign']
        
        savetask = Task(
            TaskName=taskname, Date=taskdate,  Time=tasktime, Assign=assign ,user=mydata2
                )
        savetask.save()

        print('savetask  insert')

        messages.success(request,  'added successfully! ,'+taskname  )

        return render(request, 'addtask.html', logindata)   

        return HttpResponse("task saved please go to tasklist" )
    
    return render(request, 'addtask.html', logindata)    


   # return render(request, 'addtask.html', {'assigntouser':usersrecords })    


def dashboard(request):

    if request.method == 'POST':

        dict(a=datetime.now(),value='something')

        email = request.POST['email']
        password = request.POST['password']

        request.session['email'] = email
        request.session['password'] = password

        if email!='':
             
            try:
                userlogin = User.objects.filter(
                    Q(Email=email) & Q(Password=password))
                if (userlogin):
                    return redirect('useraccount')
                else:
                    print("not valid")
                    messages.success(request, 'entered email or password didnt matched')
                    return redirect('login')
                    return HttpResponse("not valid")

            except Exception as e:
                return HttpResponse(e)
                pass

        else:

             return HttpResponse ('Not valid')
        

    else:

          return redirect ('login')
    


def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = User.objects.get(Email=email)
        except User.DoesNotExist:
            # Handle the case when the user does not exist
            return HttpResponse("not found")
            return redirect('forgot_password')
        
        # Generate a unique token and save it to the user's profile request.build_absolute_uri(f'/accounts/reset-password/{token}')
        # You can use the built-in `django.contrib.auth.tokens` module for token generation token = 'your_generated_token'

        # Send the password reset email
        token = ''
        reset_link =''
        subject = 'Password Reset'
        message = f'Click the link below to reset your password:\n\n{reset_link}'
        send_mail(subject, message, settings.EMAIL_HOST_USER, ['sharathshet.n@gmail.com'], fail_silently=False)

        return HttpResponse("yesgood")

        return redirect('accounts:forgot_password_done')

    return render(request, 'forgot_password.html')



def logout(request):
 
 try:
        del request.session['email']
        del request.session['password']
 except:
        pass
 return HttpResponse("<h1>Thank you for staying in , now yours  <br>Session Data cleared</h1>")


        

          
