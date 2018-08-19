from agents.baseAgent import baseAgent
class simpleAgent(baseAgent):

    def getMove(self,state=None):
        cur = super().getMove(state)
        best = self.intMin
        for space in state.spaces():
            score = self.reflexEvaluate(space)
            if score > best:
                best = score
                cur = space
        return cur
