# About
This is a simple application which allows you to use the function and calculate (roughly) what you income taxes should be.
This is for other developers who want a function to quickly calculate state income tax based on their state and income.
This information should be used for FUN only, I am not an accountant :).

# How to use this?
To Download this package use:
`pip install sit-calc-rileycworstell==0.0.1`
To import and run a simple example:
`import sit_calc as si`
`si.calculate_itaxes(70000, 'AL')`

This example will tell you your state income taxes if you live in Alabama. 
For this to work you need to put the state as the 2 letter abbreviation.

Note: The 'sit' stands for state income tax


# How the Data was Compiled.
I got the data from this project on https://taxfoundation.org/facts-and-figures-2020/
Then I converted the exel document to a CSV file. 
Then I developed and ran the pycsv.py file included in the document and took the printed result and set that as a dictionary stored
in the tax_dict.py file.

# How this works!
This dictionary (in tax_dict.py) allows the main function in states_income_tax/__init__.py to take your income and state and give you your estimated state income tax.

# Testing
The testing is currently in tests/test_states.py. As time goes I am working on adding new tests in there.

