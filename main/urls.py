from django.urls import path
from . import views

# app_name = 'main'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    
    # LINKS
    path('links', views.showlinks, name='showlinks'),
    path('link/create', views.createlink, name='createlink'),
    path('link/<int:id>/delete', views.deletelink, name='deletelink'),
    path('link/<int:id>/edit', views.editlink, name='editlink'),
    path('link/<int:id>', views.linkdetails, name='linkdetails'),
    
    # TAGS
    path('tags', views.showtags, name='showtags'),
    path('tag/create', views.createtag, name='createtag'),
    path('tag/<int:id>/delete', views.deletetag, name='deletetag'),
    path('tag/<int:id>/edit', views.edittag, name='edittag'),
    path('tag/<int:id>', views.tagdetails, name='tagdetails'),

    path('<str:shrtcode>', views.jump, name='jump')
]
