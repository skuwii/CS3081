# ============================================================
# CS3081 - Artificial Intelligence
# Lab 2 - Part 2: Knowledge & Propositional Logic
# Name: _______________________
# Student ID: _________________
# ============================================================

# Import our logic helper tools
from logic3 import Symbol, Not, And, Or, Implication, KB, check_all

# ============================================================
# THE MYSTERY
# ============================================================
# A valuable item went missing at Effat University.
# Three suspects: Sara, Lina, Nora
# We have gathered the following clues (facts):
#
#   Clue 1: The person with a key is guilty.
#   Clue 2: Sara does NOT have a key.
#   Clue 3: Lina was seen near the room.
#   Clue 4: If Lina was seen near the room, she has a key.
#
# Our question: Is Lina guilty?
# ============================================================


# ============================================================
# STEP 1: Define Propositional Symbols
# Each symbol represents a statement that can be True or False.
# ============================================================

sara_key  = Symbol("SaraHasKey")
lina_key  = Symbol("LinaHasKey")
lina_seen = Symbol("LinaSeenNearRoom")
lina_guilty = Symbol("LinaIsGuilty")

# All symbols we will use (needed for model checking)
all_symbols = ["SaraHasKey", "LinaHasKey", "LinaSeenNearRoom", "LinaIsGuilty","NoraHasKey","NoraIsGuilty","SaraSeenNearRoom"]


# ============================================================
# STEP 2: Build the Knowledge Base
# We add our clues one by one using kb.tell(...)
# ============================================================

kb = KB()

# Clue 1: If Lina has a key → Lina is guilty
kb.tell(Implication(lina_key, lina_guilty))

# Clue 2: Sara does NOT have a key
kb.tell(Not(sara_key))

# Clue 3: Lina WAS seen near the room (this is a known FACT – just a symbol set to True)
# kb.tell(lina_seen)

# Clue 4: If Lina was seen near the room → Lina has a key
kb.tell(Implication(lina_seen, lina_key))

nora_key = Symbol("NoraHasKey")
kb.tell(nora_key) #Nora has a key (new evidence)

# ============================================================
# STEP 3: Ask the Knowledge Base a question (Entailment)
# ============================================================

print("=" * 50)
print("  CS3081 Lab 2 – Knowledge Base Detective")
print("=" * 50)

# Question: Does our KB prove that Lina is guilty?
answer = check_all(kb, lina_guilty, all_symbols)

if answer:
    print("\n🔍 Query:  Is Lina guilty?")
    print("✅ YES  –  The KB ENTAILS that Lina is guilty.\n")
else:
    print("\n🔍 Query:  Is Lina guilty?")
    print("❌ NO   –  The KB does NOT entail that Lina is guilty.\n")


# ============================================================
# STEP 4: Try another question
# ============================================================

answer2 = check_all(kb, sara_key, all_symbols)

print(f"🔍 Query:  Does Sara have a key?")
if answer2:
    print("✅ YES  –  The KB entails Sara has a key.\n")
else:
    print("❌ NO   –  The KB does NOT entail Sara has a key.\n")


# ============================================================
# YOUR TURN  –  Exercise 3
# Uncomment the lines below ONE AT A TIME and re-run.
# What changes in the output? Write your observations. 
# Lina has a key is true
# ============================================================

# NEW CLUE: Actually, Sara was also seen near the room.
kb.tell(lina_seen.__class__("SaraSeenNearRoom"))

# NEW QUESTION: Ask if Lina has a key.
answer3 = check_all(kb, lina_key, all_symbols)
print(f"🔍 Query:  Does Lina have a key?")
if answer3:
    print("✅ YES  –  The KB entails Lina has a key.\n")
else:
    print("❌ NO   –  The KB does NOT entail Lina has a key.\n")


nora_guilty = Symbol("NoraIsGuilty")
answer4 = check_all(kb,nora_guilty,all_symbols)
print(f"🔍 Query:  Is Nora guilty?")
if answer4:
    print("✅ YES  –  The KB ENTAILS that Nora is guilty.\n")
else:
    print("❌ NO   –  The KB does NOT entail that Nora is guilty.\n")
