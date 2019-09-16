import gnucashxml


#filepath = '/home/rafa/Documents/6.financial/1.expense.tracking/gnucash/Data/'
filepath = '/home/rafa/Documents/6.financial/1.expense.tracking/gnucash.old.for.test/Data/rp.se54.v1/'
gnucashfile = 'test.rp.data.gnucash'


book = gnucashxml.from_filename(filepath+gnucashfile)
print(book.__repr__)

income_total = 0
expense_total = 0
for account, subaccounts, splits in book.walk():
    print(account.fullname())
    if account.actype == 'INCOME':
        income_total += sum(split.value for split in account.splits)
    elif account.actype == 'EXPENSE':
        expense_total += sum(split.value for split in account.splits)

print ("Total income : {:9.2f}".format(income_total * -1))
print ("Total expense: {:9.2f}".format(expense_total))