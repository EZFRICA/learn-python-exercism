""" Card Games """
def get_rounds(number):
    """

     :param number: int - current round number.
     :return: list - current round and the two that follow.
    """
    rounds = []
    for _ in range(3):
        rounds.append(number)
        number += 1
    return rounds

def concatenate_rounds(rounds_1, rounds_2):
    """

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """
    rounds_1.extend(rounds_2)
    return rounds_1

def list_contains_round(rounds, number):
    """

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return:  bool - was the round played?
    """
    return number in rounds

def card_average(hand):
    """

    :param hand: list - cards in hand.
    :return:  float - average value of the cards in the hand.
    """
    nbre_card = len(hand)
    som = 0
    for i in range(nbre_card):
        som += hand[i]
    return som / nbre_card

def approx_average_is_average(hand):
    """

    :param hand: list - cards in hand.
    :return: bool - if approximate average equals to the `true average`.
    """
    return (card_average(hand) == hand[(len(hand)) // 2]) or (card_average(hand) == (hand[0] + hand[-1]) / 2)

def average_even_is_average_odd(hand):
    """

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """

    nbre_card = len(hand)
    sum_even = 0
    pair = 0
    impait = 0
    sum_odd = 0
    for i in range(nbre_card):
        if i % 2 == 0:
            sum_even += hand[i]
            pair += 1
        else:
            sum_odd += hand[i]
            impait += 1
    return (sum_even / pair) == (sum_odd / impait)


def maybe_double_last(hand):
    """

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """
    if hand[-1] == 11:
        hand[-1] = 22
    return hand
