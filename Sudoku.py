import os
i = 0
j = 0
'''print("0 - file output only\n1 - IDLE ouput and file output\n")
printable = input("Printable: ")
if printable != 1:
    printable = 0
'''
printable = 0
#printable = 0 -> file output only
#printable = 1 -> IDLE output & file output
sudoku = [[0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0]]

candidates =   [[0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0]]

#################################################################################################################### FILE READ

readFile = open('WriteSudokuHere.txt','r')
for k in range(81*2+1):
    c = readFile.read(1)
    if(c != ' ' and c != '\n'):
        sudoku[i][j] = int(c)
        j = j + 1
        if j == 9:
            i = i + 1
            j = 0
        if i == 9 and j == 0:
            break
        
change = [True]

for i in range(0,9):
    for j in range(0,9):
        if sudoku[i][j] != 0:
           candidates[i][j] = sudoku[i][j]
        else:
            candidates[i][j] = [1,2,3,4,5,6,7,8,9]

#################################################################################################################### SQUARE FINDER
            
def square_finder(i,j):
    array = [0,0,0,0]
    if i>=0 and i<=2:
        array[0] = 0
        array[1] = 2
    elif i>=3 and i<=5:
        array[0] = 3
        array[1] = 5
    elif i>=6 and i<=8:
        array[0] = 6
        array[1] = 8
    else:
        return "ERROR SQUARE FINDER - PARAMETERS OUT OF RANGE"
    if j>=0 and j<=2:
        array[2] = 0
        array[3] = 2
    elif j>=3 and j<=5:
        array[2] = 3
        array[3] = 5
    elif j>=6 and j<=8:
        array[2] = 6
        array[3] = 8
    else:
        return "ERROR SQUARE FINDER - PARAMETERS OUT OF RANGE"
    return array

#################################################################################################################### VERIFY FUNCTION
            
def verify(i,j,k):#verifica daca elementul sudoku[i][j] poate fi inlocuit cu elementul k dpdv al liniilor, coloanelor si patratelor
    #LINES
    for line in range(0,9):
        if sudoku[i][line] == k and j != line:
            return 0
    #COLS
    for col in range(0,9):
        if sudoku[col][j] == k and i != col:
            return 0
    #SQUARES
    array = square_finder(i,j)
    for L in range(array[0],array[1]+1):
        for C in range(array[2],array[3]+1):
            if sudoku[L][C] == k and (L != i or C != j):
                return 0;
                
    return 1;
    
#################################################################################################################### CROSSHATCHING FUNCTION
 
def crosshatching():
    occurence = [0,0,0,0,0,0,0,0,0,0] #vector de aparitii
    for i in range(0,9):
        for each in range(0,10):
            occurence[each] = 0
        for j in range(0,9):
            if sudoku[i][j] == 0:
                for number in range(1,10):
                    if verify(i,j,number) == True:
                        occurence[number] = occurence[number]+1
        for each in range(0,10):
            if occurence[each] == 1:
                for j in range(0,9):
                    if verify(i,j,each) == True and sudoku[i][j]==0:
                        sudoku[i][j] = each
                        if(printable == 1):
                            print("Element i= ",i," j= ",j," turns into: ",each,". Function: Crosshatching - Line")
                        change[0] = True
                        candidates[i][j] = each
                        
        for each in range(0,10):
            occurence[each] = 0
        for j in range(0,9):
            if sudoku[j][i] == 0:
                for number in range(1,10):
                    if verify(j,i,number) == True:
                        occurence[number] = occurence[number]+1
        for each in range(0,10):
            if occurence[each] == 1:
                for j in range(0,9):
                    if verify(j,i,each) == True and sudoku[j][i] == 0:
                        sudoku[j][i] = each
                        if(printable == 1):
                            print("Element i= ",j," j= ",i," turns into: ",each,". Function: Crosshatching - Col")
                        change[0] = True
                        candidates[j][i] = each

        array = [square_finder(0,0),square_finder(0,3),square_finder(0,6),square_finder(3,0),square_finder(3,3),square_finder(3,6),square_finder(6,0),square_finder(6,3),square_finder(6,6)]
        
        for ARR in range(0,9):
            for each in range(0,10):
                occurence[each] = 0
            for i in range(array[ARR][0],array[ARR][1]+1):
                for j in range(array[ARR][2],array[ARR][3]+1):
                    if sudoku[i][j] == 0:
                        for number in range(1,10):
                            if verify(i,j,number) == True:
                                occurence[number] = occurence[number]+1
            for each in range(0,10):
                if occurence[each] == 1:
                    for i in range(array[ARR][0],array[ARR][1]+1):
                        for j in range(array[ARR][2],array[ARR][3]+1):
                            if verify(i,j,each) == True and sudoku[i][j] == 0:
                                sudoku[i][j] = each
                                if(printable == 1):
                                    print("Element i= ",i," j= ",j," turns into: ",each,". Function: Crosshatching - Square")
                                change[0] = True
                                candidates[i][j] = each

