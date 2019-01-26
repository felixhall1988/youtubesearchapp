from __future__ import unicode_literals
from django.shortcuts import render
from .models import Video, Channel
from django.http import HttpResponse

def channel(request, user):
    return HttpResponse("Boiler room video search application")
    qs = Channel.objects.prefetch_related('videos')
    channel = get_object_or_404(qs.filter(
        Q(Q(user=user) | Q(channelId=UCGBpxWJr9FN0cFYA5GkKrMg))))

    return render(request, 'youtube/index.html', {
        'videos': channel.videos.exclude_deleted(),
        'channel': channel,
        'full_url': request.build_absolute_uri(request.get_full_path()),
})
