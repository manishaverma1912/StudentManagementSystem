from django.shortcuts import render  , redirect
from .forms import RegisterForm  , loginForm
from django.contrib.auth import authenticate ,login ,logout
from django.contrib.auth.decorators import  login_required


def register(request):
    if request.method == "POST":
        f = RegisterForm(request.POST)
        if f.is_valid():
            # f.save() #this function directly save the data in DB
            user = f.save(commit = False)
            user.set_password(f.cleaned_data["password"])   #hash password to raw string  by using  set_passsword
            # print(user, user.set_password(f.cleaned_data["password"]) )
            user.save()
            login(request , user)       # after register direct login and redirect in home page
            return redirect('home')

            # return redirect('login')   # after register direct login  
            
            

    else :
         f = RegisterForm()   
 
    return render(request , "account//register.html", { "f" : f })
        

def login_view(request):
    if request.method == "POST":
        l = loginForm(data = request.POST)
        if l.is_valid():
            user = l.get_user()
            login(request , user)
            return redirect('home')
    else:
        l =loginForm()

    return render(request , "account//login.html" , {"lo" : l})    

@login_required            
def home(request):
    return render(request , "account//home.html")

            

@login_required        
def logout_view(request):
    logout(request)
    return redirect('login')

