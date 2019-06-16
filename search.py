import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
          actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()

def genericSearch(problem, fringe, add_to_fringe_fn):
  """
  a node is a triple - (state, cost, path)
  where actions are the actions excuted from  the initial 
  state to the current state.
  """
  closed = set()
  start = (problem.getStartState(), 0, [])  # (state, cost, actions) 
  add_to_fringe_fn(fringe, start, 0)

  while not fringe.isEmpty():
    state, cost, actions = fringe.pop()

    if problem.isGoalState(state):
      return actions

    if not state in closed:
      closed.add(state)

      for newState, newAction, newCost in problem.getSuccessors(state):
        nextNode = (newState, cost+newCost, actions+[newAction])
        add_to_fringe_fn(fringe, nextNode, cost+newCost)

def depthFirstSearch(problem):
    """Search the deepest nodes in the search tree first."""
    fringe = util.Stack()
    def add_to_fringe_fn(fringe, node, cost):
      fringe.push(node)
    
    return genericSearch(problem, fringe, add_to_fringe_fn)

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    fringe = util.Queue()
    def add_to_fringe_fn(fringe, node, cost):
      fringe.push(node)

    return genericSearch(problem, fringe, add_to_fringe_fn)

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    fringe = util.PriorityQueue()
    def add_to_fringe_fn(fringe, node, cost):
      fringe.push(node, cost)

    return genericSearch(problem, fringe, add_to_fringe_fn)

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    fringe = util.PriorityQueue()
    def add_to_fringe_fn(fringe, node, cost):
      cost += heuristic(node[0], problem)
      fringe.push(node, cost)
    
    return genericSearch(problem, fringe, add_to_fringe_fn)

def wrongPositionHeuristic(state, problem, info={}):
  wrongNumber = 0
  i = 0
  for row in range(3):
    for col in range(3):
      if state.cells[row][col] != i:
        wrongNumber += 1
      i += 1
  return wrongNumber

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
