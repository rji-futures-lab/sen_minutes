from django.urls import path

from . import views

app_name = 'minutes_search'

urlpatterns = [
    path('', views.index, name='index'),
    path('guide/', views.guide, name='guide'),
    path('guide/witness_for', views.witness_for_csv, name='witness_for'),
    path('guide/witness_against', views.witness_against_csv, name='witness_against'),
    path('search_by_bill/', views.search_by_bill, name='search_by_bill'),
    path('search_by_bill/<int:year>/<int:bill_no>', views.bill_detail, name='bill_detail'),
    path('search_by_org/', views.search_by_org, name='search_by_org'),
    path('search_by_lawmaker/', views.search_by_lawmaker, name='search_by_lawmaker'),
    path('search_by_name/', views.search_by_name, name='search_by_name'),
] 
