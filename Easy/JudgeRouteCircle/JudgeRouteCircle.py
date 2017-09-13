# https://leetcode.com/problems/judge-route-circle/description/
class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        y = 0
        x = 0
        
        for move in moves:
            if move.lower() not in ['u', 'd', 'l', 'r']:
                ValueError('Valid moves are "U", "D", "L", or "R". Enter them as a continuous string, not separated by any characters or spaces.')
            
            if move.lower() == "u":
                y += 1
            elif move.lower() == "d":
                y -= 1
            elif move.lower() == "r":
                x += 1
            elif move.lower() == "l":
                x -= 1
        
        result = False
        if x == 0 and y == 0:
            result = True
        
        return result
        