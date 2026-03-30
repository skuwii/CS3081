from logic import *
import termcolor

rain = Symbol("rain")
hagrid = Symbol("hagrid")
dumbledore = Symbol("dumbledore")
snape = Symbol("snape")

knowledge = And( 
    Or(hagrid, dumbledore, snape),    
    Not(And(hagrid, dumbledore)),     
    Not(And(hagrid, snape)),          
    Not(And(dumbledore, snape)),      
    Implication(rain, Not(snape)),    
    snape,                            
)

symbols = [rain, hagrid, dumbledore, snape]
for symbol in symbols:
    if model_check(knowledge, symbol):
        termcolor.cprint(f"{symbol}: YES", "green")
    elif not model_check(knowledge, Not(symbol)):
        print(f"{symbol}: MAYBE")
    else:
        termcolor.cprint(f"{symbol}: NO","red")
