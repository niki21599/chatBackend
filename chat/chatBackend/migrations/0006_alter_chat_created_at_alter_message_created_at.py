# Generated by Django 4.0.5 on 2023-02-22 15:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('chatBackend', '0005_alter_chat_created_at_alter_message_chat_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 22, 15, 9, 2, 216917, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='message',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 22, 15, 9, 2, 217213, tzinfo=utc)),
        ),
    ]
