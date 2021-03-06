QIF Parser
============

[![Travis CI Status](https://travis-ci.org/ebridges/qifparse.png?branch=master)](https://travis-ci.org/ebridges/qifparse)

qifparse is a parser for Quicken interchange format files (.qif).

Even if the qif format is:

* quite old now
* not supported for import by Quicken any more,
* ambiguous in some data management (notably on dates)

it's still quite commonly used by many personal finance managers.


Usage
======

Here's a sample parsing:

```
   >>> from qifparse.parser import QifParser
   >>> qif = QifParser.parse(file('file.qif'))
   >>> qif.get_accounts()
   (<qifparse.qif.Account object at 0x16148d0>, <qifparse.qif.Account object at 0x1614850>)
   >>> qif.accounts[0].name
   'My Cash'
   >>> qif.get_categories()
   (<qifparse.qif.Category object at 0x15b3d10>, <qifparse.qif.Category object at 0x15b3450>)
   >>> qif.accounts[0].get_transactions()
   (<Transaction units=-6.5>, <Transaction units=-6.0>)
   >>> str(qif)
   '!Type:Cat\nNfood\nE\n^\nNfood:lunch\nE\n^\n!Account\nNMy Cash\nTCash\n^\n!Type:Cash...
   ...
```

Here's a sample of a structure creation::

```
   >>> qif_obj = qif.Qif()
   >>> acc = qif.Account(name='My Cc', account_type='Bank')
   >>> qif_obj.add_account(acc)
   >>> cat = qif.Category(name='food')
   >>> qif_obj.add_category(cat)
   >>> tr1 = qif.Transaction(amount=0.55)
   >>> acc.add_transaction(tr1, header='!Type:Bank')

   >>> tr2 = qif.Transaction()
   >>> tr2.amount = -6.55
   >>> tr2.to_account = 'Cash'
   >>> acc.add_transaction(tr2)
   >>> acc.add(tr2)
   >>> str(qif_obj)
   '!Type:Cat\nNfood\nE\n^\n!Account\nNMy Cc\nTBank\n^\n!Type:Bank\nD02/11/2013\nT...
   ...
```

Object Definitions
============

### Class `QifParser`

*Methods*

Main entry point of the application:

* `parse(file_handle, date_format=None)`

Several internal class methods for parsing sub-components of the QIF file.  The file is split on the `^` character into a list of `chunk`s and fed to one or more of the below methods:

* `parseClass(chunk)`
* `parseCategory(chunk)`
* `parseAccount(chunk)`
* `parseMemorizedTransaction(chunk, date_format=None)`
* `parseTransaction(chunk, date_format=None)`
* `parseInvestment(chunk, date_format=None)`

Class method for handling the various different date formats that may appear in the `D` field (for `Transaction` and `Investment` fields.):

* `parseQifDateTime(qdate)`


### Class `Qif`

*Methods*

* `add_account()`
* `add_category()`
* `add_class()`
* `add_transaction()`
* `get_accounts()`: returns a list of `Account` objects.
* `get_categories()`
* `get_classes()`
* `get_transactions()`

### Class `Account`

*Methods*

* `account_type()`
* `add_transaction()`
* `balance_amount()`
* `balance_date()`
* `credit_limit()`
* `date_format()`
* `description()`
* `get_transactions()`: returns a `tuple` of lists of `Transaction` objects.
* `get_type()`
* `name()`
* `set_type()`

### Class `Transaction`

*Fields*

* `address`
* `amount`
* `category`
* `cleared`
* `date`
* `date_format`
* `memo`
* `num`
* `payee`
* `reimbursable_expense`
* `small_business_expense`
* `splits`
* `to_account`

### Class `AmountSplit`

*Fields*

* `category`
* `to_account`
* `amount`
* `percent`
* `address`
* `memo`

More infos
============
For more informations about qif format:

* http://en.wikipedia.org/wiki/Quicken_Interchange_Format
* http://svn.gnucash.org/trac/browser/gnucash/trunk/src/import-export/qif-import/file-format.txt
