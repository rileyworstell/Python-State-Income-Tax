states = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY',
          'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY',
          'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA',
          'WV', 'WI', 'WY', 'DC']

max = 900000000
state_taxes = {'AL': [[0.02, 500], [0.04, 2500], [0.05, max]],
               'AK': [[0, 0]],
               'AZ': [[0.0259,   26500], [0.0334, 26500], [0.0417, 106000], [0.045, max]],
               'AR': [[0.02, 4000], [0.04, 4000], [0.059, 71300], [0.066, max]]}


def is_not_valid(income):
    if (income <= 0) or (income >= max):
        return True


def calculate_itaxes(income, state):
    if is_not_valid(income):
        return 0
    left_to_tax = income
    amount_to_pay = 0
    tax_range = state_taxes[state]
    if tax_range == [[0, 0]]:
        return 0
    for i in tax_range:
        if i[1] > left_to_tax:
            return amount_to_pay + (i[0] * left_to_tax)
        else:
            amount_to_pay += (i[0] * i[1])
            left_to_tax -= i[1]


print(calculate_itaxes(10000, 'AK'))
