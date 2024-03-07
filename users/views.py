# Import the render function from django.shortcuts module
from django.shortcuts import render
# Import the HttpResponse class from django.http module
from django.http import HttpResponse
'''
# Import the MyModel model from the current directory
from .models import MyModel
'''

# Create your views here.
def index(request):
    return render(request, 'base.html')
'''
# Define a view function called 'index' that takes a request object as parameter
def indexs(request):
    # Return an HTTP response with the text "Hello, world! This is the index page."
    return HttpResponse("Hello, world! This is the index page.")

# Define a view function called 'my_view' that takes a request object as parameter
def my_view(request):
    # Query all objects from the MyModel model and store the result in the 'queryset' variable
    queryset = MyModel.objects.all()
    # Render a template called 'myapp/my_template.html' with the 'queryset' variable passed to it
    return render(request, 'myapp/my_template.html', {'queryset': queryset})

# Define a view function called 'detail_view' that takes a request object and a primary key (pk) as parameters
def detail_view(request, pk):
    # Retrieve a specific object from the MyModel model based on its primary key (pk)
    instance = MyModel.objects.get(pk=pk)
    # Render a template called 'myapp/detail.html' with the 'instance' variable passed to it
    return render(request, 'myapp/detail.html', {'instance': instance})
'''