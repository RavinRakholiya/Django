# Generated by Django 2.1.15 on 2020-06-13 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20200613_1538'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl2cases',
            name='tbl2consultants',
            field=models.ManyToManyField(to='home.tbl2Consultants'),
        ),
        migrations.AddField(
            model_name='tbl2cases',
            name='tbl2healthcenters',
            field=models.ManyToManyField(to='home.tbl2HealthCenters'),
        ),
        migrations.AddField(
            model_name='tbl2cases',
            name='tbl2patientstbl2consultants',
            field=models.ManyToManyField(to='home.tbl2Patients'),
        ),
    ]