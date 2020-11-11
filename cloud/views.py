

from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .forms import LoginForm
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages

from .models import Guest_User, Posts


def index(request) :
	return render(request, 'index.html')

def user_login(request) :
	form = AuthenticationForm()
	return render(request, 'user_login.html', context = {"form":form})		

def logout_request(request):
    logout(request)      
    messages.info(request, "Logged out successfully!")
    return render(request,'index.html')


# def login(request):
#    username = "not logged in"
   
#    if request.method == "POST":
#       #Get the posted form
#       MyLoginForm = LoginForm(request.POST)
      
#       if MyLoginForm.is_valid():
#          username = MyLoginForm.cleaned_data['username']
#    else:
#       MyLoginForm = Loginform()
		
#    return render(request, 'loggedin.html', {"username" : username})




def login_request(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return HttpResponse("Admin Page!!!")
        else :
            try:
                user = Guest_User.object.get(username=username)
            except Guest_User.DoesNotExist:
                return HttpResponse("User Does Not Exist!!")
            if user is not None:
                if(user.password == password):
                    return HttpResponse("Guest User Page!!!")
                else:
                    return HttpResponse("Wrong password!!")

    form = AuthenticationForm()
    return render(request = request,
                    template_name = "user_login.html",
                    context={"form":form})



def add_post(request) :
    post = Posts(post_title="aeku", post_description="viku")
    post.save()
    return HttpResponse("Inserted")

# def update_post(request) :
#     pass

# def delete_post(request) :
#     pass

def read_post(request) :
    post = Posts.object.get(post_title = "aeku")
    stringval = "" + post.post_title + "" + post.post_description
    return HttpResponse(stringval)


def add_user(request) :
    user = Guest_User(username = "guest", password = "guest")
    user.save()
    return HttpResponse("User Added")

def read_user(request):
    user = Guest_User.object.get(username="guest")
    return HttpResponse(user.password)