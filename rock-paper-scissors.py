import random
gamenum = player = pc = 0
options = ['πέτρα', 'χαρτί', 'ψαλίδι']
while True:

    gamenum += 1
    points = f'Εσύ: {player} πόντους - Computer: {pc} πόντους'
    print(points)
    pcchoice = options[random.randrange(0, 3)]
    command = 'π[έτρα], ψ[αλίδι], χ[ααααααααααρτί]! - [\q για να βγεις]'
    #print(pcchoice)
    
    choice = print(f'Παιχνίδι:{gamenum} - {command}')
    userchoice = input(command)

    if (userchoice == '\q' or userchoice == '\;'):
        print('\nΓειααααα σου ρε φίλε!')
        break
    
    elif userchoice in ['p', 'petra', 'rock', 'π', 'πέτρα', 'πετρα']:
        if pcchoice == options[0]:
            print(f'Διάλεξες πέτρα - Διάλεξα {pcchoice}. Ισοπαλία.' + points)
        elif pcchoice == options[1]:
            print(f'Διάλεξες πέτρα - Διάλεξα {pcchoice}. Σε κέρδισα.')
            pc += 1
        else:
            print(f'Διάλεξες πέτρα - Διάλεξα {pcchoice}.  Έχασα.')
            player += 1
        print('\n')
        
    elif userchoice in ['ps', 'psalidi', 'scissors', 'ψ', 'ψαλίδι', 'ψαλιδι', 'c']:
        if pcchoice == options[2]:
            print(f'Διάλεξες ψαλίδι - Διάλεξα {pcchoice}. Ισοπαλία.')
        elif pcchoice == options[0]:
            print(f'Διάλεξες ψαλίδι - Διάλεξα {pcchoice}. Σε κέρδισα.')
            pc += 1
        else:
            print(f'Διάλεξες ψαλίδι - Διάλεξα {pcchoice}. Έχασα.')
            player += 1
        print('\n')
        
    elif userchoice in ['x', 'xarti', 'paper', 'χ', 'χαρτί', 'χαρτι']:
        if pcchoice == options[1]:
            print(f'Διάλεξες χαρτί - Διάλεξα {pcchoice}. Ισοπαλία.')
        elif pcchoice == options[0]:
            print(f'Διάλεξες χαρτί - Διάλεξα {pcchoice}. Έχασα.')
            player += 1
        else:
            print(f'Διάλεξες χαρτί - Διάλεξα {pcchoice}.  Σε κέρδισα.')
            pc += 1
        print('\n')
        
    else:
        print('Δεν κατάλαβα τι έγραψες.\n')
        continue
  
