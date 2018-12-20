# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-12-18 20:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('squares', '0002_auto_20181218_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='squaresproposed',
            name='assigned_squares',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='squaresproposed',
            name='q1_winning_square',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='squaresproposed',
            name='q1_winning_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='q1_winning_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='squaresproposed',
            name='q2_winning_square',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='squaresproposed',
            name='q2_winning_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='q2_winning_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='squaresproposed',
            name='q3_winning_square',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='squaresproposed',
            name='q3_winning_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='q3_winning_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='squaresproposed',
            name='q4_winning_square',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='squaresproposed',
            name='q4_winning_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='q4_winning_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='squaresproposed',
            name='shit_22_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shit_22_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='squaresproposed',
            name='shit_55_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shit_55_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='squaresproposed',
            name='shit_99_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shit_99_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
