# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-12-18 20:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bets', '0005_auto_20181217_1638'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofilebetsaudit',
            options={'verbose_name': 'User Profile Bets Audit', 'verbose_name_plural': 'User Profile Bets Audits'},
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='current_bets_balance',
            field=models.IntegerField(default=0, help_text="The user's current balance. Every time the user settles up,        the current prop bets balance is reset to zero."),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='overall_bets_winnings',
            field=models.IntegerField(default=0, help_text="The user's overall prop bets winnings since joining."),
        ),
        migrations.AlterField(
            model_name='userprofilebetsaudit',
            name='admin_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile_bets_admin', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userprofilebetsaudit',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile_bets_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
