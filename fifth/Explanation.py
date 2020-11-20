import os

class Explanation:
    def explanation(self):
        print('****************************************')
        print("*                                      *")
        print("*      Welcome to Stinkin' Dungeon     *")
        print("*                                      *")
        print("*       A simple text-based RPG        *")
        print("*                                      *")
        print("*      Design: Reijer Grimbergen       *")
        print("*                                      *")
        print("****************************************")

        print()
        print("1) Show the rules of the game")
        print("2) Start the game")
        while True:
            user_select = input('Please enter selection.')

            if user_select == '1':
                print("Rules of Stinkin' Dungeon:")
                print("==========================")
                print("1) You are a prince and in room (1,1) of the Dungeon of the Stinkers")
                print("2) Somewhere in this dungeon there is a princess that you must rescue from the Stinkers")
                print("3) There are two Stinkers and one Super Stinker in this dungeon")
                print("4) When you enter a room with a Stinker, you must fight him")
                print("5) When fighting a Stinker, your health points will go down")
                print(
                    "6) To improve your chances of beating a Stinker, you need a sword that is somewhere in the dungeon")
                print(
                    "7) If you survive a Stinker fight, you can restore your health by drinking an health potion that is somewhere in the dungeon")
                print(
                    "8) You cannot carry a health potion with you. If you want to use it you must go back to the room you found it")
                print("9) The princess is in the room with the Super Stinker")
                print("10) To enter the room with the Super Stinker you need two keys")
                print(
                    "11) Each Stinker holds one of the keys. If you defeat a Stinker, you will get the key he carries.")
                print("12) Each room has a number of doors through which you can go to get to the other rooms")
                print("13) Only by visiting a room, you will get access to the information about this room")
                print("14) The Stinkers smell so bad that you can smell them in the neighboring room")
                os.system('ECHO Press any key to start the game.')
                os.system('PAUSE > NUL')
                return

            elif user_select == '2':
                return

            else:
                continue