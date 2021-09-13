from django.shortcuts import render
import datetime
# month  = {"January":1,"February":2, "March":3, "April":4, "May":5, "June":6, "July": 7, "Augest": 8, "September": 9, "Outober": 10, "November": 11, "December": 12 }
month = range(12)
# Create your views here.
def index(request):
    now= datetime.datetime.now()
    context = {"newmonth": now.month in month and now.day == 1}
    return render(request, "newmonth/index.html", context)