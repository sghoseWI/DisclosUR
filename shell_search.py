from prompt_toolkit import prompt, AbortAction
from prompt_toolkit.history import InMemoryHistory
from prompt_toolkit.contrib.completers import WordCompleter
#import open_states

def find_connections(address):
    pass

def main():
    history = InMemoryHistory()

    while True:
        try:
            address = prompt('Address > ',
                          history=history,
                          on_abort=AbortAction.RETRY)
            output = find_connections(address)

            print(messages)
        except EOFError:
            break  # Control-D pressed.

    print('Call your representative - GoodBye!')

if __name__ == '__main__':
    main()