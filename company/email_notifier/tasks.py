import datetime
from templated_email import send_templated_mail, get_templated_mail

from company.settings import EMAIL_HOST_USER

from sales.models import License

time_deltas = {
    '4 Months': datetime.timedelta(weeks=16),
    '1 Month': datetime.timedelta(weeks=4),
    '1 Week': datetime.timedelta(weeks=1)
}

def check_licenses(target_date):
    active_licenses = License.objects.filter(activated=True).all()
    scheduled_sellers = {}

    for active_license in active_licenses:
        remaining_active_time = active_license.expire_date - target_date
        reason = None

        if remaining_active_time == time_deltas['4 Months']:
            reason = 'Expira em 4 meses'
        if (remaining_active_time <= time_deltas['1 Month']) and (target_date.weekday() == 0):
            reason = 'É segunda feira e falta um mês ou menos expirar'
        if remaining_active_time <= time_deltas['1 Week']:
            reason = 'Expira em breve'
        
        if reason:
            try:
                scheduled_sellers[active_license.seller][active_license.client].append((active_license, reason))
            except KeyError:
                scheduled_sellers[active_license.seller] = {active_license.client:[(active_license, reason)]}
    
    return scheduled_sellers
        
def send_email(seller, client, licenses):
    message = get_templated_mail(
        template_name='notify_seller',
        from_email=EMAIL_HOST_USER,
        to=[seller.email],
        context={
            'seller':seller,
            'client': client,
            'licenses':licenses
        },)
    message.send()

def notify_sellers(target_date=datetime.date.today()):
    scheduled_sellers = check_licenses(target_date)

    for seller in scheduled_sellers.keys():
        for client, licenses in scheduled_sellers[seller].items():
            send_email(seller, client, licenses)