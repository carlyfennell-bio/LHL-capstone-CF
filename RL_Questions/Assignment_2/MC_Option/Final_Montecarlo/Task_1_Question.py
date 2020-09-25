import csv
import sys

Current_Card_combination = {}
Suggested_Combination = {}
op = {}

if len(sys.argv)>1:
    gamma = float(sys.argv[1])

else:
    gamma = 0.9

if len(sys.argv)>2:
    epsilon = float(sys.argv[2])

else:
    epsilon = 0.001

def readfile():
    with open('Transition_Probabilities.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            if row[0] in Current_Card_combination:
                if row[1] in Current_Card_combination[row[0]]:
                    Current_Card_combination[row[0]][row[1]].append((float(row[3]), row[2]))
                else:
                    Current_Card_combination[row[0]][row[1]] = [(float(row[3]), row[2])]
            else:
                Current_Card_combination[row[0]] = {row[1]:[(float(row[3]),row[2])]}


    with open('Probabilistic_Rewards.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            Suggested_Combination[row[0]] = float(row[1]) if row[1] != 'None' else None

readfile()

class MDProcess:
    def __init__(self, transition={}, reward={}, gamma=.9):
        self.states = transition.keys()
        self.transition = transition
        self.reward = reward
        self.gamma = gamma

    def R(____, ____):
        _________________________

    def actions(_____, ____):
        _________________________

    def T(____, ____, ____):
        _________________________

mdp = MDProcess(transition=Current_Card_combination, reward=Suggested_Combination)

def value_iteration():
    states = mdp.states
    actions = mdp.actions
    T = mdp.T
    R = mdp.R
    V1 = {s: 0 for s in states}
    
    while True:
        _____________________
        _____________________
        _____________________
        _____________________
        _____________________
        _____________________
        _____________________

def best_policy(V):
    _____________________
    _____________________
    _____________________
    _____________________
    _____________________
    _____________________

def expected_utility(a, s, V):
    T = mdp.T
    return sum([p * V[s1] for (p, s1) in mdp.T(s, a)])

def Add_prob():
    for k,v in op.items():
        for v1 in Current_Card_combination[k][v[0]]:
            if k==v1[1]:
                op[k].append(v1[0])
                
def main():
    V = value_iteration()
    pi = best_policy(V)
    print ('\nOptimal policy is \nState - Action')
    for s in pi:
        op[s] = [pi[s]]
        print (s, ' --> ' , pi[s])
    Add_prob()

if __name__ == '__main__':
    main()