from django.db import models
from postgres_copy import CopyManager

# Create your models here.

class witness_for(models.Model):
    PARTY_CHOICES=(
        ('R', 'Republican'),
        ('D', 'Democrat'),
    )
    CHOICES=(
        ('yes', 'Yes'),
        ('no', 'No'),
        ('', 'Pending'),
    )
    COMMITTEE_CHOICES=(
        ('Agriculture, Food Production and Outdoor Resources', 'Agriculture, Food Production and Outdoor Resources'),
        ('Appropriations', 'Appropriations'),
        ('Commerce, Consumer Protection, Energy and the Environment', 'Commerce, Consumer Protection, Energy and the Environment'),
        ('Economic Development', 'Economic Development'),
        ('Education', 'Education'),
        ('Financial and Governmental Organizations and Elections', 'Financial and Governmental Organizations and Elections'),
        ('Fiscal Oversight', 'Fiscal Oversight'),
        ('General Laws', 'General Laws'),
        ('General Laws and Pensions', 'General Laws and Pensions'),
        ('Government Reform', 'Government Reform'),
        ('Governmental Accountability and Fiscal Oversight', 'Governmental Accountability and Fiscal Oversight'),
        ('Health and Pensions', 'Health and Pensions'),
        ('Insurance and Banking', 'Insurance and Banking'),
        ('Jobs, Economic Development and Local Government', 'Jobs, Economic Development and Local Government'),
        ('Judiciary and Civil and Criminal Jurisprudence', 'Judiciary and Civil and Criminal Jurisprudence'),
        ('Local Government and Elections', 'Local Government and Elections'),
        ('Professional Registration', 'Professional Registration'),
        ('Progress and Development', 'Progress and Development'),
        ('Rules, Joint Rules, Resolutions and Ethics', 'Rules, Joint Rules, Resolutions and Ethics'),
        ('Seniors, Families and Children', 'Seniors, Families and Children'),
        ('Seniors, Families and Pensions', 'Seniors, Families and Pensions'),
        ('Small Business and Industry', 'Small Business and Industry'),
        ('Small Business, Insurance and Industry', 'Small Business, Insurance and Industry'),
        ('Transportation and Infrastructure', 'Transportation and Infrastructure'),
        ('Transportation, Infrastructure and Public Safety', 'Transportation, Infrastructure and Public Safety'),
        ('Veterans Affairs and Health', 'Veterans Affairs and Health'),
        ('Veterans and Military Affairs', 'Veterans and Military Affairs'),
        ('Ways and Means', 'Ways and Means'),
    )
    id = models.AutoField(
        primary_key=True,
    )

    year = models.IntegerField()

    bill_no = models.IntegerField()

    bill_sponsor = models.CharField(
        max_length=100,
    )

    party = models.CharField(
        max_length=1,
        choices=PARTY_CHOICES
    )
    committee = models.CharField(
        max_length=150,
        choices=COMMITTEE_CHOICES,
    )
    # passed = models.CharField(
    #     max_length=3,
    # )
    witness_for = models.CharField(
        max_length=100,
        null=True,
    )
    witness_for_org = models.CharField(
        max_length=100,
        null=True,
    )
    law = models.CharField(
        max_length=3,
        null=True,
        choices=CHOICES,
    )

    source_file = 'witness_against'

    objects = CopyManager()

class witness_against(models.Model):
    PARTY_CHOICES=(
        ('R', 'Republican'),
        ('D', 'Democrat'),
    )
    CHOICES=(
        ('yes', 'Yes'),
        ('no', 'No'),
        ('None', 'Pending'),
    )
    COMMITTEE_CHOICES=(
        ('Agriculture, Food Production and Outdoor Resources', 'Agriculture, Food Production and Outdoor Resources'),
        ('Appropriations', 'Appropriations'),
        ('Commerce, Consumer Protection, Energy and the Environment', 'Commerce, Consumer Protection, Energy and the Environment'),
        ('Economic Development', 'Economic Development'),
        ('Education', 'Education'),
        ('Financial and Governmental Organizations and Elections', 'Financial and Governmental Organizations and Elections'),
        ('Fiscal Oversight', 'Fiscal Oversight'),
        ('General Laws', 'General Laws'),
        ('General Laws and Pensions', 'General Laws and Pensions'),
        ('Government Reform', 'Government Reform'),
        ('Governmental Accountability and Fiscal Oversight', 'Governmental Accountability and Fiscal Oversight'),
        ('Health and Pensions', 'Health and Pensions'),
        ('Insurance and Banking', 'Insurance and Banking'),
        ('Jobs, Economic Development and Local Government', 'Jobs, Economic Development and Local Government'),
        ('Judiciary and Civil and Criminal Jurisprudence', 'Judiciary and Civil and Criminal Jurisprudence'),
        ('Local Government and Elections', 'Local Government and Elections'),
        ('Professional Registration', 'Professional Registration'),
        ('Progress and Development', 'Progress and Development'),
        ('Rules, Joint Rules, Resolutions and Ethics', 'Rules, Joint Rules, Resolutions and Ethics'),
        ('Seniors, Families and Children', 'Seniors, Families and Children'),
        ('Seniors, Families and Pensions', 'Seniors, Families and Pensions'),
        ('Small Business and Industry', 'Small Business and Industry'),
        ('Small Business, Insurance and Industry', 'Small Business, Insurance and Industry'),
        ('Transportation and Infrastructure', 'Transportation and Infrastructure'),
        ('Transportation, Infrastructure and Public Safety', 'Transportation, Infrastructure and Public Safety'),
        ('Veterans Affairs and Health', 'Veterans Affairs and Health'),
        ('Veterans and Military Affairs', 'Veterans and Military Affairs'),
        ('Ways and Means', 'Ways and Means'),
    )

    id = models.AutoField(
        primary_key=True,
    )

    year = models.IntegerField()

    bill_no = models.IntegerField()

    bill_sponsor = models.CharField(
        max_length=100,
    )

    party = models.CharField(
        max_length=1,
    )
    committee = models.CharField(
        max_length=100,
        choices=COMMITTEE_CHOICES,
    )
    # passed = models.CharField(
    #     max_length=3,
    # )
    witness_against = models.CharField(
        max_length=100,
        null=True,
    )
    witness_against_org = models.CharField(
        max_length=100,
        null=True,
    )
    law = models.CharField(
        max_length=3,
        null=True,
    )

    source_file = 'witness_for'

    objects = CopyManager()
