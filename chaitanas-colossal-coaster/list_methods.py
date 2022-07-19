""" Chaitana's Colossal Coaster """

def add_me_to_the_queue(express_queue, normal_queue, ticket_type, person_name):
    """

    :param express_queue: list - names in the Fast-track queue.
    :param normal_queue:  list - names in the normal queue.
    :param ticket_type:  int - type of ticket. 1 = express, 0 = normal.
    :param person_name: str - name of person to add to a queue.
    :return: list - the (updated) queue the name was added to.
    """
    if ticket_type == 1 :
        express_queue.append(person_name)
        return express_queue
    normal_queue.append(person_name)
    return normal_queue


def find_my_friend(queue, friend_name):
    """

    :param queue: list - names in the queue.
    :param friend_name: str - name of friend to find.
    :return: int - index at which the friends name was found.
    """
    return queue.index(friend_name)


def add_me_with_my_friends(queue, index, person_name):
    """

    :param queue: list - names in the queue.
    :param index: int - the index at which to add the new name.
    :param person_name: str - the name to add.
    :return: list - queue updated with new name.
    """

    # new_list = []
    # taille = len(queue)
    # for i in range(index + 1):
    #     if i == index :
    #         new_list.append(person_name)
    #         break
    #     new_list.append(queue[i])

    # for j in range(taille - index):
    #     new_list.append(queue[index+j])
    # return new_list

    queue.insert(index, person_name)
    return queue

def remove_the_mean_person(queue, person_name):
    """

    :param queue: list - names in the queue.
    :param person_name: str - name of mean person.
    :return:  list - queue update with the mean persons name removed.
    """
    # new_list = []
    # taille = len(queue)
    # for i in range(taille):
    #     if i == queue.index(person_name) :
    #         continue
    #     new_list.append(queue[i])
    # return new_list

    queue.remove(person_name)
    return queue

def how_many_namefellows(queue, person_name):
    """

    :param queue: list - names in the queue.
    :param person_name: str - name you wish to count or track.
    :return:  int - the number of times the name appears in the queue.
    """
    namefellows = queue.count(person_name)
    return namefellows

def remove_the_last_person(queue):
    """

    :param queue: list - names in the queue.
    :return: str - name that has been removed from the end of the queue.
    """
    last_person = queue[-1]
    queue.remove(last_person)
    return last_person

def sorted_names(queue):
    """

    :param queue: list - names in the queue.
    :return: list - copy of the queue in alphabetical order.
    """
    sorted_list = sorted(queue)
    return sorted_list
