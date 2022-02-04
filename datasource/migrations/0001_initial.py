# Generated by Django 3.2.12 on 2022-02-04 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('brand', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Datasource',
            fields=[
                ('brand_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='brand.brand')),
                ('source_id', models.CharField(help_text='the original identifier used by the datasource. i.e wikiid, or banktrack tag', max_length=100, unique=True)),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bank_brand', to='brand.brand')),
            ],
            bases=('brand.brand',),
        ),
        migrations.CreateModel(
            name='Banktrack',
            fields=[
                ('datasource_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='datasource.datasource')),
            ],
            bases=('datasource.datasource',),
        ),
        migrations.CreateModel(
            name='Bimpact',
            fields=[
                ('datasource_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='datasource.datasource')),
            ],
            bases=('datasource.datasource',),
        ),
        migrations.CreateModel(
            name='Bocc',
            fields=[
                ('datasource_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='datasource.datasource')),
            ],
            bases=('datasource.datasource',),
        ),
        migrations.CreateModel(
            name='Fairfinance',
            fields=[
                ('datasource_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='datasource.datasource')),
            ],
            bases=('datasource.datasource',),
        ),
        migrations.CreateModel(
            name='Gabv',
            fields=[
                ('datasource_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='datasource.datasource')),
            ],
            bases=('datasource.datasource',),
        ),
        migrations.CreateModel(
            name='Marketforces',
            fields=[
                ('datasource_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='datasource.datasource')),
            ],
            bases=('datasource.datasource',),
        ),
        migrations.CreateModel(
            name='Switchit',
            fields=[
                ('datasource_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='datasource.datasource')),
            ],
            bases=('datasource.datasource',),
        ),
        migrations.CreateModel(
            name='Usnic',
            fields=[
                ('datasource_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='datasource.datasource')),
            ],
            bases=('datasource.datasource',),
        ),
        migrations.CreateModel(
            name='Wikidata',
            fields=[
                ('datasource_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='datasource.datasource')),
            ],
            bases=('datasource.datasource',),
        ),
    ]
