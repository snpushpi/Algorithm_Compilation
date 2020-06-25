class FenwickTree():
    def __init__(self,n):
        self.Binary_index_tree = [0]*(n+1)
        self.n = n
    def update(self,i,delta):
        '''At ith index of the main array, there is an update or we increase the value by delta, so we will change our fenwick tree
        based on that.'''
        i+=1
        while i<=self.n:
            self.Binary_index_tree[i]+=delta
            i+= i & (-i)
    def sum(self,i):
        '''gives sum from index to index i of the original array.'''
        sum=0
        i+=1
        while i>=0:
            sum+=self.Binary_index_tree[i]
            i-=i & (-i)

    def construct(self,arr):
        '''given an array, it constructs the Bindary_index_tree based on the update method.'''
        for i in range(self.n):
            self.update(i,arr[i])
        return  self.Binary_index_tree

    
