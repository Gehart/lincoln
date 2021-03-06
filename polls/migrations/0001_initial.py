# Generated by Django 3.0.4 on 2020-03-31 14:46

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('tag_image', models.FileField(blank=True, null=True, upload_to='categories/%Y/')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_pub', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(db_index=True, max_length=200)),
                ('title_detail', models.CharField(db_index=True, max_length=300)),
                ('slug', models.SlugField(blank=True, max_length=150, unique=True)),
                ('body', ckeditor.fields.RichTextField(blank=True)),
                ('article_image', models.FileField(blank=True, null=True, upload_to='posts/%Y/')),
                ('tags', models.ManyToManyField(blank=True, related_name='posts', to='polls.Tag')),
            ],
            options={
                'ordering': ['-date_pub'],
            },
        ),
    ]
