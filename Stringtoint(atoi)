class Solution { // did java bc i was bored of python
    public int myAtoi(String s) {
        s= s.trim();
        int sign =1;
        int i =0;
        long res = 0 ; 

        if(s.length() ==0){
            return 0; 
        }
        if(s.charAt(0) == '-'){
            sign =-1;
            i++;
        }
        else if(s.charAt(0)== '+'){
            i++;
        }

        while(i<s.length()){
            char c = s.charAt(i);

            if (c<'0' || c>'9'){// valid # 
                break; 
            }
            res = res*10 + (c-'0'); 
            if (sign * res > Integer.MAX_VALUE) return Integer.MAX_VALUE; // Handle overflow
            if (sign * res < Integer.MIN_VALUE) return Integer.MIN_VALUE;

            i++;
        }
        return   ( int) (sign *res);
    }
}
