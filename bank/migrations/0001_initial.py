# Generated by Django 3.2.7 on 2021-10-02 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=100, unique=True, verbose_name='Unique tag for the bank')),
                ('name', models.CharField(default='unknown', max_length=200, verbose_name='Name of the Bank to be displayed to the user')),
                ('description', models.TextField(blank=True, default='', verbose_name='Description of the bank to be displayed to the user')),
                ('snippet_1', models.TextField(help_text='Used to fill in templates', verbose_name='Custom fact about the bank.')),
                ('snippet_2', models.TextField(help_text='Used to fill in templates', verbose_name='Custom fact about the bank.')),
                ('snippet_3', models.TextField(help_text='Used to fill in templates', verbose_name='Custom fact about the bank.')),
            ],
        ),
    ]
