from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.views import generic
from .models import Album
from .forms import UserForm

class IndexView(generic.ListView):
    template_name ='music/index.html'
    context_object_name = 'all_albums'

    def get_queryset(self): #query db for albums
        return Album.objects.all()

class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'


#form to create new object, also have update
class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']

# form to create new object, also have update
class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']

class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')

class UserFormView(View):
    form_class = UserForm
    template_name = 'music/registration_form.html'

    #display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name,{'form': form})
    #process form data here
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            #create object from form, does not save it to DB yet.
            user = form.save(commit=False)

            #cleaned (normalized) data/ data that is formatted properly.
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            #this is how you set pw.
            user.set_password(password)
            user.save()

            #returns User objects if credentials are correct
            #checks DB if they are an actual user.
            user = authenticate(username=username, password=password)

            if user is not None:
                #django lets you have users that are inactive, etc so check for that
                if user.is_active:
                    login(request, user) #passes in session, done
                    # request.user.username to refer to them
                    #redirect to home page now
                    return redirect('music:index')


        return render(request, self.template_name, {'form': form})