# Generated by Django 4.2.4 on 2023-08-31 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('title_en', models.CharField(max_length=60, null=True)),
                ('title_uz', models.CharField(max_length=60, null=True)),
                ('title_ru', models.CharField(max_length=60, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('description_en', models.TextField(blank=True, null=True)),
                ('description_uz', models.TextField(blank=True, null=True)),
                ('description_ru', models.TextField(blank=True, null=True)),
                ('price', models.FloatField(default=0)),
            ],
        ),
    ]
