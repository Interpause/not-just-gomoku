from agents.baseAgent import baseAgent
class simpleAgent(baseAgent):
    '''A simple agent that plays using shallow reflexEvaluate to decide.'''

    def getMove(self,state=None):
        cur = super().getMove(state)
        best = self.intMin
        for space in state.spaces():
            score = self.reflexEvaluate(space)
            if score > best:
                best = score
                cur = space
        return cur
