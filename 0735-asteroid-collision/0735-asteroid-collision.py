class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:

        st = []

        for x in asteroids:
            
            while st and st[-1] > 0 and x < 0:
                if abs(x) > st[-1]:
                    st.pop()

                elif abs(x) < st[-1]:
                    x = 0
                    break

                elif abs(x) == st[-1]:
                    st.pop()
                    x = 0
                    break

            if x != 0:
                st.append(x)
        
        return st