"""Generate random logs of user consuming objects, with objects
optionally in categories and optionaly any depth of category, and
controlling their distribution.
"""

import re
import random
from collections import namedtuple
from functools import partial

Line = namedtuple('Line', 'user, consumes')
Category = namedtuple('Category', 'id')
Item = namedtuple('Item', 'id')


def gen_line(user_qty, items_shapes):
    user = random.randint(1, user_qty)
    consumed = []
    for cat_distrib in items_shapes[:-1]:
        consumed.append(Category(int(cat_distrib())))
    consumed.append(Item(int(items_shapes[-1]())))
    return Line(user, consumed)


def gen_logs(line_qty, user_qty, items_shapes):
    """Generate some not-such-random logs.

    line_qty: Qty of lines to generate.
    user_qty: Qty of "user" consuming the items.
    items_shapes: Shape of the comsumed object, as a tuple of dimentions:
      - ((gamma(alpha, beta)), ) means User consuming items using a gama distribution
      - ((gamma(alpha, beta)), (normal(mu, sigma))) means users consuming categories with a gamma distribution, in which they consume items in a normal distribution
    """
    return [gen_line(user_qty, items_shapes) for _ in range(line_qty)]



def parse_args():
    import argparse
    parser = argparse.ArgumentParser(
        description='Generate some logs.'
        'shape take the form of: gammavariate(7.5, 1) '
        'using any function from the random module. '
        'Multiple distructions can be given to imbricate categories '
        'and subcategories.')
    parser.add_argument('--line-qty', type=int, default=10)
    parser.add_argument('--user-qty', type=int, default=9)
    parser.add_argument('--human-readable', action='store_true')
    parser.add_argument('shape', help='Distrubiton of a category or item.',
                        nargs='+')
    return parser.parse_args()


def main():
    args = parse_args()
    items_shapes = []
    for shape in args.shape:
        parsed = re.match(r'(?P<function>[^\(]*)\((?P<params>[0-9., ]+)\)', shape)
        if parsed:
            function = parsed.group('function')
            params = [float(x) for x in parsed.group('params').split(',')]
            items_shapes.append(partial(getattr(random, function), *params))
        parsed = re.match(r'\[(?P<weights>[0-9., ]+)\]', shape)
        if parsed:
            weights = [float(x) for x in parsed.group('weights').split(',')]
            items_shapes.append(lambda: random.choices(list(range(len(weights))), weights)[0])
    for line in gen_logs(args.line_qty, args.user_qty, items_shapes):
        if args.human_readable:
            print(line)
        else:
            print(line.user, ' '.join(str(consumed.id) for consumed in line.consumes))


if __name__ == '__main__':
    main()
