""" Making the Grade """
def round_scores(student_scores):
    """
    :param student_scores: list of student exam scores as float or int.
    :return: list of student scores *rounded* to nearest integer value.
    """

    int_list = []
    taille_tab = len(student_scores)
    for i in range(taille_tab):
        int_list.append(round(student_scores[i]))
    return int_list

def count_failed_students(student_scores):
    """
    :param student_scores: list of integer student scores.
    :return: integer count of student scores at or below 40.
    """

    failed_students = 0
    taille_tab = len(student_scores)
    for i in range(taille_tab):
        if student_scores[i] <= 40:
            failed_students += 1
    return failed_students

def above_threshold(student_scores, threshold):
    """
    :param student_scores: list of integer scores
    :param threshold :  integer
    :return: list of integer scores that are at or above the "best" threshold.
    """

    best_students_list = []
    taille_tab = len(student_scores)
    for i in range(taille_tab):
        if student_scores[i] >= threshold:
            best_students_list.append(student_scores[i])
    return best_students_list


def letter_grades(highest):
    """
    :param highest: integer of highest exam score.
    :return: list of integer lower threshold scores for each D-A letter grade interval.
             For example, where the highest score is 100, and failing is <= 40,
             The result would be [41, 56, 71, 86]:

             41 <= "D" <= 55
             56 <= "C" <= 70
             71 <= "B" <= 85
             86 <= "A" <= 100
    """
    threshold = 41
    return list(range(threshold, highest, round((highest - threshold) / 4)))

def student_ranking(student_scores, student_names):
    """
     :param student_scores: list of scores in descending order.
     :param student_names: list of names in descending order by exam score.
     :return: list of strings in format ["<rank>. <student name>: <score>"].
     """

    tab_size = len(student_scores)
    tab_student_rank = []
    for i in range(tab_size):
        data_of_tab = f"{i+1}. {student_names[i]}: {student_scores[i]}"
        tab_student_rank.append(data_of_tab)
    return tab_student_rank


def perfect_score(student_info):
    """
    :param student_info: list of [<student name>, <score>] lists
    :return: first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """
    tab_size = len(student_info)
    for i in range(tab_size):
        if student_info[i][-1] == 100:
            return student_info[i]
    return []
