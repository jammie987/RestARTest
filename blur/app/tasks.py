import os
import urllib.request

import cv2
from celery import shared_task
from django.conf import settings

from .models import Video

@shared_task
def estimate(url):
    record = Video.objects.create(link=url)
    video_name = 'vid{}.mp4'.format(record.id)
    urllib.request.urlretrieve(url, video_name)

    cap = cv2.VideoCapture(video_name)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    blur_count = 0
    for i in range(frame_count):
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blur = cv2.Laplacian(gray, cv2.CV_64F).var()
        if blur < settings.BLUR_TRESHOLD:
            blur_count += 1
    result = -1 if blur_count / frame_count > 0.7 else 1
    record.result = result
    record.save()
    os.remove(video_name)
    return result
