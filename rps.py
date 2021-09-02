import random
gamenum = 0
options = ['πέτρα', 'χαρτί', 'ψαλίδι']
while True:

    global options
    global games
    gamenum += 1
    pcchoice = options[random.randrange(0, 3)]
    command = 'π[έτρα], ψ[αλίδι], χ[ααααααααααρτί]! - [\q για να βγεις]'
    #print(pcchoice)
    
    choice = print(f'Παιχνίδι:{gamenum} - {command}')
    userchoice = input(command)

    if (userchoice == '\q' or userchoice == '\;'):
        print('\nΓεια σου ρε φίλε!')
        break
    
    elif userchoice in ['p', 'petra', 'rock', 'π', 'πέτρα', 'πετρα']:
        if pcchoice == options[0]:
            print(f'Διάλεξες πέτρα - Διάλεξα {pcchoice}. Ισοπαλία.')
        elif pcchoice == options[1]:
            print(f'Διάλεξες πέτρα - Διάλεξα {pcchoice}. Σε κέρδισα.')
        else:
            print(f'Διάλεξες πέτρα - Διάλεξα {pcchoice}.  Έχασα.')
        print('\n')
        
    elif userchoice in ['ps', 'psalidi', 'scissors', 'ψ', 'ψαλίδι', 'ψαλιδι', 'c']:
        if pcchoice == options[2]:
            print(f'Διάλεξες ψαλίδι - Διάλεξα {pcchoice}. Ισοπαλία.')
        elif pcchoice == options[0]:
            print(f'Διάλεξες ψαλίδι - Διάλεξα {pcchoice}. Σε κέρδισα.')
        else:
            print(f'Διάλεξες ψαλίδι - Διάλεξα {pcchoice}. Έχασα.')
        print('\n')
        
    elif userchoice in ['x', 'xarti', 'paper', 'χ', 'χαρτί', 'χαρτι']:
        if pcchoice == options[1]:
            print(f'Διάλεξες χαρτί - Διάλεξα {pcchoice}. Ισοπαλία.')
        elif pcchoice == options[0]:
            print(f'Διάλεξες χαρτί - Διάλεξα {pcchoice}. Έχασα.')
        else:
            print(f'Διάλεξες χαρτί - Διάλεξα {pcchoice}.  Σε κέρδισα.')
        print('\n')
        
    else:
        print('Δεν κατάλαβα τι έγραψες.\n')
        continue
  
