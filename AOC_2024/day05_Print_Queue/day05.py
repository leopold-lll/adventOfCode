import re
from pprint import pprint


def read_input(file_name="sample.txt"):
    with open(file_name, 'r') as file:
        lines = file.readlines()

    # Initialize an empty dictionary
    page_after = {}
    # Initialize a list to store lists of numbers after an empty line
    ll = []

    # Flag to check if we are in the second input type
    first_input = True

    # Process each line in the file
    for line in lines:
        line = line.strip()  # Remove whitespace

        # Check for an empty line
        if not line:
            first_input = False
            continue

        if first_input:
            # Split the line into two parts based on the '|' delimiter
            v1, v2 = map(int, line.split('|'))

            # If v1 is not in the dict, initialize an empty set
            if v1 not in page_after:
                page_after[v1] = set()
            # Add the v2 to the set corresponding to the key
            page_after[v1].add(v2)
        else:
            # Split the line into numbers based on the ',' delimiter
            numbers = list(map(int, line.split(',')))
            ll.append(numbers)

    # Print the resulting dict and list of lists
    # pprint(page_after)
    return (page_after, ll)


def fix_sequence(orig_after, seq):
    # print("Filter requires to the seq only")
    # print("seq", seq)
    page_after = {}
    for el in seq:
        if el in orig_after:
            page_after[el] = set(seq) & orig_after[el]
        else:
            page_after[el] = set()
    # pprint(page_after)

    # Perform topological sorting
    result = topological_sort(page_after)
    print("Topological Order:   ", result)
    return (result[len(result)//2])


def topological_sort(graph):
    result = []
    while graph:
        # Find all keys with an empty set as value
        empty_keys = [k for k, v in graph.items() if not v]

        if not empty_keys:
            raise ValueError(
                "The graph contains a cycle and cannot be sorted topologically.")

        # Add these keys to the result and remove them from the graph
        result.extend(empty_keys)

        for key in empty_keys:
            del graph[key]

        # Remove the keys from the remaining sets in the graph
        for value_set in graph.values():
            value_set.difference_update(empty_keys)

    return result


def main(page_after, sequences):
    sum1, sum2 = 0, 0
    for seq in sequences:
        broken_rule = False
        # print("\nChecking sequence:", l)
        for i in range(len(seq)):
            # check that numbers who come first cannot be in the "after dependency" (symmetry guarantee no problems)
            if seq[i] in page_after:
                # print("Check:", set(seq[:i]), page_after[seq[i]])
                overlap = set(seq[:i]) & page_after[seq[i]]
                if overlap:
                    print("\nThe rules has been broken, due to:", overlap)
                    broken_rule = True
                    break

        if broken_rule:
            sum2 += fix_sequence(page_after, seq)
        else:
            middle = seq[len(seq)//2]
            sum1 += middle
            print("Found valid sequence:", seq, ", middle value:", middle)

    print("Part1: The sum of middle values of original valid sequences is:  ", sum1)
    print("Part2: The sum of middle values of sequences after correction is:", sum2)


if __name__ == "__main__":
    page_after, sequences = read_input("input.txt")
    main(page_after, sequences)
    # Part1: The sum of middle values of original valid sequences is:   4637
    # Part2: The sum of middle values of sequences after correction is: 6370

    # Topological sorting example:
    # graph = {29: set(), 47: {53, 61, 29}, 53: {29},
    #          61: {53, 29}, 75: {61, 53, 29, 47}}
    # result = topological_sort(graph)
    # print("Topological Order:", result)
