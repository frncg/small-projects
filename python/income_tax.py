# tax bracket calculator by frncg
import json

# read file and declare income variable
f = open("brackets.json").read()
brackets = json.loads(f)
income = 0

# get valid input from user
while True:
  try:
    income = int(input("Enter income: "))
    if income > 0:
      break
    else:
      print("Number must be greater than 0")
  except ValueError:
    print("Value must be numbers without commas only")
    continue

# enter .json arrays
tax_rates = brackets["federal"]["tax_rates"]
lower_bracket = brackets["federal"]["single_filers"]["lower_bracket"]
# declare variables for the loop
leftover, tax_paid, upper_bracket, effective_tax = income, 0, 0, 0

for i in range(0, len(tax_rates)):
  tax_dec = tax_rates[i] / 100.0

  # check if loop is not at last element yet
  if i < len(tax_rates) - 1:
    upper_bracket = lower_bracket[i + 1] - 1

    # check if over current bracket
    if income > upper_bracket:
      tax_paid += round((upper_bracket - lower_bracket[i]) * tax_dec)
    else:
      leftover -= lower_bracket[i]
      tax_paid += round(leftover * tax_dec)
      break
  else:
    leftover -= lower_bracket[i]
    tax_paid += round(leftover * tax_dec)
    break

# get effective tax
effective_tax = round(100 * tax_paid / income, 2)

# print results
print("Tax paid: ${:,}".format(tax_paid))
print("Effective tax: " + str(effective_tax) + "%")
print("Take-home pay: ${:,}".format(income-tax_paid))