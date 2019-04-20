from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Article

class homepage(ListView):
    model = Article
    template_name = 'homepage/home.html'
    context_object_name = 'articles'

    def get_context_data(self,**kwards):
        ctx = super(homepage, self).get_context_data(**kwards)
        ctx['title'] = 'ROMBICK'
        ctx['active'] = 'homepage'
        return ctx
class ArticleDetailView(DetailView):
    model = Article
    context_object_name = 'article'
    template_name = 'homepage/article_detail.html'

    def get_context_data(self, **kwards):
        ctx = super(ArticleDetailView, self).get_context_data(**kwards)
        ctx['title'] = Article.objects.filter(pk=self.kwargs['pk']).first()
        return ctx
def contacts(request):
    return render(request,'homepage/contacts.html',{'title': 'Contacts', 'active': 'contacts'})
