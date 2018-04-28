
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mudur', '0007_auto_20160815_1457'),
        ('userprofile', '0016_auto_20160815_1718'),
    ]

    operations = [
        migrations.AddField(
            model_name='instructorinformation',
            name='site',
            field=models.ForeignKey(default=2, to='mudur.Site'),
            preserve_default=False,
        ),
    ]
