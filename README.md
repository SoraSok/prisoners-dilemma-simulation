# prisoners-dilemma-simulation

## Description
This program simulates the **Prisoner's Dilemma** game with two players.  
Each simulation run consists of **1,000 rounds**, and the user can choose how many runs to perform.  
At the end of all runs, the program calculates the total scores, the most frequent decisions, and other statistics, saving the results into a `Results.txt` file.

---

## Features
- **Multiple runs:** User can define how many simulations (runs) will be performed.
- **Rounds per run:** Each run contains 1,000 rounds where both prisoners decide whether to *cooperate* or *defect*.
- **Payoff matrix:**
  - (C, C): both players get **3 points** each.
  - (D, C): defector gets **5 points**, cooperator gets **0 points**.
  - (D, D): both get **1 point** each.
- **Learning heuristic:**  
  Prisoner 2 adapts its strategy every 10 rounds based on the last 10 moves of Prisoner 1.
- **Statistics included:**  
  - Final score for each prisoner.
  - Most frequent decision (cooperate/defect).
  - Average score per round.
  - Number of (C,C) rounds.
  - Percentage of runs reaching "optimal" results.

---

## How to Run
1. Install **Python 3.x**.
2. Download the file `Prisoners_Dilemma.py`.
3. Run the program:
   ```bash
   python Prisoners_Dilemma.py
4. Enter the number of runs when prompted.
5. After execution, open the Results.txt file to see the results.
