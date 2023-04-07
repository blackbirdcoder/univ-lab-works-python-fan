# Variant 3
# Task 2:
# Taking into account information about things seized at customs for the reporting period: date of extraction,
# item code, number of units, determine the group of items for which the most common was withdrawal.

from collections import namedtuple
from random import randint


def generate_reports():
    reports = []
    code = [111, 222, 333, 444, 555]
    Rept = namedtuple('Rept', ['date', 'items'])
    for crt_num in range(len(code)):
        rept = Rept(f'1{crt_num}.11.2012', [])
        for crt_code in code:
            rept.items.append({crt_code: randint(0, 50)})
        reports.append(rept)
    return reports


def report_analysis(repts):
    code = []
    res = {
        'code': None,
        'amt': 0,
        'same': []
    }

    for rept in repts:
        code = [list(item.keys())[0] for item in rept.items]
        break

    count = {key: 0 for key in code}

    for crt_code in code:
        for rept in repts:
            for item in rept.items:
                if crt_code == list(item.keys())[0]:
                    count[crt_code] += list(item.values())[0]

    for items in count.items():
        crt_key, crt_value = items
        if res['code'] is None:
            res['code'] = crt_key
            res['amt'] = crt_value
        else:
            if res['amt'] < crt_value:
                res['code'] = crt_key
                res['amt'] = crt_value
                res['same'] = []
            elif res['amt'] == crt_value:
                res['same'].append(crt_key)
    return res


def out_report(repo, result):
    date = []
    print(f'{"=" * 3} List of goods and their quantity {"=" * 3}')
    for crt_repo in repo:
        date.append(crt_repo.date)
        print(f'Date: {crt_repo.date}')
        for items in crt_repo.items:
            print(f'Item: {list(*items.items())[0]} Quantity: {list(*items.items())[1]}')
        print('-' * 30)

    print(f'For the period from {date[0]} to {date[-1]}')
    print('The most common prohibited items:')
    print(f'Item: {result["code"]} Quantity: {result["amt"]}')
    if result['same']:
        print('There were also items:')
        for code in result['same']:
            print(f'Item: {code} Quantity: {result["amt"]}')


if __name__ == '__main__':
    reports = generate_reports()
    freq = report_analysis(reports)
    out_report(reports, freq)
