# Code contains four problems.
STATE_TAX_RATE = .051
COUNTY_TAX_RATE = .024
#Tax rate was wrong

def main():
    print('This program will calculate your taxes!\n')

    sale = float(input('How much is the cost of your purchase? '))
    state_tax = calculate_state_tax = (sale * STATE_TAX_RATE)
    # Varaible was missing the "=" and was missing variable, missing *
    county_tax = calculate_county_tax = (COUNTY_TAX_RATE * sale)
    #Missing "=", missing *
    total_cost = sale + state_tax + county_tax

    print('\nSale amount: $', format(sale, '.2f'), sep = '')
    print('State tax  : $', format(state_tax, '.2f'), sep = '')
    print('County tax : $', format(county_tax, '.2f'), sep = '')
    print('Total cost : $', format(total_cost, '.2f'), sep = '')

def calculate_state_tax(sales_amount, tax_rate):
	return(sales_amount * tax_rate)
	
def calculate_county_tax(amount, rate):
	taxes = amount * rate

main()

#Jeremy Durdel
#Chapter 5 Lab 1
#06/23/2025
