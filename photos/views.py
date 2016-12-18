from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.core.urlresolvers import reverse_lazy
from django.core.paginator import Paginator
from django.shortcuts import render_to_response, render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.middleware import csrf
from .models import Album, Photo
from .forms import UserForm

def albums(request, page_number = 1):
    list_albums = Album.objects.all()
    current_page = Paginator(list_albums, 1)
    return render_to_response('photos/index.html', {'albums':current_page.page(page_number)})

class IndexView(generic.ListView):
    template_name = 'photos/index.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()

class DetailView(generic.DetailView):
    model = Album
    template_name = 'photos/detail.html'

class CreateAlbum(CreateView):
    model = Album
    fields = ['author', 'title', 'description', 'logo']

class UpdateAlbum(UpdateView):
    model = Album
    fields = ['author', 'title', 'description', 'logo']

class DeleteAlbum(DeleteView):
    model = Album
    success_url = reverse_lazy('photos:index')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

class CreatePhoto(CreateView):
    model = Photo
    fields = '__all__'
    success_url = reverse_lazy('photos:index')

class UserFormView(View):
    form_class = UserForm
    template_name = 'photos/registration_form.html'

    #Пустая форма
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # Обработка данных формы
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit = False)

            # clean data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # Если данные введены правильно
            user = authenticate(username = username, password = password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('photos:index')
        return render(request, self.template_name, {'form': form})

class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "photos/login_form.html"

    # Если вход выполнен успешно
    success_url = reverse_lazy('photos:index')

    def form_valid(self, form):
        # Получаем объект пользователя на основе введённых в форму данных
        self.user = form.get_user()

        # Выполняем аутентификацию пользователя
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)

class LogoutView(View):
    def get(self, request):
        # Выполняем выход для пользователя, запросившего данное представление.
        logout(request)

        # После чего, перенаправляем пользователя на главную страницу.
        return HttpResponseRedirect("/photos/")