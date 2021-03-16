import logging
from datetime import date
import xlsxwriter

from django.utils import timezone

from apps.core.models import Account
from event_management.celery import app

logger = logging.getLogger(__name__)


@app.task
def send_daily_horoscope_notification():
    today = date.today()
    """qs = Account.objects.filter(date_joined=date)
    workbook = xlsxwriter.Workbook('Example2.xlsx')
    worksheet = workbook.add_worksheet()
    row = 0
    column = 0
    for q in qs:
        worksheet.write(row, column, qs.email)
        row += 1
      
    workbook.close()"""
    logger.info('testing')

