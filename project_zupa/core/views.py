from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView
from django.shortcuts import get_object_or_404
from django.views.generic.edit import FormView
from django.urls import reverse


from .models import Glasnik, Post, PostViews
from .forms import KontaktForm

# Create your views here.
class HomeView(TemplateView):
    model = Glasnik
    template_name = "core/glasnici.html"
    context_object_name = 'queryset'
    paginate_by = 6

    def get(self, request, *args, **kwargs):
        latest = Glasnik.objects.order_by('-broj')
        context = {
            'latest': latest,
        }
        return render(request, 'core/home.html', context)

    def get_context_data(self, **kwargs):
        most_recent = Glasnik.objects.order_by('-broj')
        context = super().get_context_data(**kwargs)
        context['most_recent'] = most_recent
        context['page_request_var'] = "page"
        return context


class GlasniciListView(ListView):
    model = Glasnik
    template_name = "core/glasnici.html"
    context_object_name = 'queryset'


    def get_context_data(self, **kwargs):        
        context = super().get_context_data(**kwargs)
        return context


class VijestiView(ListView):
    model = Post
    template_name = "core/vijesti.html"
    all_posts = get_object_or_404(Post)
    context = {
        'all_posts': all_posts,
    }

    def get_absolute_url(self):
        return reverse('vijesti_detail', kwargs={
            'slug': self.slug
        })
    

class VijestiDetailView(DetailView):

    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['timestamp'] = Post.timestamp
        return context


class PovijestView(TemplateView):
    template_name='core/povijest.html'


class KontaktView(TemplateView):
    template_name = "core/kontakt.html"
    form = KontaktForm()


class KontaktFormView(FormView):
    template_name = "core/kontakt.html"
    form_class = KontaktForm
    success_url = '/home/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.4
        
        return super().form_valid(form)
