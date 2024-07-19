class Solution {
public:
    int numSteps(string s) {

        if(s[s.length()-1]=='1' && s.length()<=1){
            return 0;
        }
        else{
            int move=0;
            while(!(s[s.length()-1] == '1' && s.length()==1)){
                move++;
                if(s[s.length()-1]=='0'){
                    string x="";
                    for(int i=0;i<s.length()-1;i++){
                        x+=s[i];
                    }
                    s=x;
                }
                else{
                    int l_in=s.length()-1;
                    s[l_in]='0';
                    l_in--;
                    int carry=1;
                    while(l_in>-1){
                        if(s[l_in]=='0'){
                            s[l_in]='1';
                            carry=0;
                            break;
                        }
                        else{
                            s[l_in]='0';
                            carry=1;
                        }
                        l_in--;
                    }
                    if(carry==1){
                        string x="1";
                        for(int i=0;i<s.length();i++){
                            x+=s[i];
                        }
                        s=x;
                    }


                }
            }
            return move;
        } 
    }
};
