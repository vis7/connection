# Generated by Django 3.1.1 on 2020-10-04 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('newsfeed', '0001_initial'),
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsfeed',
            name='post_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.post'),
        ),
    ]
