from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    TemplateView, RedirectView , ListView, DetailView,
    FormView, CreateView, UpdateView,DeleteView, View
)
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import TaskForm
from .models import Task




class TaskListView(LoginRequiredMixin,ListView):
    #model = Task 
    # default is Task.objects.all()
    template_name = 'todo/index.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user) # use for request needed

    # post method override
    def post(self, request):
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = self.request.user
            task.save()
            return redirect('/')


