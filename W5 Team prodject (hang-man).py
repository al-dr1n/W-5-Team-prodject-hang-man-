import random


print("Welcome to Hang-man")
incorect = 0
while incorect < 9:
    parachute_1 = "  ___ "
    no_parachute_1 = ""
    parachute_2 = " /"
    no_parachute_2 = "  "
    parachute_3 = "___"
    no_parachute_3 = "   "
    parachute_4 = "\ "
    no_parachute_4 = ""
    parachute_5 = " \ "
    no_parachute_5 = "   "
    parachute_6 = "  /"
    no_parachute_6 = ""
    parachute_7 = "  \ "
    no_parachute_7 = "    "
    parachute_8 = "/"
    no_parachute_8 = " "

    p_1 = parachute_1
    p_2 = parachute_2
    p_3 = parachute_3
    p_4 = parachute_4
    p_5 = parachute_5
    p_6 = parachute_6
    p_7 = parachute_7
    p_8 = parachute_8

    if incorect == 1:
        p_1 = no_parachute_1
    if incorect == 2:
        p_1 = no_parachute_1
        p_2 = no_parachute_2
    if incorect == 3:
        p_1 = no_parachute_1
        p_2 = no_parachute_2
        p_3 = no_parachute_3
    if incorect == 4:
        p_1 = no_parachute_1
        p_2 = no_parachute_2
        p_3 = no_parachute_3
        p_4 = no_parachute_4
    if incorect == 5:
        p_1 = no_parachute_1
        p_2 = no_parachute_2
        p_3 = no_parachute_3
        p_4 = no_parachute_4
        p_5 = no_parachute_5  
    if incorect == 6:
        p_1 = no_parachute_1
        p_2 = no_parachute_2
        p_3 = no_parachute_3
        p_4 = no_parachute_4
        p_5 = no_parachute_5 
        p_6 = no_parachute_6 
    if incorect == 7:
        p_1 = no_parachute_1
        p_2 = no_parachute_2
        p_3 = no_parachute_3
        p_4 = no_parachute_4
        p_5 = no_parachute_5 
        p_6 = no_parachute_6
        p_7 = no_parachute_7
    if incorect == 8:
        p_1 = no_parachute_1
        p_2 = no_parachute_2
        p_3 = no_parachute_3
        p_4 = no_parachute_4
        p_5 = no_parachute_5 
        p_6 = no_parachute_6
        p_7 = no_parachute_7
        p_8 = no_parachute_8

    def word_place(word):
        print("  ---")

    def parachute(p_1,p_2,p_3,p_4,p_5,p_6,p_7,p_8,incorect):
        
        print(f"{p_1}\n{p_2+p_3+p_4}\n{p_5+p_6}\n{p_7+p_8}")
        
        
    word = "the"
    word_place(word)
    parachute(p_1, p_2, p_3, p_4, p_5, p_6, p_7, p_8,incorect)
    if p_8 == no_parachute_8:
        
        class dead_man:
            print("     |  ")
            print("     x  ")
            print("    /|\ ")
            print("    /|\ ")
            print(""" ____|____
| # # # # | 
|GAME OVER|  
| # ___ # |  
|___|'_|__|           
                             """)
            
    else :
        
        class man:
            print("   O  ")
            print("  /|\ ")
            print("  / \ ")
    
    input()
    incorect += 1





