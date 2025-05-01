from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Visit
from .forms import VisitForm, AppointmentSearchForm
from django.views.generic import TemplateView, ListView
from django.http import HttpResponse
from django.utils import timezone
import jdatetime
from jalali_date import datetime2jalali, date2jalali
from django.db.models import Q

class VisitCreateView(CreateView):
    model = Visit
    form_class = VisitForm
    template_name = 'visit/register_visit.html'
    success_url = reverse_lazy('register')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today = timezone.now().date()
        context['today'] = today
        context['todayVisit'] = Visit.objects.filter(current_visit_date=today)
        context['todayTurns'] = Visit.objects.filter(next_visit_date=today)
        return context
 
class VisitSuccessView(TemplateView):
    template_name = 'success.html'    

class VisitListView(ListView):
    model = Visit
    template_name = 'visit/visit_list.html'
    context_object_name = 'visits'
    paginate_by = 12

    def get_queryset(self):
        queryset = Visit.objects.all().order_by('-current_visit_date')
        search_query = self.request.GET.get('search')
        
        if search_query:
            queryset = queryset.filter(
                Q(first_name__icontains=search_query) |
                Q(last_name__icontains=search_query) |
                Q(phone__icontains=search_query) |
                Q(service__name__icontains=search_query)
            )
        
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('search', '')
        return context

class AppointmentListView(ListView):
    model = Visit
    template_name = 'visit/appointment_list.html'
    context_object_name = 'appointments'
    paginate_by = 12

    def get_queryset(self):
        queryset = Visit.objects.filter(next_visit_date__isnull=False).order_by('next_visit_date')
        form = AppointmentSearchForm(self.request.GET)
        
        if form.is_valid() and form.cleaned_data['date']:
            search_date = form.cleaned_data['date']
            queryset = queryset.filter(next_visit_date=search_date)
        
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AppointmentSearchForm(self.request.GET)
        return context

class VisitUpdateView(UpdateView):
    model = Visit
    form_class = VisitForm
    template_name = 'visit/visit_update.html'
    success_url = reverse_lazy('visits:visit_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'ویرایش ویزیت'
        return context

class VisitDeleteView(DeleteView):
    model = Visit
    success_url = reverse_lazy('visits:visit_list')
    template_name = 'visit/visit_confirm_delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'حذف ویزیت'
        return context















