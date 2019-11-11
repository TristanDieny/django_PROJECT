# Generated by Django 2.2.5 on 2019-10-09 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PHENOTYPE',
            fields=[
                ('PHENOTYPE_ID', models.IntegerField(default='', editable=False, primary_key=True, serialize=False)),
                ('DISEASE_TRAIT', models.TextField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PVAL',
            fields=[
                ('ID', models.IntegerField(default='', editable=False, primary_key=True, serialize=False)),
                ('PVALUE', models.DecimalField(blank=True, decimal_places=2, max_digits=5, max_length=100, null=True)),
                ('PVALUE_MLOG', models.DecimalField(blank=True, decimal_places=2, max_digits=5, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='REFERENCE',
            fields=[
                ('REFERENCE_ID', models.IntegerField(default='', editable=False, primary_key=True, serialize=False)),
                ('PUBMEDID', models.BigIntegerField(blank=True)),
                ('FIRST_AUTHOR', models.TextField(blank=True, max_length=100, null=True)),
                ('DATE', models.DateField(blank=True, null=True)),
                ('JOURNAL', models.TextField(blank=True, max_length=100, null=True)),
                ('LINK', models.TextField(blank=True, max_length=100, null=True)),
                ('STUDY', models.TextField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SNP',
            fields=[
                ('SNP_ID', models.IntegerField(default='', editable=False, primary_key=True, serialize=False)),
                ('CHR_ID', models.TextField(blank=True, null=True)),
                ('CHR_POS', models.IntegerField(blank=True, default=0, null=True)),
                ('SNPS', models.TextField(blank=True, null=True)),
                ('SNP_ID_CURRENT', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
