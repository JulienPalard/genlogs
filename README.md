# Gen Logs

Generate random logs of user consuming objects, with objects
optionally in categories and optionaly any depth of category, and
controlling their distribution.


# Usage

Distructions can be given either as a `random` function, like
`normalvariate(7.5, 1)`, or a list of weights, like `[0.1, 0.2, 0.3, 0.4]`.


# Examples

Generate users consuming items:
```
$ genlogs --user-qty 100 --human-readable 'normalvariate(7.5, 1)'
Line(user=18, consumes=[Item(id=7)])
Line(user=41, consumes=[Item(id=8)])
Line(user=55, consumes=[Item(id=8)])
Line(user=38, consumes=[Item(id=8)])
Line(user=9, consumes=[Item(id=6)])
Line(user=76, consumes=[Item(id=9)])
Line(user=90, consumes=[Item(id=8)])
Line(user=14, consumes=[Item(id=7)])
Line(user=26, consumes=[Item(id=6)])
Line(user=26, consumes=[Item(id=6)])
```

Generate users consuming items in a category:
```
$ genlogs --user-qty 100 --human-readable 'gammavariate(7.5, 1)' 'normalvariate(7.5, 1)'
Line(user=69, consumes=[Category(id=7), Item(id=5)])
Line(user=58, consumes=[Category(id=5), Item(id=7)])
Line(user=100, consumes=[Category(id=2), Item(id=7)])
Line(user=71, consumes=[Category(id=6), Item(id=8)])
Line(user=18, consumes=[Category(id=10), Item(id=7)])
Line(user=81, consumes=[Category(id=6), Item(id=7)])
Line(user=52, consumes=[Category(id=5), Item(id=7)])
Line(user=14, consumes=[Category(id=6), Item(id=7)])
Line(user=34, consumes=[Category(id=7), Item(id=6)])
Line(user=3, consumes=[Category(id=8), Item(id=7)])
```

Generate users consuming items in a subcategory in a category:
```
$ genlogs --user-qty 100 --human-readable 'gammavariate(7.5, 1)' 'gammavariate(7.5, 1)' 'normalvariate(7.5, 1)'
Line(user=47, consumes=[Category(id=9), Category(id=6), Item(id=7)])
Line(user=25, consumes=[Category(id=6), Category(id=3), Item(id=7)])
Line(user=14, consumes=[Category(id=12), Category(id=4), Item(id=6)])
Line(user=51, consumes=[Category(id=3), Category(id=11), Item(id=6)])
Line(user=4, consumes=[Category(id=10), Category(id=8), Item(id=9)])
Line(user=84, consumes=[Category(id=8), Category(id=3), Item(id=7)])
Line(user=94, consumes=[Category(id=5), Category(id=5), Item(id=8)])
Line(user=39, consumes=[Category(id=5), Category(id=7), Item(id=8)])
Line(user=48, consumes=[Category(id=6), Category(id=4), Item(id=7)])
Line(user=1, consumes=[Category(id=5), Category(id=5), Item(id=7)])
```