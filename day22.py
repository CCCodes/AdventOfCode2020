import copy


inp_f = open("input/day22.txt", "r")
inp = inp_f.read()
player1_orig = [int(line) for line in inp.split("\n\n")[0].split("\n")[1:] if line != ""]
player2_orig = [int(line) for line in inp.split("\n\n")[1].split("\n")[1:] if line != ""]


def part1():
    player1 = player1_orig.copy()
    player2 = player2_orig.copy()
    while len(player1) > 0 and len(player2) > 0:
        if player1[0] > player2[0]:
            player1.append(player1[0])
            player1.append(player2[0])
        else:  # player2[0] > player1[0]:
            player2.append(player2[0])
            player2.append(player1[0])
        del player1[0]
        del player2[0]
    winner = player1 if len(player1) > 0 else player2
    winner.reverse()
    score = 0
    for points, card in enumerate(winner):
        score += (points + 1) * card
    return score


def check_visited(visited, players):
    for v in visited:
        if v[0] == players[0] and v[1] == players[1]:
            return True
    return False


def recurse(players):
    visited = []
    while len(players[0]) > 0 and len(players[1]) > 0:
        if check_visited(visited, players):
            return 0, players[0]
        visited.append([players[0].copy(), players[1].copy()])
        draw = [players[0].pop(0), players[1].pop(0)]
        if draw[0] > len(players[0]) or draw[1] > len(players[1]):
            if draw[0] > draw[1]:
                round_winner = 0
            else:
                round_winner = 1
        else:
            players_copy = [players[0].copy()[:draw[0]], players[1].copy()[:draw[1]]]
            round_winner, _ = recurse(players_copy)
        players[round_winner].append(draw[round_winner])
        players[round_winner].append(draw[1-round_winner])
    winner = 0 if len(players[0]) > 0 else 1
    return winner, players[winner]


def part2():
    _, winner = recurse([player1_orig.copy(), player2_orig.copy()])
    winner.reverse()
    score = 0
    for points, card in enumerate(winner):
        score += (points + 1) * card
    return score


if __name__ == "__main__":
    print(part1())
    print(part2())
