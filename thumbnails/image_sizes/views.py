from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.template.defaulttags import csrf_token
from django.shortcuts import render
from django import forms
import re
import os

CURR_PATH = os.path.abspath('./')

all_sizes = []
all_count = []

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

def image_size(s):
    out = re.findall('\d+x\d+', s)
    return out[-1]

filename = 'image_sizes/fun-rooster-thumbnail-names.txt'

def fun_imgsz(fn):
    with open(fn) as test:
        content = test.readlines()
        for ln in content:
            matches = image_size(ln)
            if matches in all_sizes:
                all_count[all_sizes.index(matches)] += 1
            else:
                all_sizes.append(matches)
                all_count.append(1)

def index(request):
    total = sum(all_count)
    lst = zip(all_sizes, all_count)
    template = loader.get_template(os.path.join(CURR_PATH, 'image_sizes/templates/image_sizes/index.html'))
    context = {
        'lst': lst,
        'total': total,
        'filename' : filename,
    }
    return HttpResponse(template.render(context, request))

fun_imgsz(filename)

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            write_file(request.FILES['file'])
            return HttpResponseRedirect('index.html')
    else:
        #form = UploadFileForm()
        return render(request, 'index.html')
def myview(request):
    request.FILES['myfile']

def write_file(f):
    with open(MEDIA_ROOT, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

