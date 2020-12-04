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
If you are confused what tax_dict is:
tax_dict is a dictionary for each state that the value for each key is an array of arrays containing 2 values. 
The first value is the percentage tax rate for that income bracket in decimal form and the second value is the ammount of money that it will be taxed at. 
For example tax_dict['AL'] contains [[0.02, 500.0], [0.04, 2500.0], [0.05, 90000000]]. The 0.02 is for 2 percent and the 500 means that the first $500 you make that year will be taxed at 2 percent. Then the next is 4 percent for the next $2500 and the last part is 5 percent for up to the large number ( I chose a large number at random because noone using this will likely make more than that ^_^ )

# Testing
The testing is currently in tests/test_states.py. As time goes I am working on adding new tests in there.

