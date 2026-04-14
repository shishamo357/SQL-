def solution(alice, bob):
    # TODO: Implement me!       gu-0  tyoki 1   pa- 2


    # まず引き分け
 if alice == bob:
    return "DRAW"

    #勝ちパターン
 if alice == 0: #具
    if bob == 1:
        return "WIN"
    else:
        return "LOSE"

 if alice == 1: #チョキ
    if bob == 2:
        return "WIN"
    else:
        return "LOSE"

 if alice == 2: #パ
 
    if bob == 0:
        return "WIN"
    else:
        return "LOSE"       
    #その他