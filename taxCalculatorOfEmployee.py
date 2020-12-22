# Program for the Inland Revenue Department (IRD) named Integrated Tax System(ITS)
# Solution:

print("\t\t\t\tInland Revenue Department\n\t\t\t Welcome to Integrated Tax System")
name = input("Enter your name: ")
address = input("Address: ")
married_status = input("Enter 'Y' for Married and 'N' for Unmarried: ")
pan_no = int(input("Enter your PAN No.: "))
monthly_income = int(input("Enter your monthly income: "))
annual_income = monthly_income * 12

def married(income):
    total = 450000
    tax_rate = 1
    rate = 0
    extra_income = 0
    if income <= total:
        tax_rate = 1
    elif total < income <= total + 100000:
        rate = 10
        extra_income = 100000
    elif total + 100000 < income <= total + 200000:
        rate = 20
        extra_income = 200000
    elif (total + 200000 < income <= total + 1250000) or (total + 200000 < income < total + 2000000):
        rate = 30
        extra_income = 1250000
    elif income > total + 1300000 and income >= total + 2000000:
        rate = 36
        extra_income = 2000000

    tax = ((tax_rate / 100) * income) + ((rate / 100) * extra_income)
    return [rate, tax]

def unmarried(income):
    total = 400000
    tax_rate = 0
    rate = 0
    extra_income = 0
    if income <= total:
        tax_rate = 1
    elif total < income <= total + 100000:
        rate = 10
        extra_income = 100000
    elif total + 100000 < income <= total + 200000:
        rate = 20
        extra_income = 200000
    elif (total + 200000 < income <= total + 1300000) or (total + 200000 < income < total + 2000000):
        rate = 30
        extra_income = 1300000
    elif income > total + 1300000 and income >= total + 2000000:
        rate = 36
        extra_income = 2000000

    tax = ((tax_rate / 100) * income) + ((rate / 100) * extra_income)
    return [rate, tax]


# Temporary placeholder for use during printing
temp = 0

# Condition that checks if the person is married or not
if married_status == 'Y':
    temp = married(annual_income)
else:
    temp = unmarried(annual_income)


# Displaying the output in the specified format
print("\t\t\t\tInland Revenue Department\n\t\t\t\t\tLazimpat, Kathmandu\n\t\t\t\t\t\tWelcome to \n\t\t\t\tIntegrated Tax System")
print("Tax Payee: {0} \t\t\t\t\tAddress: {1}\nPAN No: {2}\t\tFY: 2020/2021\t\tMarried Status: {3}\nTax Payee {0} with PAN {2} falls under (1 + {4})% Tax salb.\n{0} (PAN {2}) to pay tax to government is [Rs.] = {5}".format(name, address, pan_no, married_status, str(temp[0]), str(temp[1])))


'''Output sample:
Inland Revenue Department
			 Welcome to Integrated Tax System
Enter your name: bishal
Address: gongabu
Enter 'Y' for Married and 'N' for Unmarried: n
Enter your PAN No.: 1234
Enter your monthly income: 780000
				Inland Revenue Department
					Lazimpat, Kathmandu
						Welcome to 
				Integrated Tax System
Tax Payee: bishal 					Address: gongabu
PAN No: 1234		FY: 2020/2021		Married Status: n
Tax Payee bishal with PAN 1234 falls under (1 + 36)% Tax salb.
bishal (PAN 1234) to pay tax to government is [Rs.] = 720000.0

Process finished with exit code 0

'''