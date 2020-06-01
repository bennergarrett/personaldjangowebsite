from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"
    
    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

class ThanksPage(TemplateView):
    template_name = 'thanks.html'
    
