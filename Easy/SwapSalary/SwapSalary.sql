-- https://leetcode.com/problems/swap-salary/description/
UPDATE salary SET sex = CASE
         WHEN sex = 'f' THEN 'm'
         WHEN sex = 'm' THEN 'f'
       END
       