from sys import stdin as si
from sys import maxsize as m

class SegmentTree(object):

    def __init__(self, lst):
        self.given_list = lst
        self.segment_list = [0]*(2*len(self.given_list)+1)

    def create_tree(self, i, j, p):
        
        if i == j:
            self.segment_list[p] = self.given_list[i] # or j

        else:
            mid = i+(j-i)//2
            self.segment_list[p] = min(self.create_tree(i,mid,2*p+1),
                                       self.create_tree(mid+1,j,2*p+2))
        return self.segment_list[p]

    def get_range_min(self, s, e, qs, qe, p):
        print (s, e, qs, qe, p)
        if qe < s or qs> e:
            return m
        elif qs<=s and  e<=qe:
            # given range is completely inside the range of the node
            return self.segment_list[p]
        else:
            mid = s+(e-s)//2
            return min(self.get_range_min(s,mid,qs,qe,2*p+1),
                       self.get_range_min(mid+1,e,qs,qe,2*p+2))


if __name__=="__main__":
    for _ in range(int(si.readline().strip())):
        lst = list(map(int, si.readline().strip().split()))
        st = SegmentTree(lst)
        st.create_tree(0,len(lst)-1,0)
        print(lst)
        print (st.segment_list)
        for _ in range(int(si.readline().strip())):
            x,y = map(int,si.readline().strip().split())
            print (st.get_range_min(0,len(lst)-1,x,y,0))
