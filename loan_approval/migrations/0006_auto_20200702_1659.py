# Generated by Django 3.0.6 on 2020-07-02 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan_approval', '0005_auto_20200702_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='behaviorscore',
            name='M0FreqL3M_WOE',
            field=models.FloatField(blank=True, default=None, max_length=100, null=True, verbose_name='M0FreqL3M_WOE'),
        ),
        migrations.AlterField(
            model_name='behaviorscore',
            name='M1FreqL12M_Bin_WOE',
            field=models.FloatField(blank=True, default=None, max_length=100, null=True, verbose_name='M1FreqL12M_Bin_WOE'),
        ),
        migrations.AlterField(
            model_name='behaviorscore',
            name='M1FreqL6M_Bin_WOE',
            field=models.FloatField(blank=True, default=None, max_length=100, null=True, verbose_name='M1FreqL6M_Bin_WOE'),
        ),
        migrations.AlterField(
            model_name='behaviorscore',
            name='M2FreqL3M_Bin_WOE',
            field=models.FloatField(blank=True, default=None, max_length=100, null=True, verbose_name='M2FreqL3M_Bin_WOE'),
        ),
        migrations.AlterField(
            model_name='behaviorscore',
            name='avgPayL6M_Bin_WOE',
            field=models.FloatField(blank=True, default=None, max_length=100, null=True, verbose_name='avgPayL6M_Bin_WOE'),
        ),
        migrations.AlterField(
            model_name='behaviorscore',
            name='avgUrateL1M_Bin_WOE',
            field=models.FloatField(blank=True, default=None, max_length=100, null=True, verbose_name='avgUrateL1M_Bin_WOE'),
        ),
        migrations.AlterField(
            model_name='behaviorscore',
            name='avgUrateL3M_Bin_WOE',
            field=models.FloatField(blank=True, default=None, max_length=100, null=True, verbose_name='avgUrateL3M_Bin_WOE'),
        ),
        migrations.AlterField(
            model_name='behaviorscore',
            name='increaseUrateL6M_Bin_WOE',
            field=models.FloatField(blank=True, default=None, max_length=100, null=True, verbose_name='increaseUrateL6M_Bin_WOE'),
        ),
        migrations.AlterField(
            model_name='behaviorscore',
            name='intercept',
            field=models.FloatField(blank=True, default=None, max_length=100, null=True, verbose_name='intercept'),
        ),
        migrations.AlterField(
            model_name='behaviorscore',
            name='label',
            field=models.FloatField(blank=True, default=None, max_length=100, null=True, verbose_name='label'),
        ),
        migrations.AlterField(
            model_name='behaviorscore',
            name='maxDelqL1M_Bin_WOE',
            field=models.FloatField(blank=True, default=None, max_length=100, null=True, verbose_name='maxDelqL1M_Bin_WOE'),
        ),
        migrations.AlterField(
            model_name='behaviorscore',
            name='maxDelqL3M_Bin_WOE',
            field=models.FloatField(blank=True, default=None, max_length=100, null=True, verbose_name='maxDelqL3M_Bin_WOE'),
        ),
    ]