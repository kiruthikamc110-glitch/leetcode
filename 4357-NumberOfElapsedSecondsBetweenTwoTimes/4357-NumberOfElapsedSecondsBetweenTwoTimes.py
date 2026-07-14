# Last updated: 14/07/2026, 14:56:32
class Solution(object):
    def secondsBetweenTimes(self, startTime, endTime):
        """
        :type startTime: str
        :type endTime: str
        :rtype: int
        """
        def toSeconds(t):
            h, m, s = map(int, t.split(":"))
            return h * 3600 + m * 60 + s

        return toSeconds(endTime) - toSeconds(startTime)