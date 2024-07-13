import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    rows = players.shape[0]
    colums = players.shape[1]
    sizePlayers = [rows, colums]
    return sizePlayers