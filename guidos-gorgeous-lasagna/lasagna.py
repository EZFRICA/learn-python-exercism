""" Guido's Gorgeous Lasagna """

# define the 'EXPECTED_BAKE_TIME' constant
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time):
    """Calculate the remaining cooking time.

    :param elapsed_bake_time: entire baking time already elapsed.
    :return: int - remaining cooking time derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual lasagna minutes in the four like
    an argument and add how many minutes the lasagna still needs to cook
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time

# define the 'preparation_time_in_minutes()' function
#       and consider using 'PREPARATION_TIME' here

def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time in minutes.

    :param number_of_layers: nombre de couches de la lasagne.
    :return: int - temps de preparation de la lasagne.

    Le nombre de minutes pour la préparation de lasagne
    """
    return number_of_layers * PREPARATION_TIME

# define the 'elapsed_time_in_minutes()' function

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculez le temps de cuisson total écoulé.

    :param number_of_layers: nombre de couches de la lasagne.
    :param elapsed_bake_time: entire baking time already elapsed.
    :return: int - nombre total de minutes de cuisson

    Take the preparation time in minutes and add it to elapsed_bake_time, returning the result
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
