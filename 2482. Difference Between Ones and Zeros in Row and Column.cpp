class Solution {
public:
    vector<vector<int>> onesMinusZeros(vector<vector<int>>& grid) {
        int rows = grid.size();
        int cols = grid[0].size(); // Assuming all rows have the same number of columns

        // Create a new vector with the same dimensions and initialize with zeros
        vector<vector<int>> newVector(rows, vector<int>(cols, 0));


        
        int* n_o=new int[cols];
        int* n_z=new int[cols];

        bool*visit=new bool[cols];
        for(int i=0;i<cols;i++)
        {
            n_o[i]=0;
            n_z[i]=0;
            visit[i]=0;
        }
        for(int i_=0;i_<rows;i_++)
        {
            int rows_one=0;
            int rows_zero=0;
            for(int jq=0;jq<cols;jq++)
            {
                if(grid[i_][jq]==1)
                {
                    rows_one++;
                }
                else
                {
                    rows_zero++;
                }
            }
            for(int j=0;j<cols;j++)
            {
                int col_one=0;
                int col_zero=0;
                if(visit[j]==0)
                {
                    for(int i=0;i<rows;i++)
                    {
                        if(grid[i][j]==1)
                        {
                            col_one++;
                        }
                        else
                        {
                            col_zero++;
                        }
                    }
                    n_o[j]=col_one;
                    n_z[j]=col_zero;
                    visit[j]=true;
                }
                
                newVector[i_][j]=rows_one+n_o[j]-rows_zero-n_z[j];
            }

        }
        return newVector;
    }
};
