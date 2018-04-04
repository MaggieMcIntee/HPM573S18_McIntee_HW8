import Parameters as P
import HW8 as Cls
import SupportSteadyState as Support

# create a cohort of fair games with the unweighted coin
cohortFairGame = Cls.SetOfGames(
    id=1,
    n_games=P.SIM_POP_SIZE,
    prob_head=P.prob_head)

# simulate the cohort
FairOutcome = cohortFairGame.simulation()

# create a cohort of games with the unfair, weighted coin
cohortWithUnfairCoin = Cls.SetOfGames(
    id=2,
    n_games=P.SIM_POP_SIZE,
    prob_head=P.prob_head2)

# simulate the cohort
withUnfiarCoinOutcome = cohortWithUnfairCoin.simulation()

print("Question 1")

# print outcomes of each cohort
Support.print_outcomes(FairOutcome, 'When coin is fair:')
Support.print_outcomes(withUnfiarCoinOutcome, 'When coin is unfair and weighted:')

# print comparative outcomes
Support.print_comparative_outcomes(FairOutcome, withUnfiarCoinOutcome)