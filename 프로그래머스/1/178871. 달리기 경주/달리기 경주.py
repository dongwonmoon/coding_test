def solution(players, callings):
    players_dict = {player: idx for idx, player in enumerate(players)}
    
    for calling in callings:
        i = players_dict[calling]
        
        players[i], players[i-1] = players[i-1], players[i]
        
        players_dict[players[i]] = i
        players_dict[players[i-1]] = i - 1
        
    return players