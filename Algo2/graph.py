class vertex:
    def __init__(self,n):
        self.name=n
        self.nbr=list()
    def add_nbr(self,v):
        if v not in self.nbr:
            self.nbr.append(v)
            self.nbr.sort()


class graph:
    vertices={}
    def add_v(self,vx):
        if isinstance(vx,vertex) and vx.name not in self.vertices:
            self.vertices[vx.name]=vx
            return True
        else:
            return False
    def add_e(self,u,v):
        if u in self.vertices and v in self.vertices:
            for key,value in self.vertices.items():
                if key==u:
                    value.add_nbr(v)
                if key==v:
                    value.add_nbr(u)
            return True
        else:
            return False
    def print(self):
        for key in sorted(list(self.vertices.keys())):
            print(key+str(self.vertices[key].nbr))

g=graph()
a=vertex('a')
g.add_v(a)
b=vertex('b')
g.add_v(b)


g.add_e('a','b')

g.print()
