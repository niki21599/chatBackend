# Generated by Django 4.0.5 on 2022-06-10 22:29

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('chatBackend', '0004_alter_chat_created_at_alter_message_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 10, 22, 29, 23, 114062, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='message',
            name='chat',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='chatBackend.chat'),
        ),
        migrations.AlterField(
            model_name='message',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 10, 22, 29, 23, 114393, tzinfo=utc)),
        ),
    ]
