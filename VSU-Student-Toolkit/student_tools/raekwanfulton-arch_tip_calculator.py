"""Tip Calculator tool created by raekwanfulton-arch.

Splits a restaurant bill, adds a tip, and shows each person's share.
Uses user input, calculations, a conditional, and a loop.
"""
TOOL_NAME = 'Tip Calculator'


def run():
    print('\nTip Calculator')
    try:
        bill = float(input('Bill amount: '))
        tip_rate = float(input('Tip percent (for example 18): '))
        people = int(input('How many people are splitting the bill: '))
    except ValueError:
        print('Please enter valid numbers.')
        return

    if bill < 0 or tip_rate < 0 or people < 1:
        print('Bill and tip must be zero or more, and at least one person is required.')
        return

    tip = bill * tip_rate / 100
    total = bill + tip
    share = total / people

    print(f'Tip amount: ${tip:.2f}')
    print(f'Total with tip: ${total:.2f}')
    print(f'Each person pays: ${share:.2f}')

    print('\nSuggested tip levels:')
    for rate in (15, 18, 20):
        amount = bill * rate / 100
        print(f'  {rate}% -> ${amount:.2f} tip, ${bill + amount:.2f} total')
