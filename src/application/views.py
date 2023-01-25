from django.shortcuts import render

# Create your views here.

from .models import Comment, Post

from django.views import View

from .models import Post, Comment

from django.http.response import HttpResponse
from django.db import transaction


class SampleView(View):

    def get(self, *args, **kwargs):
        p = Post.objecst.get(id=1)
        p.hit += 1
        raise Exception("this is exception")
        p.save()

        return HttpResponse(200)
