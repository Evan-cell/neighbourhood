from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .models import neighbourhood,healthservices,Business,Health,Authorities,BlogPost,Profile,notifications,Comment
from .email import send_priority_email
from .forms import notificationsForm,ProfileForm,BlogPostForm,BusinessForm,CommentForm
from decouple import config,Csv
import datetime as dt
from django.http import JsonResponse
import json
from django.db.models import Q
from django.contrib.auth.models import User

from rest_framework.response import Response
from rest_framework.views import APIView
# from .serializer import


# Create your views here.
