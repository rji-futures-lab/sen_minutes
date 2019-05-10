from django.shortcuts import render
from django.http import HttpResponse
from minutes_search.helpers import get_access_mo_data
from minutes_search.models import witness_for, witness_against
from django.db.models import (
    F, Func, Max, OuterRef, Subquery, Sum, Count, Case, When, Value, Q
)
from django.db.models.functions import Cast, Coalesce
import requests
from djqscsv import render_to_csv_response

# homepage view
def index(request):
    witness_list = witness_for.objects.order_by('year').values('year').distinct()
    context = { 'witness_list': witness_list }
    return render(request, 'minutes_search/index.html', context)

# simple render function for the guide page of the app
def guide(request):
    return render(request, 'minutes_search/guide.html')

def witness_for_csv(request):
  qs = witness_for.objects.all()
  return render_to_csv_response(qs)

def witness_against_csv(request):
    qs = witness_against.objects.all()
    return render_to_csv_response(qs)

def search_by_bill(request):
    """
    View for the bill search form.

    This view takes a year and a bill number and outputs four lists:
    1: A list of all witnesses in favor of a bill
    2: A list of all witnesses opposing a bill
    3: A list of all organizations testifying in favor of a bill, plus the number of testifiers from said organization
    4: A list of all organizations testifying against a bill, plus the number of testifiers from said organization
    """
    error=False
    if 'year' in request.GET and 'bill_no' in request.GET:
        year_query = request.GET['year']
        bill_query = request.GET['bill_no']
        if not year_query and not bill_query:
            error=True
        elif year_query and bill_query:
            witness_for_list = witness_for.objects.filter(bill_no=bill_query).filter(year=year_query).order_by('witness_for')
            witness_against_list = witness_against.objects.filter(bill_no=bill_query).filter(year=year_query).order_by('witness_against')
            org_for_list = witness_for.objects.filter(bill_no=bill_query).filter(year=year_query).values('witness_for_org').annotate(count=Count('witness_for_org')).order_by('count')
            org_against_list = witness_against.objects.filter(bill_no=bill_query).filter(year=year_query).values('witness_against_org').annotate(count=Count('witness_against_org')).order_by('count')
            context = {
                'witness_for_list': witness_for_list,
                'witness_against_list': witness_against_list,
                'org_for_list': org_for_list,
                'org_against_list': org_against_list,
                'bill_query': bill_query,
                'year_query': year_query,
                'bill_data': get_access_mo_data(bill_query, year_query)
            }
            return render(request, 'minutes_search/bill.html', context)
    return render(request, 'minutes_search/bill.html', {'error': error})

def bill_detail(request, year, bill_no):
    witness_for_list = witness_for.objects.filter(
        bill_no=bill_no, year=year
    ).order_by('witness_for')

    witness_against_list = witness_against.objects.filter(
        bill_no=bill_no, year=year
    ).order_by('witness_against')

    org_for_list = witness_for.objects.filter(
        bill_no=bill_no, year=year
    ).values('witness_for_org').annotate(
        count=Count('witness_for_org')
    ).order_by('count')

    org_against_list = witness_against.objects.filter(
        bill_no=bill_no, year=year).values('witness_against_org').annotate(
        count=Count('witness_against_org')
    ).order_by('count')

    context = {
        'witness_for_list': witness_for_list,
        'witness_against_list': witness_against_list,
        'org_for_list': org_for_list,
        'org_against_list': org_against_list,
        'bill_query': bill_no,
        'year_query': year,
        'bill_data': get_access_mo_data(bill_no, year)
    }
    return render(request, 'minutes_search/bill.html', context)


def search_by_name(request):
    """
    View for the lobbyist search form.

    This view takes a string and outputs two lists:
    1: A list of records where the lobbyist testified for a bill
    2: A list of records where the lobbyist testified against a bill
    """
    error=False
    if 'name' in request.GET:
        name_query = request.GET['name']
        if not name_query:
            error=True
        elif name_query:
            witness_for_list = witness_for.objects.filter(witness_for__search=name_query)
            witness_against_list = witness_against.objects.filter(witness_against__search=name_query)
            orgs_for = witness_for.objects.filter(witness_for__search=name_query).values('witness_for_org').order_by('witness_for_org').distinct()
            orgs_against = witness_against.objects.filter(witness_against__search=name_query).values('witness_against_org').order_by('witness_against_org').distinct()
            context = {'witness_for_list': witness_for_list, 'witness_against_list': witness_against_list, 'orgs_for': orgs_for, 'name_query': name_query}
            return render(request, 'minutes_search/name.html', context)
    return render(request, 'minutes_search/name.html', {'error': error})

