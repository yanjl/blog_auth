# Blog (c) by win10-pc
#
# Blog is licensed under a
# Creative Commons Attribution 3.0 Unported License.
#
# You should have received a copy of the license along with this
# work.  If not, see <http://creativecommons.org/licenses/by/3.0/>.

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist, PermissionDenied
from django.views.generic import CreateView, DetailView, ListView, TemplateView

from .forms import RegisterModelForm
from .models import Blog


class BlogIndex(TemplateView):
    template_name = 'blog/index.html'


class BlogList(LoginRequiredMixin, ListView):
    model = Blog
    context_object_name = 'posts'
    template_name = 'blog/list.html'
    paginate_by = 3

    def get_queryset(self):
        return Blog.objects.all().filter(owner=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total'] = self.get_queryset().count

        return context


class BlogOwnerMixin:
    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()

        pk = self.kwargs.get(self.pk_url_kwarg, None)
        queryset = queryset.filter(
            pk=pk,
            owner=self.request.user,
        )

        try:
            obj = queryset.get()
        except ObjectDoesNotExist:
            raise PermissionDenied

        return obj


class BlogDetail(LoginRequiredMixin, BlogOwnerMixin, DetailView):
    model = Blog
    context_object_name = 'post'
    template_name = 'blog/detail.html'


class BlogPublish(LoginRequiredMixin, CreateView):
    template_name = 'blog/publish.html'
    form_class = RegisterModelForm

    def get_success_url(self):
        last_post = Blog.objects.filter(
            owner=self.request.user).latest('publish')
        return f'/blog/detail/{last_post.id}'

    def get_initial(self):
        initial = super().get_initial()
        initial['owner'] = self.request.user
        return initial
