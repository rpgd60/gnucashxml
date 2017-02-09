"""
report.py
Generate a multicolumn report for an account
"""

import sys
import datetime

from gnucashxml import from_filename

def multisplit(book, account, date1, date2):
    mybook = from_filename(book)
    account = mybook.find_account(account)
    
    if account is None:
        raise "Cannot find account "+account
        
    splits = [j for j in account.splits if date1 <= j.transaction.date.date() <= date2]
    
    otheraccountlist = []
    for split in splits:                                     # For every transaction in this account
        for multisplits in split.transaction.splits:         # Round up its list of accounts
            if multisplits.account not in otheraccountlist:  # Compare with list of known accounts
                otheraccountlist.append(multisplits.account) # Add it to list if not known
        
    print("Date",end=",")
    for i in otheraccountlist:
        print(i.fullname(), end=",")
    print('Description')
    
    totals = {}
    for split in sorted(splits):
        print(split.transaction.date.date(),end=",")
        for j in otheraccountlist:
            value = 0
            value = sum([i.value for i in split.transaction.splits if j==i.account])
            totals[j] = totals.setdefault(j, 0) + value
            print(value,end=",")
            
        print(split.transaction.description) 

    print("",end=",")
    for i in otheraccountlist:
        print(totals[i], end=",")
    print("Total")
    
if __name__ == "__main__":
    date1=datetime.date(2000,1,1)
    date2=datetime.date(2017,1,1))
    
    multisplit("test.gnucash", "Salary", date1, date2)
