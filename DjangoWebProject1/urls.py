"""
Definition of urls for DjangoWebProject1.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from app import forms, views


urlpatterns = [
    path('', views.home, name='home'),
    path('phenotype_list_page/', views.phenotype_list_page, name='phenotype_list_page'),
    path('phenotype_detail_page/<int:maladieID>', views.phenotype_detail_page, name='phenotype_detail_page'),
    path('SNP_search_from_page/', views.SNP_search_from_page, name='SNP_search_from_page'),
    path(r'SNP_detail_page/<int:SNP_ID>/', views.SNP_detail_page, name='SNP_detail_page'),
    path(r'SNP_result_page/<str:recherche>/<int:type>', views.SNP_result_page, name='SNP_result_page')
]
