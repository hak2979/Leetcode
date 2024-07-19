class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        x_t=[]
        score=0
        for i in s:
            x_t.append(i)
        y_t=[]
        z_t=[]


        if y>x:
            for i in range(len(x_t)):
                if len(y_t)>0:
                    if y_t[len(y_t)-1]=='b' and x_t[i]=='a':
                        y_t.pop()
                        score+=y
                    else:
                        y_t.append(x_t[i])
                else:
                    y_t.append(x_t[i])

            for i in range(len(y_t)):
                if len(z_t)>0:
                    if z_t[len(z_t)-1]=='a' and y_t[i]=='b':
                        z_t.pop()
                        score+=x
                    else:
                        z_t.append(y_t[i])
                else:
                    z_t.append(y_t[i])
        else:

            for i in range(len(x_t)):
                if len(y_t)>0:
                    if y_t[len(y_t)-1]=='a' and x_t[i]=='b':
                        y_t.pop()
                        score+=x
                    else:
                        y_t.append(x_t[i])
                else:
                    y_t.append(x_t[i])
            
            for i in range(len(y_t)):
                if len(z_t)>0:
                    if z_t[len(z_t)-1]=='b' and y_t[i]=='a':
                        z_t.pop()
                        score+=y
                    else:
                        z_t.append(y_t[i])
                else:
                    z_t.append(y_t[i])

        return score





        
