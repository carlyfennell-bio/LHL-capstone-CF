import random, datetime, math

random.seed(datetime.datetime.now())
treatments = ["Allergy_Medications", "Blood_Thinners", "Chemotherapy", "Diuretic", "Radiation_Therapy"]
reward_obtained = [random.random() for i in range(5)]
treatment_count, reward_count, expected_value  = ([0, 0, 0, 0, 0] for i in range(3))

treatment = random.randint(0, 4)
epsilon = 0.1

#Question: Specify the best policy, reward function and expected value function to achieve the objective.
_______________________________________________ # define best_policy here

for i in range(1, 1000):
    if random.random() < epsilon:
        values = list(range(0, 5))
        values.remove(expected_value.index(max(expected_value)))
        treatment = random.choice(values)

    elif max(reward_count) == 0:
        treatment = _________________

    else:
        treatment = expected_value.index(max(expected_value))

    if i % 100 == 0:
        print("Optimal Treatment: %s with probability of success: %f chosen %d times. Average success probability: %.2f" % (treatments[best_policy], reward_obtained[best_policy], treatment_count[best_policy], sum(reward_count)/i))

    if random.random() < reward_obtained[treatment]:
        ____________________
        ____________________
    else:
        ____________________ #instant reward value

    treatment_count[treatment]+=1

    expected_value[treatment] = expected_value[treatment] + (1/treatment_count[treatment])* (instant_reward - expected_value[treatment])

___________________________________________________________________ #define reward_obtained function here
___________________________________________________________________ #define expected_value function here

print("\nNumber of instances when each treatment was administered: \n", treatments," \n", treatment_count)
print("\nProbability of the treatment being successful: \n", reward_obtained,"%")
print("\nExpected return value for each treatment: \n", expected_value)
