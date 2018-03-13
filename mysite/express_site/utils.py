import datetime


def get_date_range(date01, date02):
    # date01 = request.GET.get('starttime', False)
    # date02 = request.GET.get('endtime', False)
    if date01:
        starttime = datetime.datetime.strptime(date01, '%Y-%m-%d %H:%M:%S')
    else:
        starttime = datetime.datetime.now()
        starttime = starttime - datetime.timedelta(days=days)
        starttime = starttime.replace(hour=0, minute=0, second=0, microsecond=0)

    if date02:
        endtime = datetime.datetime.strptime(date02, '%Y-%m-%d %H:%M:%S')
    else:
        endtime = datetime.datetime.today()
        endtime = endtime.replace(hour=0, minute=0, second=0, microsecond=0)

    return starttime, endtime