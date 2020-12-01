# About
This is a simple application which allows you to use the function and calculate (roughly) what you income taxes should be.
This is for other developers who want a function to quickly calculate state income tax based on their state and income.
This information should be used for FUN only, I am not an accountant :).

# How to use this?

pip install -i https://test.pypi.org/simple/ states-itax-rileycworstell==0.0.1

`
import states_income_tax as si
si.calculate_itaxes(700, 'AL')
`

If you don't care about all this other stuff you can use this by pulling down this repository and calling the calculate_itaxes(income, state) function where state is your states abbreviation such as 'KY' or 'NY'.

# How the Data was Compiled.
I got the data from this project on https://taxfoundation.org/facts-and-figures-2020/
Then I converted the exel document to a CSV file. 
Then I developed and ran the pycsv.py file included in the document and took the printed result and set that as a dictionary stored
in the tax_dict.py file.

# How this works!
This dictionary (in tax_dict.py) allows the main function in states_income_tax/__init__.py to take your income and state and give you your estimated state income tax.

# Testing
The testing is currently in tests/test_states.py. As time goes I am working on adding new tests in there.

