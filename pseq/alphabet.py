
class Alphabet:
    def __init__(self, alphabet):
        pass

class Pairing:
    def __init__(self,left,right):
        self.data = dict()
        # assert left is str, "left has to be string or character"
        # assert right is str, "right has to be string or character"

        for c1,c2 in zip(left,right):
            print(c1,c2)
            if c1 in self.data:
                del self.data[c1]
            if c2 in self.data:
                del self.data[c2]
            self.data[c1] = c2
            self.data[c2] = c1

    def __getitem__(self, key):
        if key is str:
            return  [self.data[i] for i in key]
        else:
            return self.data[key]
    def __len__(self):
        return len(self.data) // 2
