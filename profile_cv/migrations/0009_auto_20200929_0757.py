# Generated by Django 3.1.1 on 2020-09-29 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_cv', '0008_auto_20200929_0740'),
    ]

    operations = [
        migrations.CreateModel(
            name='Technical_Skills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('technical', models.CharField(max_length=250)),
                ('skill', models.CharField(max_length=250)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.AddField(
            model_name='draco_profile',
            name='skills',
            field=models.ManyToManyField(blank=True, related_name='my_skills', to='profile_cv.Technical_Skills'),
        ),
    ]
