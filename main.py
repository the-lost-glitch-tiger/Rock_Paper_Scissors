
import random
import csv

FILE_NAME = 'rps_results.csv'

class bcolors:
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def main():
    while True:
        print("Kivi, paber, käärid")
        print('1. Mängi Kivi, paber, käärid')
        print('2. Mängud kokku')
        print('3. Statistika')
        print('0. Lahku')
        choice = input('Tee valik: ')
        if choice == '0':
            break
        elif choice == '1':
            game()
        elif choice == '2':
            print('mängud')
            #print(read_scores())
            print(f'Kokku männgiutd {read_scores()} mängu!')
        elif choice == '3':
            read_scores()


#battels = []
def game():
    battels = []
    while True:
        computerName = 'Arvuti'
        playerName = 'Mängia'
        print('- - - - - - - - - - -')
        print('')
        computerChoice = computer()
        #print(computerChoice)
        print('"Uus Mäng" et uuest alustada')
        print('"Exit" et lahkuda')
        #print(computerChoice)
        print(battels)
        if len(battels) == 5:
            print('--- --- --- --- ---')
            losts = 0
            wins = 0
            for i in battels:
                if i == 'Lost':
                    losts += 1
                elif i == 'Win':
                    wins += 1
                print(i)
            if wins >= losts:
                print('Mängia võitis! Arvuti kaoats')
            elif wins <= losts:
                print('Arvuti võitis! Mängia kaoatas')
            name = input('Sinu Nimi: ')
            save_scores(name, battels)
            print('--- --- --- --- ---')
            return

        winLost = ''
        choice = input('Vali: Kivi, Paber, Käärid: ').lower()
        if choice == computerChoice:
            #print(bcolors.BOLD+"Viik"+bcolors.ENDC)
            winLost = 'viik'
        elif choice == 'kivi':#or choice == '1':
            if computerChoice == 'paber':
                winLost = 'Lost'
                battels.append('Lost')
            else:
                winLost = 'Win'
                battels.append('Win')
        elif choice == 'paber':#or choice == '2':
            if computerChoice == 'käärid':
                winLost = 'Lost'
                battels.append('Lost')
            else:
                winLost = 'Win'
                battels.append('Win')
        elif choice == 'käärid':# or choice == '3':
            if computerChoice == 'kivi':
                winLost = 'Lost'
                battels.append('Lost')
            else:
                winLost = 'Win'
                battels.append('Win')
        elif choice == 'uus mäng':
            print('Alusta Uus Mäng')
            game()
        elif choice == 'exit':
            return
        else:
            print('Vale valik')
        #battels += 1
        print(bcolors.BOLD+'Arvuti: '+computerChoice+' / Mängia: '+choice+bcolors.ENDC)
        print(winLost)
        
    #print(computer())

def computer():
    """Saa suvaline number"""
    rand = random.randrange(1, 4)
    if rand == 1:
        return "kivi"
    elif rand == 2:
        return "paber"
    elif rand == 3:
        return "käärid"
    print(rand)

def save_scores(name, battli):
    with open(FILE_NAME, 'a', newline='') as csvfile:
        scorewriter = csv.writer(csvfile, delimiter=';')
        print(name)
        for score in battli:
            print(score)
            scorewriter.writerow([name]+[score])
        #scorewriter.writerow([name]+[battli])

def read_scores():
    num = 0
    with open(FILE_NAME, newline='') as csvfile:
        scorereader = csv.reader(csvfile, delimiter=';')
        for row in scorereader:
            num+=1
            print(', '.join(row))
        return num

if __name__ == '__main__':
    main()