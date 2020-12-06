from typing import List


def resolve_data() -> List[str]:
    """
    Chunk out the data file into blocks.
    Filter data to be unique
    :return: the List of strings.
    """
    groups = []
    with open("dataset/day6.txt") as f:
        lines = f.read().splitlines()
        appendable = ''
        for line in lines:
            if line:
                appendable += appendable + line
            else:
                groups.append(''.join(set(appendable)))
                appendable = ''
    return groups


if __name__ == '__main__':
    # ----- Part One -----
    print(sum([len(x) for x in resolve_data()]))
