import random

print("Hello! This is the Prisoner’s Dilemma program.")
print("How many runs you want? ", end="")
runs = int(input())
decisions = ["cooperate", "defect"]

# Global counters for all runs
total_scorePr1, total_scorePr2, total_contcoop, total_contdef, total_cc_count = 0, 0, 0, 0, 0 #contcoop - count of cooperate decisions, contdef - count of defect decisions, cc_count - count of (C,C) decisions
total_rounds, optimal_maxsum_runs, optimal_cc25_runs = 0, 0, 0 #optimal_maxsum_runs - runs where the sum of scores is optimal, optimal_cc25_runs - runs where (C,C) decisions are at least 25%

file = open("Results.txt", "w", encoding="utf-8")  # Open file for writing results

for run in range(1, runs + 1): # Loop through each run
    history = [] # Initialize history for decisions
    strategy = random.choice(decisions)
    scorePr1, scorePr2, contcoop, contdef, cc_count = 0, 0, 0, 0, 0
    total = 0

    for rcount in range(1000): # Loop through 1000 rounds
        pr1 = random.choice(decisions)
        if rcount < 10:
            pr2 = random.choice(decisions)
        else:
            pr2 = strategy

        history.append(pr1) # Append decision to history

        if (rcount + 1) % 10 == 0: # Every 10 rounds, update strategy
            if history[-10:].count("cooperate") > history[-10:].count("defect"):
                strategy = "cooperate"
            elif history[-10:].count("defect") > history[-10:].count("cooperate"):
                strategy = "defect"
            else:
                strategy = random.choice(decisions)
        # Decision logic based on the prisoners' choices
        if pr1 == "cooperate" and pr2 == "cooperate": 
            scorePr1 += 3
            scorePr2 += 3
            contcoop += 2
            cc_count += 1
        elif pr1 == "defect" and pr2 == "defect":
            scorePr1 += 1
            scorePr2 += 1
            contdef += 2
        elif pr1 == "defect" and pr2 == "cooperate":
            scorePr1 += 5
            contdef += 1
            contcoop += 1
        else:
            scorePr2 += 5
            contdef += 1
            contcoop += 1
       
        total += 1

    if scorePr1 + scorePr2 >= 0.75 * 6 * 1000:
        optimal_maxsum_runs += 1 # Check if the sum of scores is optimal
    if cc_count >= 250:  # 25% of (C,C) decisions
        optimal_cc25_runs += 1 # Check if (cooperate, cooperate) decisions are optimal

    # Write the result of the run
    file.write(f"*** Run {run} ***\n")
    file.write(f"Score for prisoner 1: {scorePr1}\n")
    file.write(f"Score for prisoner 2: {scorePr2}\n")
    file.write(f"Rounds in total: {total}\n")
    file.write("Most frequent decision: ")
    if contcoop > contdef:
        file.write("cooperate\n")
    elif contdef > contcoop:
        file.write("defect\n")
    else:
        file.write("equal\n")
    avg = (scorePr1 + scorePr2) / total
    file.write(f"Average score per round: {avg:.2f}\n")
    if scorePr1 > scorePr2:
        file.write("Prisoner 1 is the winner\n")
    elif scorePr1 < scorePr2:
        file.write("Prisoner 2 is the winner\n")
    else:
        file.write("Oh wow... It's a draw\n")
    file.write("\n")

    # Update global counters
    total_scorePr1 += scorePr1
    total_scorePr2 += scorePr2
    total_contcoop += contcoop
    total_contdef += contdef
    total_rounds += total
    total_cc_count += cc_count

# Summary
file.write("*** Summary over all runs ***\n")
file.write(f"Total score for prisoner 1: {total_scorePr1}\n")
file.write(f"Total score for prisoner 2: {total_scorePr2}\n")
file.write(f"Total rounds: {total_rounds}\n")
file.write("Most frequent decision: ")
if total_contcoop > total_contdef:
    file.write("cooperate\n")
elif total_contdef > total_contcoop:
    file.write("defect\n")
else:
    file.write("equal\n")
avg_total = (total_scorePr1 + total_scorePr2) / total_rounds
file.write(f"Average score per round: {avg_total:.2f}\n") # Calculate average score per round
file.write(f"(C,C) total: {total_cc_count} ({total_cc_count / total_rounds:.1%})\n") # Calculate (C,C) decisions percentage
file.write(f"Optimal (max sum = 0.75 * 6 * 1000) runs: {optimal_maxsum_runs}/{runs} "
           f"({optimal_maxsum_runs / runs:.1%})\n") # Calculate optimal runs based on max sum
file.write(f"Optimal (>=25% (C,C)) runs: {optimal_cc25_runs}/{runs} " 
           f"({optimal_cc25_runs / runs:.1%})\n") # Calculate optimal runs based on (C,C) decisions
file.write("\n")
if total_scorePr1 > total_scorePr2:
    file.write("Prisoner 1 is the winner 🎉")
elif total_scorePr1 < total_scorePr2:
    file.write("Prisoner 2 is the winner 🎉")
else:
    file.write("Oh wow... It's a draw")

file.close()
print("See your .txt file!")