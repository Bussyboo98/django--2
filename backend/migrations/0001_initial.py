# Generated by Django 3.1.1 on 2020-12-15 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(max_length=100, verbose_name='Category Name')),
                ('cat_desc', models.TextField(blank=True, null=True, verbose_name='Description')),
            ],
            options={
                'verbose_name_plural': 'Category',
            },
        ),
    ]
