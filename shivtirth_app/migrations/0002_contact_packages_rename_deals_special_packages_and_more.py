# Generated by Django 5.1.1 on 2025-05-08 16:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shivtirth_app', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Packages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('desc', models.CharField(max_length=150)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.RenameModel(
            old_name='Deals',
            new_name='Special_Packages',
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-date_created']},
        ),
        migrations.RemoveField(
            model_name='post',
            name='img1',
        ),
        migrations.RemoveField(
            model_name='post',
            name='img2',
        ),
        migrations.RemoveField(
            model_name='post',
            name='img3',
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='shivtirth_app.post')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
