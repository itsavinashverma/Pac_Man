from maze import *
from exception import *
from stack import *
class PacMan:
    def __init__(self, grid : Maze) -> None:
        ## DO NOT MODIFY THIS FUNCTION
        self.navigator_maze = grid.grid_representation
    def find_path(self, start, end):
        # IMPLEMENT FUNCTION HERE
        n = len(self.navigator_maze)
        m = len(self.navigator_maze[0])

        #if starting and ending point have ghost
        if self.navigator_maze[start[0]][start[1]] == 1 or self.navigator_maze[end[0]][end[1]]==1:
            raise PathNotFoundException()
        
        vis = [[False for _ in range(m)] for _ in range(n)]
        st = Stack()
        st.push((start,[start]))
        vis[start[0]][start[1]] = True

        dir = [(0,1), (1,0), (0,-1), (-1,0)]  # Right, Down, Left, Up

        while not st.is_empty():
            (x,y),path = st.pop()

            if (x,y) == end:
                return path
            
            for dx, dy in dir:
                nx = x + dx
                ny = y + dy

                if 0 <= nx < n and 0 <= ny < m:
                    if self.navigator_maze[nx][ny] == 0 and not vis[nx][ny]:
                        vis[nx][ny] = True
                        st.push(((nx,ny), path + [(nx,ny)]))



        raise PathNotFoundException()
