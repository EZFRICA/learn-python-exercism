""" High Scores """
def latest(scores):
    return scores[-1]


def personal_best(scores):
    scores.sort()
    return scores[-1]


def personal_top_three(scores):
    new_scores = sorted(scores, reverse=True)
    return new_scores[:3]
