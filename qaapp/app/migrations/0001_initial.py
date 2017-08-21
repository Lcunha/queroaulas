# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('nome', models.CharField(max_length=80)),
                ('telefone', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('dataNascimento', models.DateField()),
                ('cpf', models.BigIntegerField()),
            ],
        ),
    ]
