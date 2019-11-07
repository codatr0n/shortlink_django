from django.shortcuts import render
from django.shortcuts import get_list_or_404, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Link, Tag
from .forms import LinkForm, TagForm

import string
import random


# Create your views here.
def homepage(request):
    # return HttpResponse('Homepage')

    # render all links in database for testing
    return render(request, 'main/home.html', context={})

def jump(request, shrtcode):
    link = Link.objects.get(shortcode=shrtcode)
    if link:
        tags = link.tags.all()
        context = {'link': link, 'tags': tags}
        return render(request, 'main/jump.html', context=context)
    else:
        return HttpResponseRedirect('/')

##############################################################################
#  LINKS
##############################################################################

def showlinks(request):
    links = Link.objects.all()
    context = {'links': links}
    return render(request, 'main/showlinks.html', context=context)


def make_shortcode(length=6): # helper function for createlink
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
        if form.is_valid():
            new_link = form.save(commit=False)
            new_link.shortcode = make_shortcode()
            new_link.save()
            form.save_m2m()
            return HttpResponseRedirect('/link/'+str(new_link.id))
    else:
        context = {'form': form}
        return render(request, 'main/createlink.html', context=context)


def linkdetails(request, id):
    link = get_object_or_404(Link, pk=id)
    form = LinkForm(instance=link)
    context = {'form': form, 'link': link}
    return render(request, 'main/linkdetails.html', context=context)


def editlink(request, id):
    link = get_object_or_404(Link, pk=id)
    if request.method == 'POST':
        form = LinkForm(request.POST, instance=link)
        if form.is_valid():
            link = form.save(commit=False)
            link.save()
            form.save_m2m()
            return HttpResponseRedirect('/link/'+str(id))
    else:
        return HttpResponseRedirect('/link/'+str(id))


def deletelink(request, id):
    link = get_object_or_404(Link, pk=id)
    if request.method == 'POST':
        link.delete()
        return HttpResponseRedirect('/showlinks')
    else:
        context = {'link': link}
        return render(request, 'main/deletelink.html', context=context)


##############################################################################
#  TAGS
##############################################################################

def showtags(request):
    tags = Tag.objects.all()
    context = {'tags': tags}
    return render(request, 'main/showtags.html', context=context)


def createtag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            new_tag = form.save(commit=False)
            new_tag.save()
            form.save_m2m()
            # return HttpResponseRedirect('/tag/'+str(new_link.id))
            return HttpResponseRedirect(reverse('tagdetails', kwargs={'id': str(new_tag.id)}))
    else:
        form = TagForm()
        context = {'form': form}
        return render(request, 'main/createtag.html', context=context)


def tagdetails(request, id):
    tag = get_object_or_404(Tag, pk=id)
    form = TagForm(instance=tag)
    context = {'form': form, 'tag': tag}
    return render(request, 'main/tagdetails.html', context=context)


def edittag(request, id):
    tag = get_object_or_404(Tag, pk=id)
    if request.method == 'POST':
        form = TagForm(request.POST, instance=tag)
        if form.is_valid():
            tag = form.save(commit=False)
            tag.save()
            form.save_m2m()
            return HttpResponseRedirect('/tag/'+str(id))
    else:
        return HttpResponseRedirect('/tag/'+str(id))


def deletetag(request, id):
    tag = get_object_or_404(Tag, pk=id)
    if request.method == 'POST':
        tag.delete()
        return HttpResponseRedirect(reverse('showtags'))
    else:
        context = {'tag': tag}
        return render(request, 'main/deletetag.html', context=context)