from django.shortcuts import render
from django.views.generic import View
from django.http import HttpRequest, HttpResponse

from main.forms import ButtonForm, KeyboardForm
from abstract.mixins import HttpResponseMixin

# Create your views here.
class ButtonView(HttpResponseMixin, View):
    """View for Button"""

    form = ButtonForm

    def get(self, request: HttpRequest, *args, **kwargs):
        return self.get_http_response(
            request=request,
            template_name='button.html',
            context={
                'ctx_form' : self.form()
            }
        )

    def post(
        self, 
        request: HttpRequest,
        *args: tuple, 
        **kwargs: dict
    ) -> HttpResponse:
        form = self.form(request.POST or None)
        if not form.is_valid():
            return HttpResponse('Bad')
        print(form.cleaned_data)
        form.save()
        return HttpResponse('OK')


class KeyboardView(HttpResponseMixin, View):
    """View for Button"""

    form = KeyboardForm

    def get(self, request: HttpRequest, *args, **kwargs):
        return self.get_http_response(
            request=request,
            template_name='keyboard.html',
            context={
                'ctx_form' : self.form()
            }
        )

    def post(
        self, 
        request: HttpRequest,
        *args: tuple, 
        **kwargs: dict
    ) -> HttpResponse:
        form = self.form(request.POST or None)
        if not form.is_valid():
            return HttpResponse('Bad')
        print(form.cleaned_data)
        form.save()
        return HttpResponse('OK')