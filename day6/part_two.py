from typing import List


def data() -> List[List[str]]:
    """
    Chunk out the data set into a list of lists, where each list is a collection of 'people'
    :return: the List of strings.
    """
    groups = []
    with open("dataset/day6.txt") as f:
        lines = f.read().splitlines()
        this_group = []
        for line in lines:
            if line:
                this_group.append(line)
            else:
                groups.append(this_group)
                this_group = []
    return groups


if __name__ == '__main__':
    # ----- Part Two -----
    # for every possible character, check if such character exists in every collection of 'people'
    print(len([char for char in 'abcdefghijklmnopqrstuvwxyz' for g in data() if all([char in x for x in g])]))


