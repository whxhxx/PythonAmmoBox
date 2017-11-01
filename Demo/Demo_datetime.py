"""
datetime Demo class
"""
import datetime


def get_next_week_day(year, month, day, format='%Y-%m-%d'):
    """
    to get the next working day(only Mon. Tues. Wed. Thur. Fri.) string
        :param year:
        :param month:
        :param day:
        :param format='%Y-%m-%d':format: default format is like 2017-11-07
    """
    m_now = datetime.datetime(year, month, day)
    next_trade_day = m_now + datetime.timedelta(days=1)
    while next_trade_day.isoweekday() > 5:
        next_trade_day += datetime.timedelta(days=1)
    return next_trade_day.strftime(format)


def get_trade_day(m_now=datetime.datetime.now()):
    """
    to get the next trade day
        :param m_now=datetime.datetime.now()
    """
    seperate_mark = '-'
    year = m_now.year
    month = m_now.month
    day = m_now.day
    hour = m_now.hour
    minute = m_now.minute
    second = m_now.minute

    m_hour_minute = hour * 100 + minute

    # if during day_market
    current_trade_day = ''
    if (m_hour_minute >= 900 and m_hour_minute <= 1130) or (m_hour_minute >= 1300 and m_hour_minute <= 1500):
        current_trade_day = datetime.datetime(year = year, month = month,)
    # if during night_market
    else:
        if (m_hour_minute >= 2100 and m_hour_minute <= 2400) or (m_hour_minute >= 0 and m_hour_minute <= 230):
            current_trade_day = get_next_week_day(
                year=year, month=month, day=day)
        else:
            print 'ERROR TRADE TIME'

    return current_trade_day


def main():
    m1 = datetime.datetime(2017, 11, 1, 11, 1, 20)
    print get_trade_day(m_now=m1)
    pass


if __name__ == '__main__':
    main()
