from src.filers.pickle_file_manager import load_trie
from src.model.trie import TrieNode


dirs = ((0,1),(1,0), (0,-1), (-1,0))
def solve_wend(grid:list[list[str]], config: list[int])->list[list[int]]:
    
    config.sort()
    trie = load_trie()
    
    possibilities:dict[int,list[list[tuple[int,int]]]] = ({
        i:[] for i in config 
    })
    m,n = len(grid),len(grid[0])
    curPath=[]
    def dfs(curNode:TrieNode, i:int, j:int):
        if curNode.is_end and len(curPath) in possibilities:
            possibilities[len(curPath)].append(curPath.copy())
        
        for dx,dy in dirs:
            x,y=i+dx,j+dy
            if (-1<x<m 
                and -1<y<n 
                and grid[x][y]!="#" 
                and grid[x][y] in curNode.children):
                
                temp,grid[x][y]=grid[x][y],"#"
                curPath.append((x,y))
                dfs(curNode.children[temp], x,y)
                curPath.pop()
                grid[x][y]=temp
                        

    for i in range(m):
        for j in range(n):
            if grid[i][j]!=".":
                curPath.append((i,j))
                temp,grid[i][j]=grid[i][j], "#"
                dfs(trie.get_papa(temp),i,j)
                grid[i][j]=temp
                curPath.pop()
    
    print(possibilities)
    return []


# traverse dfs
# keep track of path
# if word and word len in config then add to possibilities
# continue until no more
# see possibilities and pick one answer


def main():
    