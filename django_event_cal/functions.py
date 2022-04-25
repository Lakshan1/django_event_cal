import calendar
from calendar import HTMLCalendar
from datetime import datetime

from .models import Events


now = datetime.now()
#Get current year
current_year = now.year

#get current month
current_month = now.date().strftime("%B")

#get current date
current_date = now.date().strftime("%d")

current_month_year = str(f"{now.date().strftime('%B')} {now.year}")

def cal_context(context,year=None,month=None,navigation=False):

    cal_context = {
        'current_date':current_date,
        'current_month_year':current_month_year,
        'navigation':navigation,
    }

    if navigation:
        cal_context['year'] = year
        month = month.capitalize()
        month_number = list(calendar.month_name).index(month)
        month_number = int(month_number)
        if month_number == 1:
            previous_month = "december"
            cal_context['previous_month'] = previous_month
        else:
            previous_month = calendar.month_name[month_number-1]
            cal_context['previous_month'] = previous_month

        if month_number == 12:
            next_month = "january"
            cal_context['next_month'] = next_month
        else:
            next_month = calendar.month_name[month_number+1]
            cal_context['next_month'] = next_month
    else:
        year = current_year
        cal_context['year'] = year
        month = current_month.capitalize()
        month_number = list(calendar.month_name).index(month)
        month_number = int(month_number)


    cal = HTMLCalendar().formatmonth(current_year,month_number)
    cal_context['cal'] = cal

    if Events.objects.all().filter(date=current_date,month__icontains=month,year=year).exists():
        objs = Events.objects.all().filter(date=current_date,month=month,year=year)
        data = objs
        cal_context['data'] = data
    else:
        res = 'No Events found...'
        data = res
        cal_context['data'] = data

    for i in context.keys():
        cal_context[i] = context[i]

    return cal_context
