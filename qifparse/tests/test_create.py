# -*- coding: utf-8 -*-
import unittest
from qifparse import qif


class TestCreateQIF(unittest.TestCase):

    def testCreateSplit(self):
        expected='''!Account
NAssets:Checking Accounts:Checking
TBank
^
!Type:Bank
D12/11/2017
T-100
S[Expenses:Groceries]
$-40
S[Expenses:Clothing]
$-60
^
'''

        qif_obj = qif.Qif()
        chk_acc = qif.Account(name='Assets:Checking Accounts:Checking', account_type='Bank')
        qif_obj.add_account(chk_acc)

        expense = qif.Transaction()
        expense.amount = -100

        splitA = qif.AmountSplit()
        splitA.to_account = 'Expenses:Groceries'
        splitA.amount = -40
        expense.splits.append(splitA)

        splitB = qif.AmountSplit()
        splitB.to_account = 'Expenses:Clothing'
        splitB.amount = -60
        expense.splits.append(splitB)

        chk_acc.add_transaction(expense, header='!Type:Bank')
#        print(str(qif_obj))
        self.assertEqual(expected, str(qif_obj))

    def testcreateQifFile(self):
        qif_obj = qif.Qif()
        acc = qif.Account(name='My Cc', account_type='Bank')
        qif_obj.add_account(acc)
        cat = qif.Category(name='food')
        qif_obj.add_category(cat)
        tr1 = qif.Transaction(amount=0.55)
        acc.add_transaction(tr1, header='!Type:Bank')

        tr2 = qif.Transaction()
        tr2.amount = -6.55
        tr2.to_account = 'Cash'
        acc.add_transaction(tr2)
        self.assertTrue(str(qif_obj))

    def testAddandGetAccounts(self):
        qif_obj = qif.Qif()
        acc = qif.Account(name='My Cc')
        qif_obj.add_account(acc)
        res = qif_obj.get_accounts(name='My Cc')
        self.assertTrue(len(res))

    def testAddandGetCategories(self):
        qif_obj = qif.Qif()
        cat = qif.Category(name='my cat')
        qif_obj.add_category(cat)
        res = qif_obj.get_categories(name='my cat')
        self.assertTrue(len(res))


if __name__ == "__main__":
    import unittest
    unittest.main()
