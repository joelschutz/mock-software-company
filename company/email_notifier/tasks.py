import datetime

from sales.models import License

time_deltas = {
    '4 Months': datetime.timedelta(weeks=16),
    '1 Month': datetime.timedelta(weeks=4),
    '1 Week': datetime.timedelta(weeks=1)
}

def check_licenses(target_date=datetime.date.today()):
    active_licenses = License.objects.filter(activated=True).all()
    scheduled_sellers = {}

    for active_license in active_licenses:
        remaining_active_time = active_license.expire_date - target_date
        reason = None

        if remaining_active_time == time_deltas['4 Months']:
            reason = 'Exactly 4 months to expire.'
        elif (remaining_active_time <= time_deltas['1 Month']) and (target_date.weekday() == 0):
            reason = 'Monday task, 1 month to expire.'
        elif remaining_active_time <= time_deltas['1 Week']:
            reason = 'Expiring soon'
        
        if reason:
            try:
                scheduled_sellers[active_license.seller][active_license.client].append((active_license, reason))
            except KeyError:
                scheduled_sellers[active_license.seller] = {active_license.client:[(active_license, reason)]}
    
    return scheduled_sellers
        
