# Variant 3
# Task 1:
# The report stores information: company name, profit
# enterprises per month, accrual on salary Sort this report in order
# decrease in profits and display information from the three most profitable enterprises.

from collections import namedtuple
from random import randint

company_names = ('NexaCorp', 'Synthetix', 'Cybrospace', 'NeoCypher', 'OmegaTech', 'Dynamics')


def create_companies(names):
    companies = []
    Company = namedtuple('Company', ['name', 'profit', 'salary'])
    for crt_name in names:
        profit = randint(1000, 10000)
        companies.append(Company(crt_name, profit, profit // 2))
    return companies


def report(comps):
    pattern = '{}) Name: {} Profit: {} Salary: {}'

    # sorted
    for init_idx in range(len(comps) - 1):
        remem_idx = init_idx
        for res_idx in range(init_idx + 1, len(comps)):
            if comps[res_idx].profit > comps[remem_idx].profit:
                remem_idx = res_idx
        tmp = comps[init_idx]
        comps[init_idx] = comps[remem_idx]
        comps[remem_idx] = tmp

    print('List of companies under audit:')
    for idx, crt_comp in enumerate(comps):
        print(pattern.format(idx + 1, crt_comp.name, crt_comp.profit, crt_comp.salary))
    print('')
    print(f'{"!*" * 3} The most successful three companies {"!*" * 3} ')
    for idx, crt_comp in enumerate(comps[0:3]):
        print("-" * 50)
        print(pattern.format(idx + 1, crt_comp.name, crt_comp.profit, crt_comp.salary))
    print("-" * 50)


if __name__ == '__main__':
    companies_set = create_companies(company_names)
    report(companies_set)
