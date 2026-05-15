class Solution {
public:
    int getSubboxID(int rows, int cols)
    {
        return (rows / 3) * 3 + (cols / 3) + 1;
    }
    
    bool isValidSudoku(vector<vector<char>>& board) {
        vector<vector<unordered_set<int>>> validator;
        for(int i = 1; i<= 9; i++)
        {
            unordered_set<int> row_validator;
            unordered_set<int> column_validator;
            unordered_set<int> subbox_validator;
            vector<unordered_set<int>> digit_validator = {row_validator, column_validator, subbox_validator};
            validator.push_back(digit_validator);
        }
        for(int i = 1; i<= 9; i++)
        {
            for(int j = 1; j<= 9; j++)
            {
                if (board[i-1][j-1] == '.') continue;
                int num = board[i-1][j-1] - '1';
                int k = getSubboxID(i-1,j-1);
                if(validator[num][0].contains(i)) return false;
                else validator[num][0].insert(i);
                if(validator[num][1].contains(j)) return false;
                else validator[num][1].insert(j);
                if(validator[num][2].contains(k)) return false;
                else validator[num][2].insert(k);
            }
        }
        return true;
    }
};
