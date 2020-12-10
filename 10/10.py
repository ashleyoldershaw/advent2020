def get_joltage_differences(input_joltages):
    input_joltages.sort()

    differences = {0: 0, 1: 0, 2: 0, 3: 0}

    if input_joltages[0] <= 3:
        differences[input_joltages[0]] += 1

    for i in range(1, len(input_joltages)):
        if 0 <= (diff := input_joltages[i] - input_joltages[i - 1]) <= 3:
            differences[diff] += 1
        else:
            print("Streak ended without using all adapters!")
            break

    differences[3] += 1

    return differences[1] * differences[3]


def find_number_of_combinations(input_joltages):
    # create a graph of paths from 0 to the maximum, and count the number of paths through the graph
    input_joltages.append(0)
    input_joltages.append(max(input_joltages) + 3)
    input_joltages.sort()

    # the graph has all the links from it to other nodes, and stores how many paths it has to get to that node
    graph = {i: {"links": [j for j in input_joltages if 0 < j - i <= 3], "paths": 0} for i in input_joltages}

    # add initial path, we add this to each link to graph[0] and add that to each link
    # when we reach a place where 2 paths can reach there then paths is added to twice
    # and so on until we get to the last node
    # this is similar to Dijkstra's algorithm except we're just counting the no. of paths rather than the shortest path
    graph[0]["paths"] = 1
    for node in sorted(graph.keys()):
        for link in graph[node]["links"]:
            graph[link]["paths"] += graph[node]["paths"]

    return graph[input_joltages[-1]]["paths"]


if __name__ == '__main__':
    with open("adapters.txt", "r") as f:
        joltages = [int(x) for x in f.read().splitlines()]

    output = get_joltage_differences(joltages)
    print(f"Output for part 1 is {output}")

    output = find_number_of_combinations(joltages)
    print(f"Number of possible combinations is {output}")
