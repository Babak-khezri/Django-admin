from .models import Story
from django.utils import timezone


class SetStoryStatusMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        stories = Story.objects.filter(status='a')
        for story in stories:
            if (timezone.now() - story.date).days >= 1:
                story.status = 'd'
                story.save()
        response = self.get_response(request)
        return response
