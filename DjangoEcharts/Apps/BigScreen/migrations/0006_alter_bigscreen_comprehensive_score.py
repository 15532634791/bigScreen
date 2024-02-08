# Generated by Django 4.2 on 2024-01-29 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BigScreen', '0005_alter_bigscreen_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bigscreen',
            name='comprehensive_score',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='综合得分', max_digits=5, null=True),
        ),
    ]
