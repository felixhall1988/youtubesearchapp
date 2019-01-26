# Generated by Django 2.1.5 on 2019-01-25 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channelid', models.TextField(unique=True)),
                ('author', models.TextField(null=True, unique=True)),
                ('title', models.TextField(db_index=True, default='')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('hidden', models.BooleanField(db_index=True, default=False)),
                ('thumbnail', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('youtubeid', models.TextField(unique=True)),
                ('title', models.TextField(default='')),
                ('duration', models.IntegerField(default=0)),
                ('view_count', models.IntegerField(default=0, null=True)),
                ('favorite_count', models.IntegerField(default=0, null=True)),
                ('uploaded', models.DateTimeField(db_index=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField()),
                ('description', models.TextField(default='')),
                ('uploader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='videoapp.Channel')),
            ],
        ),
    ]
