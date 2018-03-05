from prompt_toolkit import prompt, AbortAction
from prompt_toolkit.history import InMemoryHistory
from prompt_toolkit.contrib.completers import WordCompleter
import open_states
import query_cpi as qc

def find_connections(address):
    legislators = open_states.get_legislator_names(address)
    leg_corp_dict = qc.legislator_to_corps(legislators)
    return leg_corp_dict

def get_output(address):
    leg_corp_dict = find_connections(address)
    for leg in leg_corp_dict:
        name = clean_name(leg)
        print('Your representative, {} is connected to:'.format(name))
        for corp in leg_corp_dict[leg]:
            if corp != None or corp != 'N/A':
                print(corp)
            else:
                print('nothing.... fix this bug')

def clean_name(leg):
    l = leg.title().split()
    l.reverse()
    return " ".join(l)

def main():
    history = InMemoryHistory()

    while True:
        try:
            address = prompt('Address > ',
                          history=history,
                          on_abort=AbortAction.RETRY)
            get_output(address)
            #output = find_connections(address)
            #print(output)

        except EOFError:
            break  # Control-D pressed.

    print('Call your representative - GoodBye!')

if __name__ == '__main__':
    main()