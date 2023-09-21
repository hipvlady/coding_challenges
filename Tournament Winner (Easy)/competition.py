def tournamentwinner(competitions, results):
    tournament_results = {}

    for competition, result in zip(competitions, results):
        winning_team = competition[0] if result == 1 else competition[1]

        if winning_team not in tournament_results:
            tournament_results[winning_team] = 3
        else:
            tournament_results[winning_team] += 3

    return max(tournament_results, key=tournament_results.get)


competitions = [["HTML", "C#"], ["C#", "Python"], ["Python", "HTML"]]
results = [0, 0, 1]
d = tournamentwinner(competitions, results)
print(d)
