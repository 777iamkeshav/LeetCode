class Solution:
    def decodeString(self, s: str) -> str:

        dq = deque()


        for sym in s:

            if sym != "]":

                dq.append(sym)

            else:

                st = []

                while (sym1:=dq.pop()) != "[":

                    st.append(sym1)

                dig = ""

                #print(dq)

                #print(f"st = {st}")

                #print(dq[-1])

                while dq and dq[-1] in "0123456789":

                    

                    d = dq.pop()

                    dig = d + dig

                #print(f"dig = {dig}")

                dig = int(dig)

                st = st[::-1] * dig

                dq.extend(st)

        #print(dq)

        return "".join(dq)

                    








        
        