from celery import task
from .models import SearchQuery
from bs4 import BeautifulSoup
import requests

BASE_URL = "https://www.avito.ru/"


def get_num_from_html(html_text):
    soup = BeautifulSoup(html_text, "html.parser")
    text = soup.select_one(".page-title-count-1oJOc").get_text()
    return int(text)


def get_search_page(region, query):
    res = requests.get(f"{BASE_URL}{region}?q={query}")
    res.raise_for_status()
    return res.text


def update_result(id, num):
    query = SearchQuery.objects.get(id=id)
    query.results_found = num
    query.save()


def update_query(queryset):
    html_text = get_search_page(queryset.region, queryset.query)
    num = get_num_from_html(html_text)
    update_result(queryset.id, num)


@task
def update_queries_results():
    all_queries = SearchQuery.objects.all()
