import tax_dict as tax


state_taxes = tax.tax_dict

max = 90000000


def is_not_valid(income):
    if (income <= 0) or (income >= max):
        return True


# Calculating State Income taxes for single filers
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


# Calculate Federal Income taxes for single filers
def calculate_ftaxes(income):
    left_to_tax = income
    fed_taxes = tax.fed_tax_dict['Single']
    if is_not_valid(income):
        return 0
    left_to_tax = income
    amount_to_pay = 0
    for i in fed_taxes:
        if i[1] > left_to_tax:
            return amount_to_pay + (i[0] * left_to_tax)
        else:
            amount_to_pay += (i[0] * i[1])
            left_to_tax -= i[1]


# print(calculate_itaxes(700, 'AL'))
