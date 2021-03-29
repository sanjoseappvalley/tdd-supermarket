# tdd-supermarket

solving a supermarket problem with tdd approach, writing tests first.


Supermarket problem
Some company decided to create a supermarket that sell only three products:

Name         Price

Wine         $ 500
BBQ Grill    $ 100
Beer         $  25

CEO of this company is a big fan of buy-one-get-one-free offers of beer. He wants us to add a rule to do this.

The COO, though, likes low prices and wants people buying wine to get a price discount for bulk purchases.

If you buy 3 or more wine, the price should drop to $450.

The check-out can scan items in any order, and because the CEO and COO change their minds often, it needs to be flexible regarding our pricing rules.

The interface to that checkout looks like this:

co = Checkout.new(pricing_rules)
co.scan(item)
co.scan(item)

price = co.total
Implement a checkout system that fulfills these requirements.
