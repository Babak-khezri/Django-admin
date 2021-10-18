from account.models import User
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Story, Highlight
from .mixins import FormValidMixin
from django.urls.base import reverse
from django.views import View
from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from .forms import ImageUploadForm


class StoryCreateView(LoginRequiredMixin, FormValidMixin, CreateView):
    model = Story
    fields = ['image', ]
    template_name = 'story/story_create.html'

    def get_success_url(self):
        return reverse('instagram:home')


def story_list_view(request, username):
    user = request.user
    account = get_object_or_404(User, username=username)
    stories = account.stories.active()
    for story in stories:
        story.hits.add(user)
        story.save()
    return render(request, 'story/story_list.html', {'stories': stories})


class StoryListView(View):
    def get(self, request):
        pass


def highlite_create_view(request):
    if request.method == 'POST':
        stories = [int(story) for story in request.POST.getlist('stories')]
        stories = [Story.objects.get(pk=pk) for pk in stories]
        if stories:
            form = ImageUploadForm(request.POST, request.FILES)
            image = form.cleaned_data['image'] if form.is_valid(
            ) else stories[0].image
            highlight = Highlight.objects.create(
                user=request.user, image=image, name=request.POST.get('name'))
            for story in stories:
                highlight.stories.add(story)
            highlight.save()
            return redirect('profiles:profile', request.user.username)
    stories = get_list_or_404(Story, user=request.user)
    return render(request, 'story/highlight_create.html', {'stories': stories})


def highlight_story_view(request, pk):
    highlight = get_object_or_404(Highlight, pk=pk)
    stories = highlight.stories.all()
    return render(request, 'story/story_list.html', {'stories': stories})
