from django.conf import settings
from django.shortcuts import render, redirect
from django.views.generic.base import View

from oauth2client.client import flow_from_clientsecrets, OAuth2WebServerFlow
from oauth2client.contrib import xsrfutil
from oauth2client.contrib.django_util.storage import DjangoORMStorage
from .models import CredentialsModel

from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'app/home.html'

from django import forms
from django.views.generic.edit import FormView

class YouTubeForm(forms.Form):
    pass

class HomePageView(FormView):
    template_name = 'core/home.html'
    form_class = YouTubeForm

class AuthorizeView(View):

    def get(self, request, *args, **kwargs):
        storage = DjangoORMStorage(
            CredentialsModel, 'id', request.user.id, 'credential')
        credential = storage.get()
        flow = OAuth2WebServerFlow(
            client_id=settings.GOOGLE_OAUTH2_CLIENT_ID,
            client_secret=settings.GOOGLE_OAUTH2_CLIENT_SECRET,
            scope='https://www.googleapis.com/auth/youtube',
            redirect_uri='http://127.0.0.1:8000/oauth2callback/')
        if credential is None or credential.invalid == True:
            flow.params['state'] = xsrfutil.generate_token(
                settings.SECRET_KEY, request.user)
            authorize_url = flow.step1_get_authorize_url()
            return redirect(authorize_url)
        return redirect('/')    

