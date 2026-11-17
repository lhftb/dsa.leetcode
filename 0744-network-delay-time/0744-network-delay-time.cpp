class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        unordered_map<int, vector<pair<int, int>>> graph;
        for (const auto& time : times) {
            int u = time[0];
            int v = time[1];
            int w = time[2];
            graph[u].push_back({v, w});
        }
        vector<int> distances(n + 1, numeric_limits<int>::max());
        distances[k] = 0;
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
        pq.push({0, k});
        vector<bool> visited(n + 1, false);
        while (!pq.empty()) {
            auto [curr_weight, node] = pq.top();
            pq.pop();
            if (visited[node]) continue;
            visited[node] = true;
            distances[node] = curr_weight;
            for (const auto& [nei, weight]: graph[node]) {
                if (!visited[nei]) {
                    distances[nei] = curr_weight + weight;
                    pq.push({curr_weight + weight, nei});
                }
            }
        }
        int mtime = 0;
        for (int i = 1; i <= n; ++i) {
            if (distances[i] == numeric_limits<int>::max()) return -1;
            mtime = max(mtime, distances[i]);
        }
        return mtime;
    }
};