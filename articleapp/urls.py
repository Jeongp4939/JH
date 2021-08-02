from django.urls import path
from django.views.generic import TemplateView

from articleapp.views import ArticleCreationView

app_name = 'articleapp'

urlpatterns = [

    path('list/', TemplateView.as_view(template_name='articleapp/list.html'), name='list'),

    path('create/', ArticleCreationView.as_view(), name = 'create')
]
