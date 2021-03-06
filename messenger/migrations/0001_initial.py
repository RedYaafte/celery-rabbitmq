# Generated by Django 2.2.4 on 2019-08-08 16:23

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
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.PositiveSmallIntegerField(choices=[(0, 'Evento'), (1, 'Aviso')], default=1)),
                ('priority', models.PositiveSmallIntegerField(choices=[(0, 'Critico'), (1, 'Importante'), (2, 'Normal'), (3, 'Baja')], default=2)),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('read', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('from_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='messages_sent', to=settings.AUTH_USER_MODEL)),
                ('to_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='messages', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
