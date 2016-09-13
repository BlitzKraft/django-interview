from django.http import HttpResponse
from django.template import loader
import re
import os

CURR_PATH = os.path.abspath('./')

all_sizes = []
all_count = []

def image_size(s):
    out = re.findall('\d+x\d+', s)
    return out[-1]

with open('image_sizes/fun-rooster-thumbnail-names.txt') as test:
    content = test.readlines()
    for ln in content:
        matches = image_size(ln)
        if matches in all_sizes:
            all_count[all_sizes.index(matches)] += 1
        else:
            all_sizes.append(matches)
            all_count.append(1)

def index(request):
    #sizes = all_sizes
    #count = all_count
    lst = zip(all_sizes, all_count)
    template = loader.get_template(CURR_PATH + '/image_sizes/templates/image_sizes/index.html')
    context = {
        'lst': lst,
    }
    return HttpResponse(template.render(context, request))

