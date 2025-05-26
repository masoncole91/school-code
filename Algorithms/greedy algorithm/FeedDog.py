def feedDog(hunger_level, biscuit_size):
    """
    return:
    - dogs with hunger needs met (first list) from biscuit sizes (second list);
    - if none fed, 0;
    don't feed same dogs twice or reuse biscuits;
    use a greedy algorithm;
    code repurposed from:
    Exploration 5.3: Greedy Algorithms - Activity Selection Problem
    """
    result = []

    # sort lists by descending order so dogs don't get non-optimally large biscuits
    hunger_level, biscuit_size = sorted(hunger_level)[::-1], sorted(biscuit_size)[::-1]
    for indice in range(len(hunger_level)):

        # find smallest possible biscuit size for dog
        size = 0
        while size < len(biscuit_size):

            # select locally optimal choice
            if biscuit_size[size] >= hunger_level[indice]:
                result.append(hunger_level[indice])
                biscuit_size.remove(biscuit_size[size])
                break
            size += 1

    return len(result)
