from agents.baseAgent import baseAgent
class simpleAgent(baseAgent):

    def getMove(self,state=None):
        super().getMove(state)
        cur = None
        best = self.intMin
        for space in state.spaces():
            score = self.reflexEvaluate(space)
            if score > best:
                best = score
                cur = space
        return cur