#################################################################################################################### CANDIDATES MATRIX     

def candidate_matrix():
    for i in range(0,9): #creates candidate matrix
        for j in range(0,9):
            if sudoku[i][j] == 0:
                for number in range(1,10):
                    if verify(i,j,number) == False and number in candidates[i][j]:
                        candidates[i][j].remove(number)

    for i in range(0,9): #naked pair, triple or more
        for j in range(0,9):
            if sudoku[i][j] == 0:
                found = 1
                #Search in line, col or squarer:
                for line in range(0,9):
                    if sudoku[i][line] == 0 and candidates[i][line] == candidates[i][j] and j != line:
                        found += 1
                if found == len(candidates[i][j]):
                    for line in range(0,9):
                        if candidates[i][j] != candidates[i][line] and sudoku[i][line] == 0:
                            for each in candidates[i][j]:
                                if each in candidates[i][line]:
                                    candidates[i][line].remove(each)
                                    if(printable == 1):
                                        print("Element i=",i," j=",line," has no longer candidate ",each,". Function: Candidate Matrix - Naked elements in line. Naked type: ",found)
                found = 1
                for col in range(0,9):
                    if sudoku[col][j] == 0 and candidates[col][j] == candidates[i][j] and i != col:
                        found += 1
                if found == len(candidates[i][j]):
                    for col in range(0,9):
                        if candidates[i][j] != candidates[col][j] and sudoku[col][j] == 0:
                            for each in candidates[i][j]:
                                if each in candidates[col][j]:
                                    candidates[col][j].remove(each)
                                    if(printable == 1):
                                        print("Element i=",i," j=",line," has no longer candidate ",each,". Function: Candidate Matrix - Naked elements in col. Naked type: ",found)

                found = 1
                array = square_finder(i,j)
                for ii in range(array[0],array[1]+1):
                    for jj in range(array[2],array[3]+1):
                        if sudoku[ii][jj] == 0 and candidates[ii][jj] == candidates[i][j] and (i!=ii or j!=jj):
                            found += 1
                if found == len(candidates[i][j]):
                    for ii in range(array[0],array[1]+1):
                        for jj in range(array[2],array[3]+1):
                            if candidates[i][j] != candidates[ii][jj] and sudoku[ii][jj] == 0:
                                for each in candidates[i][j]:
                                    if each in candidates[ii][jj]:
                                        candidates[ii][jj].remove(each)
                                        if(printable == 1):
                                            print("Element i=",i," j=",line," has no longer candidate ",each,". Function: Candidate Matrix - Naked elements in square. Naked type: ",found)
                
    for i in range(0,9): #single candidate
        for j in range(0,9):
            if sudoku[i][j] == 0:
                if len(candidates[i][j]) == 1:
                    sudoku[i][j] = candidates[i][j][0]
                    change[0] = True
                    candidates[i][j] = candidates[i][j][0]
                    if(printable == 1):
                        print("Element i= ",i," j= ",j," turns into: ",candidates[i][j],". Function: Candidate Matrix - Single candidate")

#################################################################################################################### SEE IF SUDOKU IS CORRECT
    
def SEEIFCORRECT():
    for i in range(0,9):
        for j in range(0,9):
            for k in range(0,9):
                    if (sudoku[i][j] == sudoku[i][k] and j!=k) or (sudoku[i][j] == sudoku[k][j] and i!=k):
                        if printable == 1:
                            print("SUDOKU IS INCORRECT!")
                        if sudoku[i][j] == sudoku[i][k]:
                            if(printable == 1):
                                print("[",i,"][",j,"] = [",i,"][",k,"]\n")
                        else:
                            if(printable == 1):
                                print("[",i,"][",j,"] = [",k,"][",j,"]\n")
                        return 0
    return 1

