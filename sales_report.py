"""Generate sales report showing total melons each salesperson sold."""
# improvements:
# make this script a function to be called.
# include the sales totals for each salesperson (another function)
# close the resource at the end of the function

# salepeople and melons_sold arrays are created and are empty to eventually append sum totals of each to.
salespeople = []
melons_sold = []


def melons_sold_by_salesperson():
    f = open('sales-report.txt')
# the txt file is open to be read
    for line in f:
        line = line.rstrip()
        entries = line.split('|')
    # this loop iterates over the txt file and prints each line separating the lines into three elements where they are separated (by the '|'). each element is renamed to 'entries'.

    salesperson = entries[0]
    melons = int(entries[2])
    # these lines name the entries. the first entry (index=0) is the salesperson and the 3rd entry (index =2) is the melon count from the sale. the 'int' returns the datatype as an integer.

    if salesperson in salespeople:
        position = salespeople.index(salesperson)
        melons_sold[position] += melons
        # this iterates over the salespeople in the txt file and adds to the melon count if the salesperson name matches.
    else:
        salespeople.append(salesperson)
        melons_sold.append(melons)
        # these lines append the salespeople and melons to the salespeople and melons_sold arrays.

    for i in range(len(salespeople)):
        print(f'{salespeople[i]} sold {melons_sold[i]} melons')
    f.close()
# this for loop runs through the salespeople array and prints the print statement for each iteration (i.e. for each salesperson that is in the salespeople array)
