from django.db.models import query
from django.shortcuts import render
from django.http import JsonResponse
from .models import SearchQuery
import json

# Create your views here.
def add_query(req):
    params = json.loads(req.body)
    params["query"]
    params["region"]
    pair = SearchQuery.objects.get_or_create(
        querystring=params["query"], region=params["region"]
    )
    return JsonResponse({"status": 201, "id": pair.id})


def home(req):
    return render(req, "index.html")


def get_stats(req):
    pass
