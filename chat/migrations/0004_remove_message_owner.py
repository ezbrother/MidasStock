# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_auto_20150619_0153'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='owner',
        ),
    ]
