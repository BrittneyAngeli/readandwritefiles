import csv


def main():
    
    #Open the customer file 
    customers = open('customers.csv', 'r')

    customer_file = csv.reader(customers, delimiter = ',')

    #Open the customer_country.csv file to write into 
    country_outfile = open('customer_country.csv', 'w')

    #Customer and country counter 
    customer_counter = 0

    #Write the file header and skip first line
    country_outfile.write('FirstName,LastName,Country' + '\n')
    next(customer_file)

    #Display each client and their associated country and the counter
    for record in customer_file:
        country_outfile.write(record[1] + ',' + record[2] + ',' + record[4] + '\n')
        customer_counter += 1

    print("Number of records: ", customer_counter)
    
    #Close the file 
    country_outfile.close()

main()