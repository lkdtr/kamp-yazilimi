
from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrainessParticipation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('morning', models.CharField(default='0', max_length=3, verbose_name='Sabah', choices=[('-1', 'Kurs Yap\xc4\xb1lmad\xc4\xb1'), ('0', 'Kat\xc4\xb1lmad\xc4\xb1'), ('1', 'Yar\xc4\xb1s\xc4\xb1na Kat\xc4\xb1ld\xc4\xb1'), ('2', 'Kat\xc4\xb1ld\xc4\xb1')])),
                ('afternoon', models.CharField(default='0', max_length=3, verbose_name='Ogleden Sonra', choices=[('-1', 'Kurs Yap\xc4\xb1lmad\xc4\xb1'), ('0', 'Kat\xc4\xb1lmad\xc4\xb1'), ('1', 'Yar\xc4\xb1s\xc4\xb1na Kat\xc4\xb1ld\xc4\xb1'), ('2', 'Kat\xc4\xb1ld\xc4\xb1')])),
                ('evening', models.CharField(default='0', max_length=3, verbose_name='Aksam', choices=[('-1', 'Kurs Yap\xc4\xb1lmad\xc4\xb1'), ('0', 'Kat\xc4\xb1lmad\xc4\xb1'), ('1', 'Yar\xc4\xb1s\xc4\xb1na Kat\xc4\xb1ld\xc4\xb1'), ('2', 'Kat\xc4\xb1ld\xc4\xb1')])),
                ('day', models.CharField(default='1', max_length=20, verbose_name='Gun')),
            ],
        ),
        migrations.AddField(
            model_name='trainesscourserecord',
            name='instapprovedate',
            field=models.DateField(default=datetime.datetime(2016, 6, 8, 16, 13, 21, 509342), null=True, blank=True),
        ),
        migrations.AddField(
            model_name='trainessparticipation',
            name='courserecord',
            field=models.ForeignKey(to='training.TrainessCourseRecord'),
        ),
    ]
