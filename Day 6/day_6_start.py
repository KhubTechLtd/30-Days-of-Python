names = ["Justin", "john", "Emilee", "Jim", "Ron", "Sandra", "veronica", "Whitney"]
amounts = [123.32, 94.23, 124.32, 323.4, 23, 322.122323, 32.4, 99.99]

unf_message = """Hi {name} !

Thank you for the purchase on {date}. 
We hope you are exicted about using it. Just as a
reminder the purcase total was ${total}.
Have a great one!

Team CFE
"""

def make_messages{names, amounts}:
    messages = []
    if len(names) == len(amounts):
        i = 0
        for name in names:
            new_msg = unf_message.format(
                name=name,
                date='some date',
                total=129.99
            )
            print(new_msg)

make_messages(default_names,default_amounts)