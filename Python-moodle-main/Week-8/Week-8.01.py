def find_winner():
    import sys
    input = sys.stdin.read
   
    data = input().split()
   
    n = int(data[0])
    votes = data[1:]
   
    vote_count = {}
   
    for vote in votes:
        if vote in vote_count:
            vote_count[vote] += 1
        else:
            vote_count[vote] = 1
   
    # Find the candidate with the maximum votes
    max_votes = 0
    winner = ""
   
    for candidate, count in vote_count.items():
        if count > max_votes or (count == max_votes and candidate < winner):
            max_votes = count
            winner = candidate
           
    print(winner)

if __name__ == "__main__":
    find_winner()
