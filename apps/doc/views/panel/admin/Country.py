# -*- coding: utf-8 -*-
from django.conf import settings
from django.core.urlresolvers import reverse
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic import ListView
from apps.common.view import SearchFormMixin
from apps.doc.forms.Country import CountryForm, CountryFiltersForm
from apps.doc.models.Country import Country


class CountryListView(SearchFormMixin, ListView):
    model = Country
    template_name = 'panel/admin/country/list.html'
    search_form_class = CountryFiltersForm
    paginate_by = settings.PANEL_PAGE_SIZE
    filtering = {
        'name': SearchFormMixin.ALL,
    }


class CountryCreateView(CreateView):
    model = Country
    form_class = CountryForm
    template_name = 'panel/admin/country/create.html'

    def get_success_url(self):
        return reverse('country_list')


class CountryUpdateView(UpdateView):
    model = Country
    form_class = CountryForm
    template_name = 'panel/admin/country/edit.html'

    def get_success_url(self):
        return reverse('country_list')


class CountryDeleteView(DeleteView):
    model = Country
    template_name = 'panel/admin/country/delete.html'

    def get_success_url(self):
        return reverse('country_list')


