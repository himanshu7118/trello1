from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Document
# Create your views here.
# from django.conf import settings
# from django.core.files.storage import FileSystemStorage
from .forms import Document_Form
# def upload(request):
#     if request.method == 'POST' and request.FILES['myfile']:
#         myfile = request.FILES['myfile']
#         fs = FileSystemStorage()
#         filename = fs.save(myfile.name, myfile)
#         uploaded_file_url = fs.url(filename)
#         return render(request, 'simple_upload.html', {
#             'uploaded_file_url': uploaded_file_url
#         })
#     return render(request,'simple_upload.html')

    
def upload(request):
    if request.method == 'POST':
        form = Document_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload')
    else:
        form = Document_Form()
    obj=Document.objects.all()
    return render(request, 'model_form_upload.html', {
        'form': form,
        'items':obj
    })



