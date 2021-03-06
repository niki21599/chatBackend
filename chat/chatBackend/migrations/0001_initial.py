# Generated by Django 4.0.5 on 2022-06-09 09:03

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(default=datetime.date.today)),
                ('user_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_1', to=settings.AUTH_USER_MODEL)),
                ('user_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_2', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=500)),
                ('created_at', models.DateField(default=datetime.date.today)),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chatBackend.chat')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender_message_set', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
