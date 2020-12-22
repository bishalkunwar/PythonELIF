# Program for the Inland Revenue Department (IRD) named Integrated Tax System(ITS)
# Solution:

print("\t\t\t\tDepartment of Transport Management\n\t\t\t\t\tBanseswor, Kathmandu\n\t\t\t\t Welcome to DOTM Bike Renewal System\n\t\t\t\t\tFiscal Year 2020/21")
name = input("Customer Name: ")
address = input("Customer Address: ")
bike_cc = int(input("Customer Bike in cc: "))
phone_number = input("Phone No.: ")

# Checking Condition
if bike_cc >= 125:
    tax_amount = 2800
elif 126 < bike_cc <= 160:
    tax_amount = 4500
elif 161 < bike_cc <= 250:
    tax_amount = 5500
elif 251 < bike_cc <= 400:
    tax_amount = 9000
elif 501 < bike_cc <= 650:
    tax_amount = 20000
else:
    tax_amount = 30000


# Displaying the output
print("\t\t\t\t Department of Transport Management\n\t\t\t\t\tBanseswor, Kathmandu\n\t\t\t\tWelcome to DOTM Bike Renewal System\n\t\t\t\t\tFiscal Year 2020/21")
print("Customer Name: {0}\t\t\t\t\tAddress: {1}\nCustomer Bike[cc]: {2}\t\t\t\t\tPhone No.: {3}\n{0} with {2} cc Bike has to pay Tax of [Rs.] = {4}".format(name, address, str(bike_cc), phone_number, str(tax_amount)))

'''Output sample:
				Department of Transport Management
					Banseswor, Kathmandu
				 Welcome to DOTM Bike Renewal System
					Fiscal Year 2020/21
Customer Name: bishal
Customer Address: gongabu
Customer Bike in cc: 250
Phone No.: 9818087244
				 Department of Transport Management
					Banseswor, Kathmandu
				Welcome to DOTM Bike Renewal System
					Fiscal Year 2020/21
Customer Name: bishal					Address: gongabu
Customer Bike[cc]: 250					Phone No.: 9818087244
bishal with 250 cc Bike has to pay Tax of [Rs.] = 2800

Process finished with exit code 0'''