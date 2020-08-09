from os import system, name

def render_sites_list(sites):
    output = []
    counter = 0
    for item in sites:
        output.append('[' + str(counter) + '] ' + str(item['title']))
        counter += 1
    return output

def clear_screen(): 
    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear') 