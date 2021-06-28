import random
import sys


while True:
    a=input("Enter R to Rotate a Dice")
    b=(random.randint(1,6))
    if a=="r" or a=="R":
    
        if b==1:
            print("""|-------|""")
            print("""|       |""")
            print("""|   O   |""")
            print("""|       |""")
            print("""|       |""")
            print("""|-------|""")

        elif b==2:
            print("""|-------|""")
            print("""|       |""")
            print("""|   O   |""")
            print("""|   O   |""")
            print("""|       |""")
            print("""|-------|""")

        elif b==3:
            print("""|-------|""")
            print("""|   O   |""")
            print("""|   O   |""")
            print("""|   O   |""")
            print("""|       |""")
            print("""|-------|""")

        elif b==4:
            print("""|-------|""")
            print("""|       |""")
            print("""| O   O |""")
            print("""| O   O |""")
            print("""|       |""")
            print("""|-------|""")

        elif b==5:
            print("""|-------|""")
            print("""|   O   |""")
            print("""|  O O  |""")
            print("""|  O O  |""")
            print("""|   O   |""")
            print("""|-------|""")

        elif b==6:
            print("""|-------|""")
            print("""|  O O  |""")
            print("""|  O O  |""")
            print("""|  O O  |""")
            print("""|       |""")
            print("""|-------|""")
            
    else:
        print("end")
        sys.exit()


        
        
