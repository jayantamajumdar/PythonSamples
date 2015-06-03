# Gambler's ruin Simulation for Roulette with probability of winning = 18/37 
# Goal: find optimal betting strategy

# Trials := number of simulations
# Plays := Maximum number of spins per simulation 
# Cash := Bet Amount


import numpy as np

trials = 10000.0
plays = 100.0
cash = 20.0

# Spin is randomly generated 10000x100x20 matrix with values picked from uniform distribution 
# Wins is True
spin = np.random.rand(cash, trials, plays)
wins = spin > (18.0/37.0)



new = []

# Random Walk matrix with step forward (maxBet amount) for wins matrix = True, 
# step back for entries in win matrix = False
for i in range(int(cash)):
	maxBet = i+1
	bet= np.where(wins[i,:,:] == True, maxBet, -maxBet)
	new.append(bet)


# Newstack is np array of size 100x10000x20 which translates the 
# true/false wins matrix to a win/loss amount for each bet (if that bet is placed)

newstack = np.vstack(new)
newstack = newstack.reshape(cash, trials, plays)
newstack = newstack.swapaxes(0,2) 


# State Matrix to keep track of current amount of cash remaining
# newState calculates amount left following next bet
state = np.zeros((trials, cash))
newState = np.zeros((trials, cash))



for i in range(int(cash)):
	bet = i + 2
	for j in range(int(plays)):
		state[:] = cash
		statecheck = np.where(state[:] > bet, True, False)
		newState = state + newstack[i,:,:]

# newState has the final values for all 10000 simulations of each of the 20 options for betting amounts
# We average across these values to find the expected amount a player walks away with at the end of 100 plays

average = np.mean(newState, axis =0)
print average

print 'The optimal betting strategy from this simulation is: ' + str(np.argmax(average)+1)
