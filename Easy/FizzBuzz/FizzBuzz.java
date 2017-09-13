// https://leetcode.com/problems/fizz-buzz/description/
class Solution {
    public List<String> fizzBuzz(int n) {
        List<String> fizzList = new ArrayList<String>();
        
        for(int i=1; i<=n; i++){
              if(i % 5 == 0 && i % 3 == 0) {
                  fizzList.add("FizzBuzz");
              } else if (i % 5 == 0) {
                  fizzList.add("Buzz");
              } else if (i % 3 == 0) {
                  fizzList.add("Fizz");
              } else {
                  fizzList.add(Integer.toString(i));
              }
         }
        
        return fizzList;
        
    }
}