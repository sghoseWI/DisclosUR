from prompt_toolkit import prompt, AbortAction
from prompt_toolkit.history import InMemoryHistory
from prompt_toolkit.contrib.completers import WordCompleter
import open_states
import center_for_public_integrity.query_cpi as qc

def find_connections(address):
    legislators = open_states.get_legislator_names(address)
    leg_corp_dict = qc.legislator_to_corps(legislators)
    return leg_corp_dict

def main():
    history = InMemoryHistory()

    while True:
        try:
            address = prompt('Address > ',
                          history=history,
                          on_abort=AbortAction.RETRY)
            output = find_connections(address)

            print(output)
        except EOFError:
            break  # Control-D pressed.

    print('Call your representative - GoodBye!')

if __name__ == '__main__':
    main()