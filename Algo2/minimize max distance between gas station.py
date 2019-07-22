import heapq
class Solution(object):
    def minmaxGasDist(self, stations, K):
        """
        :type stations: List[int]
        :type K: int
        :rtype: float
        """
        stations.sort()
        print(stations)
        q = []
        n = len(stations)
        for i in range(n - 1):
            heapq.heappush(q, (stations[i] - stations[i + 1], 1, i, i + 1))
            print(q)
        ans = q[0][0]
        while K:
            _, num, i, j = heapq.heappop(q)
            print('after pop',_, num, i, j)
            threshold = -q[0][0]
            print('threshold is ',threshold)
            cnt = int((stations[j] - stations[i]) / threshold) + 1
            x = min(K, cnt - num)
            K -= x
            heapq.heappush(q, (-1.0 * (stations[j] - stations[i]) / (num + x), num + x, i, j))
        return q


a=Solution()
print(a.minmaxGasDist([1,5,10],3))