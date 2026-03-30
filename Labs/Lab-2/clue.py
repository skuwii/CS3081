import termcolor

from logic import *

alice = Symbol("AliceSuspect")
bob = Symbol("BobSuspect")
carol = Symbol("CarolSuspect")
characters = [alice, bob, carol]

office = Symbol("office")
garage = Symbol("garage")
basement = Symbol("basement")
rooms = [office, garage, basement]

poison = Symbol("poison")
rope = Symbol("rope")
candlestick = Symbol("candlestick")
weapons = [poison, rope, candlestick]

symbols = characters + rooms + weapons


def check_knowledge(knowledge):
    for symbol in symbols:
        if model_check(knowledge, symbol):
            termcolor.cprint(f"{symbol}: YES", "green")
        elif not model_check(knowledge, Not(symbol)):
            termcolor.cprint(f"{symbol}: MAYBE","yellow")
        else:
            termcolor.cprint(f"{symbol}:NO","red")

# There must be a person, room, and weapon.
knowledge = And(
    Or(alice, bob, carol),
    Or(office, garage, basement),
    Or(poison, rope, candlestick)
)

# Initial cards
knowledge.add(And(
    Not(alice), Not(office), Not(poison)
))

# Opponent card
knowledge.add(Or(
    Not(bob), Not(garage), Not(rope)
))

# Learned cards
knowledge.add(Not(candlestick))
knowledge.add(Not(basement))

check_knowledge(knowledge)
