
def score_fnc(gold, prediction):
    """Return the score of a prediction with FNC rules.

    :param gold: the gold reponse
    :type path: str
    :param prediction: the prediction reponse
    :type path: str
    :return: score between 1 and 0
    :rtype: float
    """
    RELATED = set(["agree", "disagree", "discuss"])
    score = 0
    if gold == prediction:
        score += 0.25
        if gold != 'unrelated':
            score += 0.50
    if gold in RELATED and prediction in RELATED:
        score += 0.25
    return score
