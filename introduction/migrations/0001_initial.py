# Generated by Django 3.2.5 on 2021-07-13 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClubMembers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('year', models.TextField()),
                ('Course', models.TextField()),
                ('Description', models.TextField()),
                ('Github_URL', models.TextField()),
                ('Atcoder_account', models.TextField()),
            ],
        ),
    ]
