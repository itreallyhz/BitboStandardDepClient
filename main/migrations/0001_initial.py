# Generated by Django 4.2.5 on 2023-10-26 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ResidentInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('address_unit_no', models.CharField(max_length=100, null=True)),
                ('address_phase', models.CharField(max_length=100, null=True)),
                ('address_block_no', models.CharField(max_length=100, null=True)),
                ('address_street_no', models.CharField(max_length=100, null=True)),
                ('address_block', models.CharField(max_length=100, null=True)),
                ('address_subdivision', models.CharField(max_length=100, null=True)),
                ('address_building', models.CharField(max_length=100, null=True)),
                ('qualifier', models.CharField(max_length=100, null=True)),
                ('date_of_birth', models.DateField(null=True)),
                ('place_of_birth', models.CharField(max_length=100, null=True)),
                ('sex', models.CharField(max_length=30, null=True)),
                ('civil_status', models.CharField(max_length=30, null=True)),
                ('is_ofw', models.BooleanField(default=False, null=True)),
                ('occupation', models.CharField(max_length=100, null=True)),
                ('monthly_income', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('income_status', models.CharField(max_length=50, null=True)),
                ('employment_status', models.CharField(max_length=50, null=True)),
                ('place_of_work', models.CharField(max_length=100, null=True)),
                ('date_started_working', models.DateField(null=True)),
                ('citizenship', models.CharField(max_length=100, null=True)),
                ('relation_to_household_head', models.CharField(max_length=100, null=True)),
                ('date_of_arrival', models.DateField(null=True)),
                ('arrival_status', models.BooleanField(default=False, null=True)),
                ('is_indigenous', models.BooleanField(default=False, null=True)),
                ('contact_number', models.CharField(max_length=30, null=True)),
                ('tin_no', models.CharField(max_length=20, null=True)),
                ('sss_no', models.CharField(max_length=20, null=True)),
                ('gsis_no', models.CharField(max_length=20, null=True)),
                ('email_address', models.EmailField(max_length=100, null=True)),
                ('is_registered_voter', models.BooleanField(default=False, null=True)),
                ('voting_precint', models.CharField(max_length=100, null=True)),
                ('previous_residence', models.CharField(max_length=100, null=True)),
                ('educational_attainment', models.CharField(max_length=100, null=True)),
                ('enrollment_status', models.CharField(max_length=25, null=True)),
                ('school_type', models.CharField(max_length=100, null=True)),
                ('persons_staying_in_the_household', models.CharField(max_length=1000, null=True)),
                ('from_what_country', models.CharField(max_length=100, null=True)),
                ('place_of_delivery', models.CharField(max_length=100, null=True)),
                ('birth_attendant', models.CharField(max_length=100, null=True)),
                ('immunization', models.CharField(max_length=100, null=True)),
                ('health_facility_visited_last_six_months', models.CharField(max_length=100, null=True)),
                ('reason_for_visit', models.CharField(max_length=100, null=True)),
                ('disability', models.CharField(max_length=100, null=True)),
                ('disability_citizen_id_no', models.CharField(max_length=100, null=True)),
                ('solo_parent', models.BooleanField(default=False, null=True)),
                ('is_registered_senior_citizen', models.BooleanField(default=False, null=True)),
                ('senior_citizen_id_no', models.CharField(max_length=50, null=True)),
                ('place_of_school', models.CharField(max_length=100, null=True)),
                ('religion', models.CharField(max_length=100, null=True)),
                ('ethnicity', models.CharField(max_length=100, null=True)),
                ('type_of_document', models.CharField(max_length=100, null=True)),
                ('issued_date', models.DateField(null=True)),
                ('where_document_issued', models.CharField(max_length=100, null=True)),
                ('skills_development_training', models.CharField(max_length=100, null=True)),
                ('is_rbi_complete', models.BooleanField(default=False, null=True)),
                ('is_mic_complete', models.BooleanField(default=False, null=True)),
                ('profile_picture', models.CharField(max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('active_flag', models.IntegerField(default=1)),
                ('lot_ownership', models.CharField(max_length=100, null=True)),
                ('blk_lot_phase', models.CharField(max_length=100, null=True)),
                ('address', models.CharField(max_length=250, null=True)),
                ('national_id', models.CharField(max_length=50, null=True)),
                ('blood_type', models.CharField(max_length=20, null=True)),
                ('patient_number', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]