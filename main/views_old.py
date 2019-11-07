from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_list_or_404, get_object_or_404

from .models import Link, Tag
from .forms import LinkForm

import string, random


# Create your views here.
def homepage(request):
    # return HttpResponse('Homepage')

    return render(request, 'main/home.html', context = { })  # render all links in database for testing


def link(request, shrtcode):
    link = Link.objects.get(shortcode = shrtcode)
    if link:
        tags = link.tags.all()
        context = { 'link': link, 'tags': tags }
        return render(request, 'main/link.html', context = context )
    else:
        return HttpResponseRedirect('/')


def make_shortcode(length=6):
    characters = string.ascii_letters + string.digits
    shortcodes = Link.objects.all()
    while(True):
        new_shortcode = ''.join(random.choice(characters) for i in range(length))
        if new_shortcode not in shortcodes:
            break
    return new_shortcode


def createlink(request):
    form = LinkForm()

    if request.method == 'POST':
        form = LinkForm(request.POST)
        print(form)
        if form.is_valid():
            new_link = form.save(commit=False)
            new_link.shortcode = make_shortcode()
            new_link.save()
            form.save_m2m()

            context = {'form': form}

            return render(request, 'main/createlink.html', context = context)

    else:
        # context = { 'tags': tags }
        context = { 'form': form }
        return render(request, 'main/createlink.html', context = context)

def viewlinks(request):
    links = Link.objects.all()
    context = { 'links': links }
    return render(request, 'main/viewlinks.html', context = context)


def editlink(request, id):
    link = get_object_or_404(Link, pk=id)

    if request.method == 'POST':
        form = LinkForm(request.POST, instance=link)
        if form.is_valid():
            link = form.save(commit=False)
            # link.shortcode = Link.objects.get(pk=id).shortcode
            link.save()
            form.save_m2m()

            context = {'form': form, 'link': link}

            return render(request, 'main/editlink.html', context = context)

    else:
        form = LinkForm(instance=link)
        context = {'form': form, 'link': link}

    return render(request, 'main/editlink.html', context = context)

def deletelink(request, id):
    link = get_object_or_404(Link, pk=id)

    if request.method == 'POST':
        link.delete()
        return HttpResponseRedirect('/viewlinks')

    else:
        context = {'link': link }

    return render(request, 'main/deletelink.html', context = context)