// https://leetcode.com/problems/island-perimeter/description/
class Solution {
    public int islandPerimeter(int[][] grid) {
        int perimeter = 0;
        
        for (int r = 0; r < grid.length; r++) {
            for (int d = 0; d < grid[r].length; d++) {
                
                int land = grid[r][d];
                
                if (land == 1) {
                    
                    int landT = ((r != 0) ? grid[r-1][d] : 0);
                    int landB = ((r+1 < grid.length) ? grid[r+1][d] : 0);
                    int landL = ((d != 0) ? grid[r][d-1] : 0);
                    int landR = ((d+1 < grid[r].length) ? grid[r][d+1] : 0);
                    
                    perimeter += land - landT;
                    perimeter += land - landB;
                    perimeter += land - landL;
                    perimeter += land - landR;
                    
                }
                             
            }
        }
        return perimeter;
    }
}