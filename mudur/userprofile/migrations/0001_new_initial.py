# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-21 22:56
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import userprofile.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mudur', '0001_new_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accommodation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('E', 'Erkek'), ('K', 'Kadin'), ('H', 'Hepsi')], max_length=1, verbose_name='Gender')),
                ('usertype', models.CharField(choices=[('inst', 'instructor'), ('stu', 'student'), ('hepsi', 'hepsi')], max_length=15, verbose_name='User Type')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('address', models.CharField(max_length=300, verbose_name='Address')),
                ('website', models.CharField(max_length=300, verbose_name='Website')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mudur.Site')),
            ],
            options={
                'verbose_name': 'Accommodation',
                'verbose_name_plural': 'Accommodations',
            },
        ),
        migrations.CreateModel(
            name='InstructorInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transportation', models.CharField(choices=[('0', 'Uçak'), ('1', 'Otobüs'), ('2', 'Araba'), ('3', 'Diğer')], max_length=1, verbose_name='Transportation')),
                ('additional_information', models.CharField(max_length=300, null=True, verbose_name='Additional Information')),
                ('arrival_date', models.DateField(default=datetime.date.today, verbose_name='Arrival Date')),
                ('departure_date', models.DateField(default=datetime.date.today, verbose_name='Departure Date')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mudur.Site')),
            ],
            options={
                'verbose_name': 'Instructor Additional Information',
                'verbose_name_plural': 'Instructor Additional Information',
            },
        ),
        migrations.CreateModel(
            name='TrainessClassicTestAnswers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=2000, verbose_name='Cevap')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mudur.TextBoxQuestions', verbose_name='Soru')),
            ],
            options={
                'verbose_name': 'Trainess Answer for Classic Question',
                'verbose_name_plural': 'Trainess Answers for Classic Questions ',
            },
        ),
        migrations.CreateModel(
            name='TrainessNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.CharField(max_length=500, verbose_name='Note')),
                ('note_date', models.DateTimeField(default=datetime.datetime.now)),
                ('label', models.CharField(max_length=50, verbose_name='Label')),
            ],
            options={
                'verbose_name': 'Trainess Note',
                'verbose_name_plural': 'Trainess Notes',
            },
        ),
        migrations.CreateModel(
            name='UserAccomodationPref',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usertype', models.CharField(choices=[('inst', 'instructor'), ('stu', 'student'), ('hepsi', 'hepsi')], max_length=30, verbose_name='User Type')),
                ('preference_order', models.SmallIntegerField(default=1)),
                ('approved', models.BooleanField(default=False)),
                ('accomodation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userprofile.Accommodation')),
            ],
            options={
                'verbose_name': 'Participant Accommodation Preference',
                'verbose_name_plural': 'Participant Accommodation Preferences',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birthdate', models.DateField(default=datetime.date(1970, 1, 1), verbose_name='Birth Date')),
                ('tckimlikno', models.CharField(blank=True, max_length=11, verbose_name='TC Identity Number')),
                ('ykimlikno', models.CharField(blank=True, max_length=11, verbose_name='Foreign Identity Number')),
                ('gender', models.CharField(choices=[('E', 'Male'), ('K', 'Female')], max_length=1, verbose_name='Gender')),
                ('mobilephonenumber', models.CharField(max_length=14, verbose_name='Mobile Phone Number')),
                ('address', models.TextField(verbose_name='Home Address')),
                ('job', models.CharField(blank=True, max_length=40, null=True, verbose_name='Job')),
                ('city', models.CharField(max_length=40, verbose_name='Current City')),
                ('country', django_countries.fields.CountryField(default='TR', max_length=2, verbose_name='Nationality')),
                ('title', models.CharField(max_length=40, verbose_name='Title')),
                ('occupation', models.CharField(choices=[('kamu', 'Public'), ('ozel', 'Private'), ('akdm', 'Academic'), ('none', 'Unoccupied')], max_length=4, verbose_name='Occupation')),
                ('current_education', models.CharField(choices=[('orta', 'Middle School'), ('lise', 'High School'), ('univ', 'University'), ('yksk', 'Master'), ('dktr', 'Doctorate'), ('none', 'Not a Student')], max_length=4, verbose_name='Current Education')),
                ('organization', models.CharField(blank=True, max_length=200, null=True, verbose_name='Organization')),
                ('university', models.CharField(blank=True, choices=[('Abant İzzet Baysal Üniversitesi (Bolu)', 'Abant İzzet Baysal Üniversitesi (Bolu)'), ('Abdullah Gül Üniversitesi (Kayseri)', 'Abdullah Gül Üniversitesi (Kayseri)'), ('Acıbadem Üniversitesi (İstanbul)', 'Acıbadem Üniversitesi (İstanbul)'), ('Adana Bilim ve Teknoloji Üniversitesi (Adana)', 'Adana Bilim ve Teknoloji Üniversitesi (Adana)'), ('Adıyaman Üniversitesi (Adıyaman)', 'Adıyaman Üniversitesi (Adıyaman)'), ('Adnan Menderes Üniversitesi (Aydın)', 'Adnan Menderes Üniversitesi (Aydın)'), ('Afyon Kocatepe Üniversitesi(Afyon)', 'Afyon Kocatepe Üniversitesi(Afyon)'), ('Ağrı İbrahim Çeçen Üniversitesi(Ağrı)', 'Ağrı İbrahim Çeçen Üniversitesi(Ağrı)'), ('Ahi Evran Üniversitesi(Kırşehir)', 'Ahi Evran Üniversitesi(Kırşehir)'), ('Akdeniz Üniversitesi (Antalya)', 'Akdeniz Üniversitesi (Antalya)'), ('Aksaray Üniversitesi (Aksaray)', 'Aksaray Üniversitesi (Aksaray)'), ('Alanya Alaaddin Keykubat Üniversitesi (Antalya)', 'Alanya Alaaddin Keykubat Üniversitesi (Antalya)'), ('Amasya Üniversitesi (Amasya)', 'Amasya Üniversitesi (Amasya)'), ('Anadolu Üniversitesi (Eskişehir)', 'Anadolu Üniversitesi (Eskişehir)'), ('Ankara Sosyal Bilimler Üniversitesi(Ankara)', 'Ankara Sosyal Bilimler Üniversitesi(Ankara)'), ('Ankara Üniversitesi(Ankara)', 'Ankara Üniversitesi(Ankara)'), ('Ardahan Üniversitesi(Ardahan)', 'Ardahan Üniversitesi(Ardahan)'), ('Artvin Çoruh Üniversitesi(Artvin)', 'Artvin Çoruh Üniversitesi(Artvin)'), ('Ataşehir Adıgüzel Meslek Yüksekokulu(İstanbul)', 'Ataşehir Adıgüzel Meslek Yüksekokulu(İstanbul)'), ('Atatürk Üniversitesi (Erzurum)', 'Atatürk Üniversitesi (Erzurum)'), ('Atılım Üniversitesi (Ankara)', 'Atılım Üniversitesi (Ankara)'), ('Avrasya Üniversitesi (Trabzon)', 'Avrasya Üniversitesi (Trabzon)'), ('Avrupa Meslek Yüksek Okulu (İstanbul)', 'Avrupa Meslek Yüksek Okulu (İstanbul)'), ('Bahçeşehir Üniversitesi(İstanbul)', 'Bahçeşehir Üniversitesi(İstanbul)'), ('Balıkesir Üniversitesi(Balıkesir)', 'Balıkesir Üniversitesi(Balıkesir)'), ('Bandırma Onyedi Eylül Üniversitesi(Balıkesir)', 'Bandırma Onyedi Eylül Üniversitesi(Balıkesir)'), ('Bartın Üniversitesi(Bartın)', 'Bartın Üniversitesi(Bartın)'), ('Başkent Üniversitesi (Ankara)', 'Başkent Üniversitesi (Ankara)'), ('Batman Üniversitesi (Batman)', 'Batman Üniversitesi (Batman)'), ('Bayburt Üniversitesi (Bayburt)', 'Bayburt Üniversitesi (Bayburt)'), ('Beykent Üniversitesi (İstanbul)', 'Beykent Üniversitesi (İstanbul)'), ('Beykoz Lojistik Meslek Yüksek Okulu (İstanbul)', 'Beykoz Lojistik Meslek Yüksek Okulu (İstanbul)'), ('Bezm-i Âlem Vakıf Üniversitesi (İstanbul)', 'Bezm-i Âlem Vakıf Üniversitesi (İstanbul)'), ('Bilecik Şeyh Edebali Üniversitesi (Bilecik)', 'Bilecik Şeyh Edebali Üniversitesi (Bilecik)'), ('Bilkent Üniversitesi (Ankara)', 'Bilkent Üniversitesi (Ankara)'), ('Bingöl Üniversitesi (Bingöl)', 'Bingöl Üniversitesi (Bingöl)'), ('Biruni Üniversitesi (İstanbul)', 'Biruni Üniversitesi (İstanbul)'), ('Bitlis Eren Üniversitesi (Bitlis)', 'Bitlis Eren Üniversitesi (Bitlis)'), ('Boğaziçi Üniversitesi (İstanbul)', 'Boğaziçi Üniversitesi (İstanbul)'), ('Bozok Üniversitesi (Yozgat)', 'Bozok Üniversitesi (Yozgat)'), ('Bursa Orhangazi Üniversitesi (Bursa)', 'Bursa Orhangazi Üniversitesi (Bursa)'), ('Bursa Teknik Üniversitesi (Bursa)', 'Bursa Teknik Üniversitesi (Bursa)'), ('Bülent Ecevit Üniversitesi (Zonguldak)', 'Bülent Ecevit Üniversitesi (Zonguldak)'), ('Canik Başarı Üniversitesi (Samsun)', 'Canik Başarı Üniversitesi (Samsun)'), ('Celâl Bayar Üniversitesi (Manisa)', 'Celâl Bayar Üniversitesi (Manisa)'), ('Cumhuriyet Üniversitesi (Sivas)', 'Cumhuriyet Üniversitesi (Sivas)'), ('Çağ Üniversitesi (Tarsus-İçel)', 'Çağ Üniversitesi (Tarsus-İçel)'), ('Çanakkale Onsekiz Mart Üniversitesi(Çanakkale)', 'Çanakkale Onsekiz Mart Üniversitesi(Çanakkale)'), ('Çankaya Üniversitesi (Ankara)', 'Çankaya Üniversitesi (Ankara)'), ('Çankırı Karatekin Üniversitesi (Çankırı)', 'Çankırı Karatekin Üniversitesi (Çankırı)'), ('Çukurova Üniversitesi (Adana)', 'Çukurova Üniversitesi (Adana)'), ('Dicle Üniversitesi (Diyarbakır)', 'Dicle Üniversitesi (Diyarbakır)'), ('Doğuş Üniversitesi (İstanbul)', 'Doğuş Üniversitesi (İstanbul)'), ('Dokuz Eylül Üniversitesi (İzmir)', 'Dokuz Eylül Üniversitesi (İzmir)'), ('Dumlupınar Üniversitesi (Kütahya)', 'Dumlupınar Üniversitesi (Kütahya)'), ('Düzce Üniversitesi (Düzce)', 'Düzce Üniversitesi (Düzce)'), ('Ege Üniversitesi (İzmir)', 'Ege Üniversitesi (İzmir)'), ('Erciyes Üniversitesi (Kayseri)', 'Erciyes Üniversitesi (Kayseri)'), ('Erzincan Üniversitesi (Erzincan)', 'Erzincan Üniversitesi (Erzincan)'), ('Erzurum Teknik Üniversitesi (Erzurum)', 'Erzurum Üniversitesi (Erzurum)'), ('Eskişehir Osmangazi Üniversitesi (Eskişehir)', 'Eskişehir Osmangazi Üniversitesi (Eskişehir)'), ('Faruk Saraç Tasarım Meslek Yüksek Okulu (Bursa)', 'Faruk Saraç Tasarım Meslek Yüksek Okulu (Bursa)'), ('Fatih Sultan Mehmet Vakıf Üniversitesi (İstanbul)', 'Fatih Sultan Mehmet Vakıf Üniversitesi (İstanbul)'), ('Fatih Üniversitesi (İstanbul)', 'Fatih Üniversitesi (İstanbul)'), ('Fırat Üniversitesi (Elazığ)', 'Fırat Üniversitesi (Elazığ)'), ('Galatasaray Üniversitesi (İstanbul)', 'Galatasaray Üniversitesi (İstanbul)'), ('Gazi Üniversitesi (Ankara)', 'Gazi Üniversitesi (Ankara)'), ('Gaziantep Üniversitesi(Gaziantep)', 'Gaziantep Üniversitesi(Gaziantep)'), ('Gaziosmanpaşa Üniversitesi (Tokat)', 'Gaziosmanpaşa Üniversitesi (Tokat)'), ('Gebze Yüksek Teknoloji Enstitüsü(İzmit-Kocaeli)', 'Gebze Yüksek Teknoloji Enstitüsü(İzmit-Kocaeli)'), ('Gedik Üniversitesi (İstanbul)', 'Gedik Üniversitesi (İstanbul)'), ('Gediz Üniversitesi (İzmir)', 'Gediz Üniversitesi (İzmir)'), ('Giresun Üniversitesi (Giresun)', 'Giresun Üniversitesi (Giresun)'), ('Gümüşhane Üniversitesi (Gümüşhane)', 'Gümüşhane Üniversitesi (Gümüşhane)'), ('Hacettepe Üniversitesi (Ankara)', 'Hacettepe Üniversitesi (Ankara)'), ('Hakkari Üniversitesi (Hakkari)', 'Hakkari Üniversitesi (Hakkari)'), ('Haliç Üniversitesi(İstanbul)', 'Haliç Üniversitesi(İstanbul)'), ('Harran Üniversitesi (Şanlıurfa)', 'Harran Üniversitesi (Şanlıurfa)'), ('Hasan Kalyoncu Üniversitesi (Gaziantep)', 'Hasan Kalyoncu Üniversitesi (Gaziantep)'), ('Hitit Üniversitesi (Çorum)', 'Hitit Üniversitesi (Çorum)'), ('Iğdır Üniversitesi (Iğdır)', 'Iğdır Üniversitesi (Iğdır)'), ('Işık Üniversitesi (İstanbul)', 'Işık Üniversitesi (İstanbul)'), ('İnönü Üniversitesi (Malatya)', 'İnönü Üniversitesi (Malatya)'), ('İpek Üniversitesi (Ankara)', 'İpek Üniversitesi (Ankara)'), ('İskenderun Teknik Üniversitesi (Hatay)', 'İskenderun Teknik Üniversitesi (Hatay)'), ('İstanbul Arel Üniversitesi(İstanbul)', 'İstanbul Arel Üniversitesi(İstanbul)'), ('İstanbul Aydın Üniversitesi(İstanbul)', 'İstanbul Aydın Üniversitesi(İstanbul)'), ('İstanbul Üniversitesi(İstanbul)', 'İstanbul Üniversitesi(İstanbul)'), ('İstanbul Bilgi Üniversitesi(İstanbul)', 'İstanbul Bilgi Üniversitesi(İstanbul)'), ('İstanbul Bilim Üniversitesi(İstanbul)', 'İstanbul Bilim Üniversitesi(İstanbul)'), ('İstanbul Esenyurt Üniversitesi(İstanbul)', 'İstanbul Esenyurt Üniversitesi(İstanbul)'), ('İstanbul Gelişim Üniversitesi(İstanbul)', 'İstanbul Gelişim Üniversitesi(İstanbul)'), ('İstanbul Kavram Meslek Yüksek Okulu(İstanbul)', 'İstanbul Kavram Meslek Yüksek Okulu(İstanbul)'), ('İstanbul Kemerburgaz Üniversitesi(İstanbul)', 'İstanbul Kemerburgaz Üniversitesi(İstanbul)'), ('İstanbul Kültür Üniversitesi(İstanbul)', 'İstanbul Kültür Üniversitesi(İstanbul)'), ('İstanbul Medeniyet Üniversitesi(İstanbul)', 'İstanbul Medeniyet Üniversitesi(İstanbul)'), ('İstanbul Medipol Üniversitesi(İstanbul)', 'İstanbul Medipol Üniversitesi(İstanbul)'), ('İstanbul Rumeli Üniversitesi(İstanbul)', 'İstanbul Rumeli Üniversitesi(İstanbul)'), ('İstanbul Sabahattin Zaim Üniversitesi(İstanbul)', 'İstanbul Sabahattin Zaim Üniversitesi(İstanbul)'), ('İstanbul Şehir Üniversitesi(İstanbul)', 'İstanbul Şehir Üniversitesi(İstanbul)'), ('İstanbul Şişli Meslek Yüksek Okulu(İstanbul)', 'İstanbul Şişli Meslek Yüksek Okulu(İstanbul)'), ('İstanbul Teknik Üniversitesi(İstanbul)', 'İstanbul Teknik Üniversitesi(İstanbul)'), ('İstanbul Ticaret Üniversitesi(İstanbul)', 'İstanbul Ticaret Üniversitesi(İstanbul)'), ('İstanbul 29 Mayıs Üniversitesi(İstanbul)', 'İstanbul 29 Mayıs Üniversitesi(İstanbul)'), ('İzmir Yüksek Teknoloji Enstitüsü(İzmir)', 'İzmir Yüksek Teknoloji Enstitüsü(İzmir)'), ('İzmir Ekonomi Üniversitesi(İzmir)', 'İzmir Ekonomi Üniversitesi(İzmir)'), ('İzmir Katip Çelebi Üniversitesi(İzmir)', 'İzmir Katip Çelebi Üniversitesi(İzmir)'), ('İzmir Üniversitesi(İzmir)', 'İzmir Üniversitesi(İzmir)'), ('Kadir Has Üniversitesi(İstanbul)', 'Kadir Has Üniversitesi(İstanbul)'), ('Kafkas Üniversitesi (Kars)', 'Kafkas Üniversitesi (Kars)'), ('Kahramanmaraş Sütçü İmam Üniversitesi(Kahramanmaraş)', 'Kahramanmaraş Sütçü İmam Üniversitesi(Kahramanmaraş)'), ('Kanuni Üniversitesi (Adana)', 'Kanuni Üniversitesi (Adana)'), ('Kapadokya Meslek Yüksek Okulu (Nevşehir)', 'Kapadokya Meslek Yüksek Okulu Üniversitesi (Nevşehir)'), ('Karabuk Universitesi (Karabuk)', 'Karabuk Universitesi (Karabuk)'), ('Karadeniz Teknik Üniversitesi (Trabzon)', 'Karadeniz Teknik Üniversitesi (Trabzon)'), ('Karamanoğlu Mehmetbey Üniversitesi(Karaman)', 'Karamanoğlu Mehmetbey Üniversitesi(Karaman)'), ('Kastamonu Üniversitesi(Kastamonu)', 'Kastamonu Üniversitesi(Kastamonu)'), ('Kırıkkale Üniversitesi(Kırıkkale)', 'Kırıkkale Üniversitesi(Kırıkkale)'), ('Kırklareli Üniversitesi(Kırklareli)', 'Kırklareli Üniversitesi(Kırklareli)'), ('Kilis 7 Aralık Üniversitesi(Kilis)', 'Kilis 7 Aralık Üniversitesi(Kilis)'), ('Kocaeli Üniversitesi(Kocaeli-İzmit)', 'Kocaeli Üniversitesi(Kocaeli-İzmit)'), ('Koç Üniversitesi (İstanbul)', 'Koç Üniversitesi (İstanbul)'), ('Konya Gıda ve Tasarım Üniversitesi (Konya)', 'Konya Gıda ve Tasarım Üniversitesi (Konya)'), ('KTO Karatay Üniversitesi (Konya)', 'KTO Karatay Üniversitesi (Konya)'), ('Mardin Artuklu Üniversitesi (Mardin)', 'Mardin Artuklu Üniversitesi (Mardin)'), ('Maltepe Üniversitesi (İstanbul)', 'Maltepe Üniversitesi (İstanbul)'), ('Marmara Üniversitesi (İstanbul)', 'Marmara Üniversitesi (İstanbul)'), ('MEF Üniversitesi (İstanbul)', 'MEF Üniversitesi (İstanbul)'), ('Mehmet Akif Ersoy Üniversitesi (Burdur)', 'Mehmet Akif Ersoy Üniversitesi (Burdur)'), ('Melikşah Üniversitesi (Kayseri)', 'Melikşah Üniversitesi (Kayseri)'), ('Mersin Üniversitesi(Mersin-İçel)', 'Mersin Üniversitesi(Mersin-İçel)'), ('Mevlana Üniversitesi(Konya)', 'Mevlana Üniversitesi(Konya)'), ('Mimar Sinan Üniversitesi (İstanbul)', 'Mimar Sinan Üniversitesi (İstanbul)'), ('Muğla Üniversitesi(Muğla)', 'Muğla Üniversitesi(Muğla)'), ('Murat\tHüdavendigar Üniversitesi(İstanbul)', 'Murat Hüdavendigar Üniversitesi(İstanbul)'), ('Mustafa Kemal Üniversitesi (Hatay)', 'Mustafa Kemal Üniversitesi (Hatay)'), ('Muş Alparslan Üniversitesi(Muş)', 'Muş Alparslan Üniversitesi(Muş)'), ('Namık Kemal Üniversitesi(Tekirdağ)', 'Namık Kemal Üniversitesi(Tekirdağ)'), ('Necmettin Erbakan Üniversitesi(Konya)', 'Necmettin Erbakan Üniversitesi(Konya)'), ('Nevşehir Hacıbektaş Üniversitesi(Nevşehir)', 'Nevşehir Üniversitesi(Nevşehir)'), ('Niğde Üniversitesi(Niğde)', 'Niğde Üniversitesi(Niğde)'), ('Nişantaşı Üniversitesi(İstanbul)', 'Nişantaşı Üniversitesi(İstanbul)'), ('Nuh Naci Yazgan Üniversitesi(Kayseri)', 'Nuh Naci Yazgan Üniversitesi(Kayseri)'), ('Okan Üniversitesi(İstanbul)', 'Okan Üniversitesi(İstanbul)'), ('Ondokuz Mayıs Üniversitesi (Samsun)', 'Ondokuz Mayıs Üniversitesi (Samsun)'), ('Orta Doğu Teknik Üniversitesi (Ankara)', 'Orta Doğu Teknik Üniversitesi (Ankara)'), ('Ordu Üniversitesi (Ordu)', 'Ordu Üniversitesi (Ordu)'), ('Osmaniye Korkut Ata Üniversitesi (Osmaniye)', 'Osmaniye Korkut Ata Üniversitesi (Osmaniye)'), ('Özyeğin Üniversitesi (İstanbul)', 'Özyeğin Üniversitesi (İstanbul)'), ('Pamukkale Üniversitesi (Denizli)', 'Pamukkale Üniversitesi (Denizli)'), ('Piri Reis Üniversitesi (Denizli)', 'Piri Reis Üniversitesi (Denizli)'), ('Plato Meslek Yüksek Okulu (İstanbul)', 'Plato Meslek Yüksek Okulu (İstanbul)'), ('Recep Tayyip Erdoğan Üniversitesi (Rize)', 'Recep Tayyip Erdoğan Üniversitesi (Rize)'), ('Sabancı Üniversitesi(İstanbul)', 'Sabancı Üniversitesi(İstanbul)'), ('Sağlık Bilimleri Üniversitesi(İstanbul)', 'Sağlık Bilimleri Üniversitesi(İstanbul)'), ('Sakarya Üniversitesi(Sakarya-Adapazarı)', 'Sakarya Üniversitesi(Sakarya-Adapazarı)'), ('Sanko Üniversitesi (Gaziantep)', 'Sanko Üniversitesi (Gaziantep)'), ('Selahaddin Eyyubi Üniversitesi (Diyarbakır)', 'Selahaddin Eyyubi Üniversitesi (Diyarbakır)'), ('Selçuk Üniversitesi (Konya)', 'Selçuk Üniversitesi (Konya)'), ('Siirt Üniversitesi (Siirt)', 'Siirt Üniversitesi (Siirt)'), ('Sinop Üniversitesi (Sinop)', 'Sinop Üniversitesi (Sinop)'), ('Süleyman Demirel Üniversitesi (Isparta)', 'Süleyman Demirel Üniversitesi (Isparta)'), ('Süleyman Şah Üniversitesi (İstanbul)', 'Süleyman Şah Üniversitesi (İstanbul)'), ('Şırnak Üniversitesi (Şırnak)', 'Şırnak Üniversitesi (Şırnak)'), ('Şifa Üniversitesi (İzmir)', 'Şifa Üniversitesi (İzmir)'), ('Trakya Üniversitesi (Edirne)', 'Trakya Üniversitesi (Edirne)'), ('TED Üniversitesi (Ankara)', 'TED Üniversitesi (Ankara)'), ('TOBB Ekonomi ve Teknoloji Üniversitesi(Ankara)', 'TOBB Ekonomi ve Teknoloji Üniversitesi(Ankara)'), ('Toros Üniversitesi (Mersin)', 'Toros Üniversitesi (Mersin)'), ('Trakya Üniversitesi (Edirne)', 'Trakya Üniversitesi (Edirne)'), ('Tunceli Üniversitesi (Tunceli)', 'Tunceli Üniversitesi (Tunceli)'), ('Turgut Özal Üniversitesi (Ankara)', 'Turgut Özal Üniversitesi (Ankara)'), ('Türk Hava Kurumu Üniversitesi (Ankara)', 'Türk Hava Kurumu Üniversitesi (Ankara)'), ('Türk-Alman Üniversitesi (İstanbul)', 'Türk-Alman Üniversitesi (İstanbul)'), ('Ufuk Üniversitesi (Ankara)', 'Ufuk Üniversitesi (Ankara)'), ('Uludağ Üniversitesi (Bursa)', 'Uludağ Üniversitesi (Bursa)'), ('Uluslararası Antalya Üniversitesi (Antalya)', 'Uluslararası Antalya Üniversitesi (Antalya)'), ('Uşak Üniversitesi (Uşak)', 'Uşak Üniversitesi (Uşak)'), ('Üsküdar Üniversitesi (İstanbul)', 'Üsküdar Üniversitesi (İstanbul)'), ('Yalova Üniversitesi (Yalova)', 'Yalova Üniversitesi (Yalova)'), ('Yaşar Üniversitesi (İzmir)', 'Yaşar Üniversitesi (İzmir)'), ('Yeditepe Üniversitesi (İstanbul)', 'Yeditepe Üniversitesi (İstanbul)'), ('Yeni Yüzyıl Üniversitesi (İstanbul)', 'Yeni Yüzyıl Üniversitesi (İstanbul)'), ('Yıldız Teknik Üniversitesi (İstanbul)', 'Yıldız Teknik Üniversitesi (İstanbul)'), ('Yıldırım Beyazıt Üniversitesi (Ankara)', 'Yıldırım Beyazıt Üniversitesi (Ankara)'), ('Yüksek İhtisas Üniversitesi (Ankara)', 'Yüksek İhtisas Üniversitesi (Ankara)'), ('Yüzüncü Yıl Üniversitesi (Van)', 'Yüzüncü Yıl Üniversitesi (Van)'), ('Zirve Üniversitesi (Gaziantep)', 'Zirve Üniversitesi (Gaziantep)'), ('Zonguldak Karaelmas Üniversitesi(Zonguldak)', 'Zonguldak Karaelmas Üniversitesi(Zonguldak)')], max_length=300, verbose_name='University')),
                ('department', models.CharField(max_length=50, verbose_name='Department')),
                ('website', models.CharField(blank=True, max_length=300, null=True, verbose_name='Website')),
                ('experience', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Work Experience')),
                ('profilephoto', models.ImageField(upload_to=userprofile.models.user_directory_path, verbose_name='Profile Picture')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Profile',
                'verbose_name_plural': 'User Profiles',
                'ordering': ('user__username',),
            },
        ),
        migrations.CreateModel(
            name='UserProfileBySite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(blank=True, null=True, upload_to=userprofile.models.user_directory_path, verbose_name='Belge Ekle')),
                ('needs_document', models.BooleanField(default=False, verbose_name='Needs Document')),
                ('userpassedtest', models.BooleanField(default=False, verbose_name='FAQ is answered?')),
                ('additional_information', models.TextField(blank=True, null=True, verbose_name='Additional Information')),
                ('canapply', models.BooleanField(default=False, verbose_name='Can Apply?')),
                ('potentialinstructor', models.BooleanField(default=False, verbose_name='Potential Instructor')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mudur.Site')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Profile By Site',
                'verbose_name_plural': 'User Profiles By Sites',
                'ordering': ('user__username',),
            },
        ),
        migrations.CreateModel(
            name='UserVerification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activation_key', models.CharField(max_length=40, null=True)),
                ('password_reset_key', models.CharField(blank=True, max_length=40, null=True)),
                ('activation_key_expires', models.DateTimeField(blank=True, null=True)),
                ('password_reset_key_expires', models.DateTimeField(blank=True, null=True)),
                ('temporary_code', models.CharField(blank=True, max_length=10, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Verification',
                'verbose_name_plural': 'User Verifications',
            },
        ),
        migrations.AddField(
            model_name='useraccomodationpref',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userprofile.UserProfile'),
        ),
        migrations.AddField(
            model_name='trainessnote',
            name='note_from_profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='note_from_profile', to='userprofile.UserProfile'),
        ),
        migrations.AddField(
            model_name='trainessnote',
            name='note_to_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='note_to_profile', to='userprofile.UserProfile'),
        ),
        migrations.AddField(
            model_name='trainessnote',
            name='site',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mudur.Site'),
        ),
        migrations.AddField(
            model_name='trainessclassictestanswers',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userprofile.UserProfile'),
        ),
        migrations.AddField(
            model_name='instructorinformation',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userprofile.UserProfile'),
        ),
    ]