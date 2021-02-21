#!/usr/bin/env python
import click

@click.command()
@click.option("--sum")

def arith(sum):
    h = int(sum)
    total = 0
    for i in range(h):
        total += i
    print('The sum is: {}'.format(total))
    print("\r")

if __name__ == '__main__':
    #pylint: disable=no-value-for-parameter
    arith()