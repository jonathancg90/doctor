# -*- coding: utf-8 -*-
import json

from django.core.urlresolvers import reverse
from django.views.generic import TemplateView, View, RedirectView
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.contrib import auth


class HomeTemplateView(TemplateView):
    template_name = 'website/home.html'


class LoginTemplateView(TemplateView):
    template_name = 'website/login.html'


class LoginUserView(View):

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        self.token = request.POST.get('rp_token', None)
        return super(LoginUserView, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        response = {}
        response['status'] = 'fail'
        user = request.POST.get('user')
        password = request.POST.get('password')

        user = auth.authenticate(
            username=user,
            password=password
        )
        if user is not None and user.is_active:
            auth.login(self.request, user)
            response['status'] = 'ok'
        response = HttpResponse(json.dumps(response))
        return response


class LogoutView(RedirectView):

    def get(self, request, *args, **kwargs):
        auth.logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)

    def get_redirect_url(self, **kwargs):
        return reverse('home')