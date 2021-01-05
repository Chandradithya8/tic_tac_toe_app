board = {
    'a':'','b':'','c':'',
    'd':'','e':'','f':'',
    'g':'','h':'','i':''
}

player = 1
total_moves = 0
end_check=0

print('a|b|c')
print('_+ +_')
print('d|e|f')
print('_+_+_')
print('g|h|i')
print('----------------------------------------------------------------')

def check():
    # horizontal check for player1

    if board['a'] == 'X' and board['b'] == 'X' and board['c'] == 'X':
        print('Player one won !')
        return 1
    if board['d'] == 'X' and board['e'] == 'X' and board['f'] == 'X':
        print('Player One Won!!')
        return 1
    if board['g'] == 'X' and board['h'] == 'X' and board['i'] == 'X':
        print('Player One Won!!')
        return 1

    # diagonal check for player1

    if board['a'] == 'X' and board['e'] == 'X' and board['i'] == 'X':
        print('Player One Won!!')
        return 1
    if board['g'] == 'X' and board['e'] == 'X' and board['c'] == 'X':
        print('Player One Won!!')
        return 1    

    # vertical check for player1

    if board['a'] == 'X' and board['d'] == 'X' and board['g'] == 'X':
        print('Player One Won!!')
        return 1
    if board['b'] == 'X' and board['e'] == 'X' and board['h'] == 'X':
        print('Player One Won!!')
        return 1
    if board['c'] == 'X' and board['f'] == 'X' and board['i'] == 'X':
        print('Player One Won!!')
        return 1
    
    # horizontal check for player2

    if board['a'] == 'O' and board['b'] == 'O' and board['c'] == 'O':
        print('Player Two Won!!')
        return 1  # used to end the game
    if board['d'] == 'O' and board['e'] == 'O' and board['f'] == 'O':
        print('Player Two Won!!')
        return 1
    if board['g'] == 'O' and board['h'] == 'O' and board['i'] == 'O':
        print('Player Two Won!!')
        return 1

    # diagonal check for player2    

    if board['a'] == 'O' and board['e'] == 'O' and board['i'] == 'O':
        print('Player Two Won!!')
        return 1
    if board['g'] == 'O' and board['e'] == 'O' and board['c'] == 'O':
        print('Player Two Won!!')
        return 1  

    # vertical check for player2

    if board['a'] == 'O' and board['d'] == 'O' and board['g'] == 'O':
        print('Player Two Won!!')
        return 1
    if board['b'] == 'O' and board['e'] == 'O' and board['h'] == 'O':
        print('Player Two Won!!')
        return 1
    if board['c'] == 'O' and board['f'] == 'O' and board['i'] == 'O':
        print('Player Two Won!!')
        return 1
    return 0

    
while True:
    print(board['a']+'|'+board['b']+'|'+board['c'])
    print('_+_+_')
    print(board['d']+'|'+board['e']+'|'+board['f'])
    print('_+_+_')
    print(board['g']+'|'+board['h']+'|'+board['i'])
    print('_+_+_')
    end_check=check()

    if total_moves==9 or end_check==1:
        break

    while True:           # input from the player
        if player == 1:
            p1_input =input("player 1")
            if p1_input in board and board[p1_input]=='':
                board[p1_input]='X'
                player = 2
                break
            else:
                print("Invalid input ! Try again!")
        else:
            p2_input =input("player 2")
            if p2_input in board and board[p2_input]=='':
                board[p2_input]='O'
                player = 1
                break
            else:
                print("Invalid input ! Try again")
                continue
    total_moves = total_moves+1
    print('-----------------------------')
