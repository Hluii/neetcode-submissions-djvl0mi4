class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # input: 2-d array
        # output: True or False
        # check each row, then each column, the each 3x3 box
        # take each row/col/sec and sort or check for duplicates
        # Can hard code 3x3 checking
        box_list = []
        # take len before sorted and compare after
        # take a list of a row then a set and compare lengths
        col_list = [[] for _ in range(9)]
        valid_row, valid_col = {}, {}
        for row in board:
            filtered_list = list(filter(lambda s: "." not in s,row))

            if len(filtered_list) != len(set(filtered_list)):
                print("row dupe")
                return False
            for i,n in enumerate(row):
    
                # add [row][i] as list[i][row]
                col_list[i].append(n)
        
        for col in col_list:
            # need to validate like above
            filtered_list = list(filter(lambda x: "." not in x, col))
            if(len(set(filtered_list)) != len(filtered_list)):
                print("col dupe")
                return False
        # move a 3x3 box over 1-3 and down 1-3 and check
        for i in range(0,8,3):
            for j in range(0,8,3):
                box_list.append(board[i][j])
                box_list.append(board[i][j+1])
                box_list.append(board[i][j+2])
                box_list.append(board[i+1][j])
                box_list.append(board[i+1][j+1])
                box_list.append(board[i+1][j+2])
                box_list.append(board[i+2][j])
                box_list.append(board[i+2][j+1])
                box_list.append(board[i+2][j+2])
                # condense, compare, reset
                filtered_list = list(filter(lambda x: "." not in x, box_list))
                if(len(filtered_list) != len(set(filtered_list))):
                    print("boxdupe")
                    return False
                box_list = []
        return True


        
        # [i][j][i][j+1][i][j+2]
        # [i+1][j][i+1][j+1][i+1][j+2]
        # [i+2][j][i+2][j+1][i+2][j+2]
        # condense into a list and check dupe

                
        
        # what I am trying now is putting each row in a dict to check for duplicates

        # another idea is making a mask or like a copy of the 2-d array that says which 
        # numbers are not valid in each slot then checking
            
        