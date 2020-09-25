import Task_1_solutions
import numpy as np
from matplotlib import pyplot as plt
import random
import csv
import sys

class Configuration:
     def __init__(self, NumberOfScenarios):
         self.NumberOfScenarios=NumberOfScenarios

class OptionsAvailable:
  def __init__(self, Current_balance, WTB_amount, guaranteed_win, time_remaining):
        self.Current_balance=Current_balance
        self.WTB_amount=WTB_amount
        self.guaranteed_win=guaranteed_win
        self.time_remaining = time_remaining

class BEModel:
    def __init__(self, Configuration):
        self.Configuration = Configuration

    def BASP_Array(self, hand):
        BASP = []
        timestep = 1 #60 minutes
        for scenarioNumber in range(self.Configuration.NumberOfScenarios):
            normal_random_number = np.random.normal(0, 1)
            next_hand = (hand.guaranteed_win)-0.5*((1-0.15)**2)
            unpredictability =(1-0.15)*np.sqrt(timestep)*normal_random_number
            price = hand.Current_balance * np.exp(next_hand+unpredictability)
            BASP.append(price)
        return BASP

class OptionHandPayoutCalculator:
    def CalculateBASP(self, hand, BASP_per_scenario):
        pay_outs = 0
        total_scenarios = len(BASP_per_scenario)
        for i in range(total_scenarios):
            price = BASP_per_scenario[i]
            pay_out = price - hand.WTB_amount
            if(pay_out>0):
                pay_outs=pay_outs+pay_out

        amount_after_risk_reduction = (np.exp(-1.0*hand.guaranteed_win*hand.time_remaining)*pay_outs)
        result = amount_after_risk_reduction/total_scenarios
        return result

def plot_scenario_paths(hand, BASP_per_scenario):
     x=[]
     y=[]
     for i in BASP_per_scenario:
            y.append(i)
            y.append(hand.Current_balance)
            x.append(1)
            x.append(0)
            plt.plot(x, y)

     plt.ylabel('Current Balance')
     plt.xlabel('Time Remaining')
     plt.show()

class MonteCarlo:
    def __init__(self, configuration, model):
        self.configuration = configuration
        self.model = model

    def Simulate(self, hand, hand_BASP):
        BASP_per_scenario = self.model.BASP_Array(hand)
        #plot_scenario_paths(hand, BASP_per_scenario)
        price = hand_BASP.CalculateBASP(hand, BASP_per_scenario)
        return price

def main():
    input_amt = float(input("How much money are you playing with: $ "))
    input_WTB = int(input("How much are you willing to bet in %: "))
    input_WTB_amount = float(input_amt * (input_WTB/100))
    print("Your Willing to bet amount is $",input_WTB_amount)
    Task_1_solutions.main()
    best_policy = Task_1_Solution.op
    print("There are " + str(len(best_policy)) + " ""state - action"" pairs in the best policy.")
    for k,v in best_policy.items():
        configuration = Configuration(5000)
        hand = OptionsAvailable(input_amt,input_WTB_amount,v[1], 1)
        model = BEModel(configuration)
        hand_BASP = OptionHandPayoutCalculator()
        simulator = MonteCarlo(configuration, model)
        BASP_best_policy = simulator.Simulate(hand, hand_BASP)
        print(k,v[0],BASP_best_policy)

if __name__ == '__main__':
    main()

