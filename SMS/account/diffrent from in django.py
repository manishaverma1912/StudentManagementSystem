from django.contrib import messages

# save the data DIRECTLY
def register(request):
    if request.method == "POST":
        f = RegisterForm(request.POST)
        if f.is_valid():
            f.save() #this function directly save the data in DB
            messages.success(request, 'Success message') # use can print the massege

            # return redirect('login')   # after register direct login
    else :
         f = RegisterForm()   
 
    return render(request , "account//register.html", { "f" : f })  

#  save the and redirect in login page 
def register(request):
    if request.method == "POST":
        f = RegisterForm(request.POST)
        if f.is_valid():
            f.save() #this function directly save the data in DB
            messages.success(request, 'Success message') # use can print the massege
            return redirect('login')   # after register direct login  
    else :
         f = RegisterForm()   
 
    return render(request , "account//register.html", { "f" : f })

#  save the and then automatic login and redirect in profile
def register(request):
    if request.method == "POST":
        f = RegisterForm(request.POST)
        if f.is_valid():
            user = f.save(commit = False)
            print(user) 
            user.set_password(f.cleaned_data["password"])   #hash password to raw string  by using  set_passsword
            user.save()
            login(request , user)       # after register direct login and redirect in home page
            return redirect('home')
    else :
         f = RegisterForm()   
 
    return render(request , "account//register.html", { "f" : f })