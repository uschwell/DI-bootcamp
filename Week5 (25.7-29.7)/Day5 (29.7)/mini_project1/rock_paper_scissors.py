from game import play
from game import Game
def get_user_menu_choice():
    print("-----Main Menu-----")
    print('Welcome to our "Rock-Paper-Scissors" Game')
    print("New Game-(n)")
    print("Scores-(s)")
    print("Quit-(q)")
    print("-------------------")
    menu_input=input()
    if(menu_input.lower()=='n'):
        return 'New Game'
    elif(menu_input.lower()=='s'):
        return 'Scores'
    elif(menu_input.lower()=='q'):
        return 'quit'


def print_results(results):
    print("-----Scores-----")
    print('You have won ' +str(results['win'])+' games')
    print('You have lost ' +str(results['loss'])+' games')
    print('You have drawn '+str(results['draw'])+' games')
    print("----------------")

def main():
    game_results={'win': 0,'loss': 0,'draw': 0}
    menu='start'
    while(True):
        menu=get_user_menu_choice()
        if(menu=='quit'):
            print("Your Final Results")
            print_results(game_results)
            print("Have A Nice Day!")
            break
        if(menu=='Scores'):
            print_results(game_results)
        if(menu=='New Game'):
            newGame=play()
            #we save our results
            value=game_results[newGame]
            value+=1
            game_results[newGame]=value



# get_user_menu_choice()
# print_results()
main()