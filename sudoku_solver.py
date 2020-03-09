#!/usr/bin/env python
# coding: utf-8

# In[47]:


sudoku=[
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]


# In[48]:


def showBoard(b):
    for i in range(9):
        if i%3==0 and i!=0:
            print("---------------------")
        for j in range(9):
            if j%3==0:
                print("|",end='')
            if j==8:
                print(b[i][j])
            else:
                print(b[i][j],end=' ')


# In[49]:


showBoard(board)


# In[50]:


def isEmpty(bo):
    for i in range(9):
        for j in range(9):
            if bo[i][j]==0:
                return (i,j)
    return None


# In[51]:


def isFit(bo, num, pos):
    # row Checker :
    for j in range(9):
        if bo[pos[0]][j] == num and pos[1] != j:
            return False

    # column checker :

    for i in range(9):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Square Checker
    sq = (pos[1] // 3, pos[0] // 3)

    for i in range(sq[1]*3, sq[1]*3 + 3):
        for j in range(sq[0] * 3, sq[0]*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True


# In[55]:


def solver(b):
    cell = isEmpty(b)
    if not cell:
        return True
    else:
        r, c = cell

    for i in range(1,10):
        if isFit(b, i, cell):
            b[r][c] = i

            if solver(b):
                return True

            b[r][c] = 0

    return False


# In[56]:


showBoard(sudoku)
solver(sudoku)


# In[57]:


showBoard(sudoku)

