#in this construction, we didn't keep the make set operation, we fix the total number of elements 
#in the very beginning, or device a way to map the elements to unique integers.
class DisjointSetUnion():
    def __init__(self,n):
        self.rank = [1]*n
        self.parent = [i for i in range(n)]
    def find(self,item):
        '''find the representative of that integer and also applies path compression.'''
        if self.parent[item]!=item:
            self.parent[item]=self.find(self.parent[item])
        return self.parent[item]
    def union(self,x,y):
        '''Unify elements x and y, or if they are in two different trees, point one's representative to another.'''
        rep_x = self.find(x)
        rep_y = self.find(y)
        if rep_x==rep_y:#they are in the same tree, so just return the function
            return 
        if self.rank[rep_x]>self.rank[rep_y]:
            self.parent[rep_y]=self.parent[rep_x]
        elif self.rank[rep_x]<self.rank[rep_y]:
            self.parent[rep_x]=self.parent[rep_y]
        else:
            self.parent[rep_y]=rep_x
            self.rank[rep_x]=self.rank[rep_x]+1

