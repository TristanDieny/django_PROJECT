"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from django.db import models
from app.models import SNP, REFERENCE, PHENOTYPE, PVAL

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Accueil',
            'year':datetime.now().year,
        }
    )

def phenotype_list_page (request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/phenotype_list_page.html',
        {
            'title':'Liste des phénotypes',
            'year':datetime.now().year,
            'ligne' : PHENOTYPE.objects.all(),
        }
    )

def phenotype_detail_page (request, maladieID):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/phenotype_detail_page.html',
        {
            'title':'Liste détaillées des phénotypes',
            'year':datetime.now().year,
            'maladieID': maladieID,
            'PHENOTYPE' : PHENOTYPE.objects.all(),
            'REFERENCE' : REFERENCE.objects.raw('SELECT * FROM app_REFERENCE, app_PHENOTYPE, app_SNP WHERE REFERENCE_ID = PHENOTYPE_ID AND REFERENCE_ID = SNP_ID ')
        }
    )

def SNP_search_from_page(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/SNP_search_from_page.html',
        {
            'title':'SNP search page',
            'PHENOTYPE' : PHENOTYPE.objects.all(),
            'CHR' : SNP.objects.raw('SELECT SNP_ID, CHR_ID FROM app_SNP'),
            'year':datetime.now().year,
        }
    )


def SNP_detail_page(request, SNP_ID):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/SNP_detail_page.html',
        {
            'title': 'SNP detail page',
            'snp_ID': SNP_ID,
            'requete' : SNP.objects.raw('SELECT * FROM app_PVAL, app_PHENOTYPE, app_SNP WHERE app_PVAL.ID = PHENOTYPE_ID AND  PHENOTYPE_ID = SNP_ID '),
            'year':datetime.now().year,
        }
    )

def SNP_result_page(request, recherche, type):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)

    if type == 1:
        requete = SNP.objects.raw('SELECT * FROM  app_PHENOTYPE, app_SNP WHERE PHENOTYPE_ID = SNP_ID AND app_PHENOTYPE.DISEASE_TRAIT = %s', [recherche])
    elif type == 2:
        requete = SNP.objects.raw('SELECT * FROM  app_PHENOTYPE, app_SNP WHERE PHENOTYPE_ID = SNP_ID AND app_SNP.CHR_ID = %s', [recherche])
    else:
        recherche = int(recherche)
        requete = SNP.objects.raw('SELECT * FROM  app_PHENOTYPE, app_SNP WHERE PHENOTYPE_ID = SNP_ID AND app_SNP.SNP_ID_CURRENT = %s', [recherche])
    
    return render(
        request,
        'app/SNP_result_page.html',
        {
            'title': 'SNP result page',
            'recherche': recherche,
            'requete' : requete,         
            'year':datetime.now().year,
        }
    )