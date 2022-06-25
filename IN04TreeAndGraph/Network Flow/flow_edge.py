class Edge:
    def __init__(self, fromVec, toVec, capacity=None, flow=0):
        self.fromVec = fromVec
        self.toVec = toVec
        self.__capacity = capacity
        self.flow = flow

    def change_capacity(self, capacity):
        self.__capacity = capacity

    def add_flow(self, flow):
        if self.flow + flow > self.__capacity:
            print("{}--{} > out of capacity".format(self.fromVec, self.toVec))
            return
        self.flow += flow

    def get_capacity(self):
        return self.__capacity

    def print_edge(self):
        print("{0}--({1}/{2})--{3}".format(self.fromVec,
              self.flow, self.__capacity, self.toVec))
