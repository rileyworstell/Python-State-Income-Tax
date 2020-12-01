import pandas as pd


states = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY',
          'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY',
          'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA',
          'WV', 'WI', 'WY', 'DC']

max = 90000000

# Helper Function to clean some of the data from the CSV
# To see more about this data look at https://taxfoundation.org/facts-and-figures-2020/ table 12


def clean_rate(val):
    i = val.index('%')
    return float(val[:i]) / 100


def clean_bracket(val):
    val = val.replace('$', '')
    val = val.replace(',', '')
    val = val.strip()
    return float(val)


# Prepare and Clean Data
pd.set_option('display.max_rows', None)  # Can Delete Later
df = pd.read_csv('table.csv')
df = df.drop(['Delete', 'Delete.1'], axis=1)

df['Rate'] = df['Rate'].fillna('0%')
df = df.fillna('0')

df['Rate'] = df['Rate'].map(lambda x: clean_rate(x))
df['Bracket'] = df['Bracket'].map(lambda x: clean_bracket(x))


def create_tax_dict():
    # Initialize variables
    state_index = 0
    result_dict = {}
    arr = []
    prev_bracket = 0
    current_state = states[state_index]
    result_dict[states[state_index]] = []
    # For each row in the data frame
    for i in range(len(df['State'])-1):
        # If the next one is not a new state
        if df['State'][i+1] == '0':
            result_dict[states[state_index]].append([
                round(df['Rate'][i], 4),  round((float(df['Bracket'][i+1]) - float(df['Bracket'][i])), 4)])
        # If it is a new state then do the below
        else:
            result_dict[states[state_index]].append([
                df['Rate'][i],  max])
            # Say New state index
            state_index += 1
            # Setting it originally to an empty array for the main function
            result_dict[states[state_index]] = []
    return result_dict


# This gave me the result that I then put in my states_itax.py file
print(create_tax_dict())
