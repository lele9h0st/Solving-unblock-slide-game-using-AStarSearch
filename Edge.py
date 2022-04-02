class Edge:
    def __init__(self, begin,end):
        self.begin=begin
        self.end=end
        self.weight=1

    def __init__(self, begin,end,weight=1):
        self.begin=begin
        self.end=end
        self.weight=weight
    
# a=[[1,2,3],[4,5,6]]
# print(len(a[0]))