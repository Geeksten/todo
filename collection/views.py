from models import todo
from django.shortcuts import render

# Create your views here.

def index(request):
    # this is your new view
    return render(request, 'index.html')

#############################################################################
# from models import todo
from django.shortcuts import render_to_response
 
def index(request): #Define our function, accept a request
 
    items = todo.objects.all() #ORM queries the database for all of the to-do entries.
    
    #Responds with passing the object items (contains info from the DB) 
    #to the template index.html
    return render_to_response('index.html', {'items': items}) 
