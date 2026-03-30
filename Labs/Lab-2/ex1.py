from logic import *

# T
# T
# T
# T

P = Symbol("P")
Q = Symbol("Q")

knowledge = Implication(And(P,Q),Or(P,Not(Q)))
print(knowledge.formula())
print(model_check(knowledge,knowledge))
