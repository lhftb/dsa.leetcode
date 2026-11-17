class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        vector<pair<int, int>> directions = {
            {  1,  0 },
            {  0,  1 },
            { -1,  0 },
            {  0, -1 }
        };
        int islands = 0;
        int m = grid.size();
        int n = grid[0].size();
        vector<vector<bool>> visited(m, vector<bool>(n, false));
        auto dfs = [&](this const auto& self, int i, int j) -> void {
            if (grid[i][j] != '1' || visited[i][j]) {
                return;
            }
            visited[i][j] = true;
            for (auto [x, y] : directions) {
                x += i;
                y += j;
                if (x >= 0 && x < m && y >= 0 && y < n) {
                    self(x, y);
                }
            }
        };
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] == '1' && !visited[i][j]) {
                    islands += 1;
                    dfs(i, j);
                }
            }
        }
        return islands;
    }
};