#################################################################################################################### TEST LOUNGE

iterable = 0

while change[0] == True:
    iterable += 1
    change[0] = False
    crosshatching()
    candidate_matrix()
    if change[0] == True:
        if(printable == 1):
            print("NUMBER OF CYCLE: ",iterable,"\n")

#################################################################################################################### FILE OUTPUT

writefile = open('AndGetItFromHere.txt','w')
for i in range(0,9):
    if i%3 == 0 and i != 0:
        writefile.write("----------------------\n")
    for j in range(0,9):
        if j%3==0 and j != 0:
            writefile.write("| ")
        writefile.write(str(sudoku[i][j]))
        writefile.write(" ")
    writefile.write("\n")
writefile.write("\nNumber of cycles: ")
writefile.write(str(iterable-1))
writefile.write("\nSUDOKU STATUS: ")
writefile.write(str(SEEIFCORRECT()))
if SEEIFCORRECT() == 0:
    writefile.write("\nWouldn't you like to struggle and do this sudoku by yourself???")
else:
    if printable == 1:
        print("SUDOKU IS CORRECT!\n")
    writefile.write("\nEasy peasy lemon squeezy.")

#################################################################################################################### IDLE OUTPUT

#IDLE PRINT
if printable == 1:
    print("SUDOKU MATRIX: ")
    for i in range(0,9):
        if i%3 == 0 and i != 0:
            print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n")
        for j in range(0,9):
            if j%3==0 and j != 0:
                print("  |",end='')
            print('\t',sudoku[i][j],end=' ')
        print("\n")

writefile.close()
readFile.close()
if printable == 0:
    #os.startfile("C:\\Users\\Mihai\\Desktop\\Sudoku Solver\\AndGetItFromHere.txt")
    os.startfile("AndGetItFromHere.txt")
    
if(printable == 1):
    input("")
'''

easy:
4 0 0 0 0 2 8 3 0
0 8 0 1 0 4 0 0 2
7 0 6 0 8 0 5 0 0
1 0 0 0 0 7 0 5 0
2 7 0 5 0 0 0 1 9
0 3 0 9 4 0 0 0 6
0 0 8 0 9 0 7 0 5
3 0 0 8 0 6 0 9 0
0 4 2 7 0 0 0 0 3

medium:
5 0 0 0 9 4 0 0 0
0 0 6 7 0 3 9 0 5
0 2 0 0 6 1 0 0 0
8 0 1 0 0 0 6 4 0
0 0 0 0 0 0 0 0 0
0 6 3 0 0 0 2 0 9
0 0 0 9 4 0 0 2 0
3 0 9 2 0 5 7 0 0
0 0 0 1 3 0 0 0 4

hard:
0 0 0 0 0 7 0 9 0
4 0 7 0 0 0 8 0 0
0 0 0 0 6 0 0 0 0
0 0 2 4 0 0 5 0 0
7 9 0 3 0 0 0 2 0
0 0 0 0 0 5 0 0 0
2 0 0 5 0 0 9 0 0
9 0 0 0 0 6 0 3 8
0 1 6 9 0 0 0 0 0

very hard:
3 0 0 0 2 0 0 0 0
2 1 0 7 0 9 0 3 0
7 0 0 0 0 1 0 5 0
0 0 9 0 0 0 0 0 0
0 0 3 9 0 5 0 0 0
0 0 0 0 8 0 9 0 0
0 0 0 0 0 8 0 1 6
0 2 0 4 0 0 0 0 0
4 0 8 0 0 0 3 0 7

very hard #2: not solved
0 8 0 0 0 0 0 0 4
0 0 0 0 0 2 7 5 0
0 7 5 6 0 0 8 9 0
0 0 0 2 0 0 0 0 8
3 0 9 8 4 6 5 0 7
8 0 0 0 0 5 0 0 0
0 9 8 0 0 7 3 4 0
0 6 3 1 0 0 0 0 0
5 0 0 0 0 0 0 7 0

very hard #3:
0 0 0 0 0 0 8 0 6
0 4 5 0 0 0 3 0 0
0 0 0 0 0 9 0 0 4
0 9 3 0 5 0 1 0 0
7 0 0 0 0 1 0 0 0
0 6 0 0 9 0 0 2 0
0 0 0 9 4 0 0 0 1
0 3 0 0 0 0 0 7 0
4 7 6 0 0 0 0 0 2

'''
