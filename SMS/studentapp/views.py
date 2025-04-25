from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request , 'index.html')



def hlo(request):
    return HttpResponse("""<h1 style="font-size:150px;color:royalblue;"> SSJS </h1>""")    


def hello(request):

    js="""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>h1{
    color: blue;
    font-size :150px;
    
}
</style>
</head>
<body>
    <h1>JSSS </h1>
    
</body>
</html"""
    return HttpResponse(js)

def test(request):
    js="""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>h1{
    color: blue;
    font-size :150px;
    
}
</style>
</head>
<body>
    <h1>JS <--> SS </h1>
    
</body>
</html"""
    return render(request , 'test.html', {'jsss': js})    

def test1(request):
    txt ="""<h1 style= "color: orange ;" > Tell me about your self </h1>
    """
    name="Manisha"
    college ="University of Lucknow "
    return render(request , 'test1.html' ,{'t': txt  , 'myname':name , "mycollege" :college } )  # t is a key and txt is the value and they are dictionary 