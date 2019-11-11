"""
Definition of models.
"""

from django.db import models
from django.utils import timezone
from django.utils.dateparse import parse_date       #Pour les dates

# Create your models here.

class SNP(models.Model):
    SNP_ID = models.IntegerField(primary_key=True, default="", editable=False)
    CHR_ID = models.TextField(blank=True, null=True)
    CHR_POS = models.IntegerField(default=0, blank=True, null=True)
    SNPS = models.TextField(blank=True, null=True)
    SNP_ID_CURRENT = models.IntegerField(blank=True, null=True)

    def seed():
        fichier = open("gwas_catalog_v1.0-associations_e96_r2019-09-24_european_nature_genetics_1000_ID.tsv")
        for line in fichier:
            line = line.split("\t")

            if(line[0] ==  "PUBMEDID"):
                continue

            element = SNP(SNP_ID = int(line[18]))
            element.CHR_ID = line[9]
            element.SNPS = line[12]
            try:    
                element.CHR_POS = int(line[10])
            except ValueError:
                print("Position éronné, id:",  line[18])
            try:    
                element.SNP_ID_CURRENT = int(line[13])
            except ValueError:
                print("SNP_ID_CURRRENT éronné, id:",  line[18])
            element.save()

class REFERENCE(models.Model):
    REFERENCE_ID = models.IntegerField(primary_key=True, default="", editable=False)
    PUBMEDID = models.TextField(blank=True)
    FIRST_AUTHOR = models.TextField (max_length=100, blank=True, null=True)
    DATE = models.DateField(blank=True, null=True)
    JOURNAL = models.TextField (max_length=100, blank=True, null=True)
    LINK = models.TextField (max_length=100, blank=True, null=True)
    STUDY = models.TextField (max_length=100, blank=True, null=True)  

    def seed():
        fichier = open("gwas_catalog_v1.0-associations_e96_r2019-09-24_european_nature_genetics_1000_ID.tsv")
        for line in fichier:
            line = line.split("\t")
            if(line[0] ==  "PUBMEDID"):      #Pour ne pas récupérer la premiere ligne qui contient les headers
                continue
            element = REFERENCE(REFERENCE_ID = int(line[18]))
            
            PUBMEDID = line[0]
            try:
                element.DATE = parse_date(line[2])
            except :
                print("Date éronné :" ,line[12])
            element.FIRST_AUTHOR = line[1]
            element.JOURNAL = line[3]
            element.LINK = line[4]
            element.STUDY = line[5]
            element.save()

class PHENOTYPE(models.Model):
    PHENOTYPE_ID = models.IntegerField(primary_key=True, default="", editable=False)
    DISEASE_TRAIT = models.TextField (max_length=100, blank=True, null=True)
    
    def seed():
        fichier = open("gwas_catalog_v1.0-associations_e96_r2019-09-24_european_nature_genetics_1000_ID.tsv")
        for line in fichier:
            line = line.split("\t")
            if(line[0] ==  "PUBMEDID"):      #Pour ne pas récupérer la premiere ligne qui contient les headers
                continue
            element = PHENOTYPE(PHENOTYPE_ID = int(line[18]))
            element.DISEASE_TRAIT = line[6]
            element.save()

class PVAL(models.Model):
    ID = models.IntegerField(primary_key=True, default="", editable=False)
    PVALUE = models.DecimalField (max_length=100, blank=True, null=True, max_digits=22, decimal_places=20)
    PVALUE_MLOG = models.DecimalField (max_length=100, blank=True, null=True, max_digits=5, decimal_places=2)
    
    def seed():
        fichier = open("gwas_catalog_v1.0-associations_e96_r2019-09-24_european_nature_genetics_1000_ID.tsv")
        for line in fichier:
            line = line.split("\t")
            if(line[0] ==  "PUBMEDID"):      #Pour ne pas récupérer la premiere ligne qui contient les headers
                continue
            element = PVAL(ID = int(line[18]))
            try:
                element.PVALUE = float(line[16])
                element.PVALUE_MLOG = float(line[17])
            except ValueError:
                print("mauvaise donnée, id:",  line[18])
            element.save()