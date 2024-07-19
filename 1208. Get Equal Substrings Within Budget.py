class Solution {
public:
    int equalSubstring(string s, string t, int maxCost) {
        int length=0;
        int j=0;
        int curr_c=0;

        for(int i=0;i<s.length();i++){
            curr_c+=abs(s[i]-t[i]);
            while(curr_c>maxCost){
                curr_c-=abs(s[j]-t[j]);
                j++;
            }
            length=max(length,i-j+1);
        }
        return length;
    }
};