def search_by_org(request):
    error=False
    if 'org' in request.GET:
        org_query = request.GET['org']
        if not org_query:
            error=True
        else:
            witness_for_list = witness_for.objects.filter(witness_for_org__search=org_query).order_by('-year')
            witness_against_list = witness_against.objects.filter(witness_against_org__search=org_query).order_by('-year')
            org_for_bills_list = witness_for.objects.filter(witness_for_org__search=org_query).values('bill_no')
            org_against_bills_list = witness_against.objects.filter(witness_against_org__search=org_query).values('bill_no')
            total_bills_for = witness_for.objects.filter(witness_for_org__search=org_query).values('bill_no').distinct().count()
            total_bills_against = witness_against.objects.filter(witness_against_org__search=org_query).values('bill_no').distinct().count()
            bills_passed_for = witness_for.objects.filter(witness_for_org__search=org_query).values('bill_no').filter(law='yes').distinct().count()
            bills_passed_against = witness_against.objects.filter(witness_against_org__search=org_query).values('bill_no').filter(law='yes').distinct().count()
            context = {
                'witness_for_list': witness_for_list,
                'witness_against_list': witness_against_list,
                'org_for_bills_list': org_for_bills_list,
                'org_against_bills_list': org_against_bills_list,
                'total_bills_for': total_bills_for,
                'total_bills_against': total_bills_against,
                'bills_passed_for': bills_passed_for,
                'bills_passed_against': bills_passed_against,
                'org_query': org_query,
            }
            return render(request, 'minutes_search/org.html', context)
    return render(request, 'minutes_search/org.html', {'error': error})

def search_by_lawmaker(request):
    error=False
    if 'lawmaker' in request.GET and 'year' in request.GET:
        lawmaker_query = request.GET['lawmaker']
        year_query = request.GET['year']
        if not lawmaker_query:
            error=True
        elif lawmaker_query:
            witness_for_list = witness_for.objects.filter(bill_sponsor__search=lawmaker_query).filter(year=year_query).order_by('bill_no')
            witness_against_list = witness_against.objects.filter(bill_sponsor__search=lawmaker_query).filter(year=year_query).order_by('bill_no')
            orgs_for = witness_for.objects.filter(bill_sponsor__search=lawmaker_query).values('witness_for_org')
            orgs_against = witness_against.objects.filter(bill_sponsor__search=lawmaker_query).values('witness_against_org')
            org_for_bills_list = witness_for.objects.filter(bill_sponsor__search=lawmaker_query).values('bill_no')
            org_against_bills_list = witness_against.objects.filter(bill_sponsor__search=lawmaker_query).values('bill_no')
            total_bills = witness_for.objects.filter(bill_sponsor__search=lawmaker_query).values('bill_no').distinct().count()
            bills_passed_for = witness_for.objects.filter(bill_sponsor__search=lawmaker_query).values('bill_no').filter(law='yes').distinct().count()
            bills_passed_against = witness_against.objects.filter(bill_sponsor__search=lawmaker_query).values('bill_no').filter(law='yes').distinct().count()
            context = {
                'witness_for_list': witness_for_list,
                'witness_against_list': witness_against_list,
                'orgs_for': orgs_for,
                'orgs_against': orgs_against,
                'org_for_bills_list': org_for_bills_list,
                'org_against_bills_list': org_against_bills_list,
                'total_bills': total_bills,
                'bills_passed_for': bills_passed_for,
                'bills_passed_against': bills_passed_against,
                'lawmaker_query': lawmaker_query
            }
            return render(request, 'minutes_search/lawmaker.html', context)
    return render(request, 'minutes_search/lawmaker.html', {'error': error})
