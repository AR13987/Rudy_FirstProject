# Generated by Django 5.1.1 on 2024-10-07 05:06

import django.db.models.deletion
import django.db.models.manager
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_advuser_send_messages'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rubric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=20, unique=True, verbose_name='Название')),
                ('order', models.SmallIntegerField(db_index=True, default=0, verbose_name='Порядок')),
            ],
        ),
        migrations.CreateModel(
            name='SubRubric',
            fields=[
            ],
            options={
                'verbose_name': 'Подрубрика',
                'verbose_name_plural': 'Подрубрики',
                'ordering': ('super_rubric__order', 'super_rubric__name', 'order', 'name'),
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('main.rubric',),
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='SuperRubric',
            fields=[
            ],
            options={
                'verbose_name': 'Надрубрика',
                'verbose_name_plural': 'Надрубрики',
                'ordering': ('order', 'name'),
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('main.rubric',),
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='rubric',
            name='super_rubric',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='main.superrubric', verbose_name='Надрубрика'),
        ),
    ]
