# Generated by Django 2.2.1 on 2019-05-19 09:40

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
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Topic', models.TextField(max_length=100)),
                ('Discription', models.TextField(max_length=200)),
                ('CreateData', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Message', models.TextField(max_length=300)),
                ('Tine', models.DateTimeField(auto_now=True)),
                ('Resp', models.TextField(blank=True, max_length=200, null=True)),
                ('Board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BoardAPP.Board')),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
