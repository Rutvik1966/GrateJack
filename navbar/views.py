from fileinput import filename
from django.http import HttpResponse
from django.shortcuts import render
import mimetypes
import os
# Create your views here.
def helloworld(request):
    return render(request,'./nav/navbar.html')
def landing(request):
    return render(request,'./landing/landing.html')

def download_file(request):
    # Define Django project base directory
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # Define text file name
    filename = 'Jack_Resume.pdf'
    # Define the full file path
    filepath = BASE_DIR + '\\file\\' + filename
    # Open the file for reading content
    path = open(filepath, 'rb')
    # Set the mime type
    mime_type, _ = mimetypes.guess_type(filepath)
    # Set the return value of the HttpResponse
    response = HttpResponse(path, content_type=mime_type)
    # Set the HTTP header for sending to browser
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    # Return the response value
    return response