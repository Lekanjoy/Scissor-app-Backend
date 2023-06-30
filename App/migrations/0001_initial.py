# Generated by Django 4.2 on 2023-06-06 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('original_link', models.URLField()),
                ('shortened_link', models.URLField(blank=True, null=True)),
            ],
        ),
    ]