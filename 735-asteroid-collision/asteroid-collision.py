class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st=[]
        for i in range(len(asteroids)):
            if asteroids[i]>0:
                st.append(asteroids[i])
                
            else:
                a=asteroids[i]
                while  st and a != 0:
                    if st[-1]<0 and a<0:
                        break
                    if abs(a)<abs(st[-1]):
                        a=0
                    elif abs(a)>abs(st[-1]):
                        st.pop(-1)
                    elif abs(a)==abs(st[-1]):
                        a=0
                        st.pop(-1)
                if a!=0:
                    st.append(a)

                
                
        return st



            