
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0017_instructorinformation_site'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='current_education',
            field=models.CharField(default='none', max_length=4, verbose_name='Current Education', choices=[('orta', 'Middle School'), ('lise', 'High School'), ('univ', 'University'), ('yksk', 'Master'), ('dktr', 'Doctorate'), ('none', 'Not a Student')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='occupation',
            field=models.CharField(default='none', max_length=4, verbose_name='Occupation', choices=[('kamu', 'Public'), ('ozel', 'Private'), ('akdm', 'Academic'), ('none', 'Unoccupied')]),
            preserve_default=False,
        ),
    ]
