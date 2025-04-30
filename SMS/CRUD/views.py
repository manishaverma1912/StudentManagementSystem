from django.shortcuts import render , redirect , get_object_or_404
from CRUD.models import Review


# Create your views here.

def reviewForm(request):
    if request.method == "POST":
        Mname = request.POST.get("Manisha")
        Memail = request.POST.get("email") 
        Mmessage = request.POST.get("message")

        review = Review()      # Review() is a class and we create an Object for access the propertities and field of class .
        review.name = Mname
        review.email = Memail
        review.message = Mmessage
        review.save()

    ReviewForm = Review.objects.all()
    return render(request ,'CRUD//reviewForm.html',{'RF' : ReviewForm} )


def delete_review(request , ok ):
    dReview = get_object_or_404(Review , id = ok )
    # dReview = get_object_or_404(Review , pk = ok )

    if request.method == "POST":
        dReview.delete()
        return redirect('reviewform')

    return render(request , 'CRUD//delete.html', {'dataReview' : dReview})    

def update_review(request , ok):
    u = get_object_or_404(Review , id =ok)

    if request.method == 'POST':
        u.name = request.POST.get('name')
        u.email = request.POST.get("email") 
        u.message = request.POST.get("message")


        u.save()
        return redirect('reviewform')
    
    return render(request ,'CRUD//update.html' ,{"uu" : u})














