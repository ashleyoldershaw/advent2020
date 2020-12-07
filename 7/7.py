def create_graph(raw_lines):
    rules = {}

    # clean out references to bags, and use dict comprehension to generate a nice graph
    for line in raw_lines:
        line = line.replace("bags", "")
        line = line.replace("bag", "")
        line = line.replace(".", "")
        entry = line.split("contain")
        bag = entry[0].strip()
        contents = {x.strip()[2:]: int(x.strip()[0]) for x in entry[1].split(",") if x.strip() != "no other"}
        rules[bag] = contents

    return rules


def find_bags_in_bag(graph, start, goal):
    # finds shortest path between 2 nodes of a graph using BFS
    # this was lifted from stack overflow and modified by me
    # it was designed for lists of lists but funnily python lets this work with dicts as well
    # keep track of explored nodes
    explored = []
    # keep track of all the paths to be checked
    queue = [[start]]

    # the gold bag won't contain itself so return false
    if start == goal:
        return False

    # keeps looping until all possible paths have been checked
    while queue:
        # pop the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        if node not in explored:
            neighbours = graph[node]
            # go through all neighbour nodes, construct a new path and
            # push it into the queue
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                # return path without gold bag if we reacj the gold bag
                if neighbour == goal:
                    return new_path[:-1]

            # mark node as explored
            explored.append(node)

    # in case there's no path between the 2 nodes
    return False


def find_bags_with_gold_bag_in(graph):
    output = set()
    # look in the graph for all the bags in the bag, check it's not already in the output set so we don't have to do bfs
    for bag in graph:
        if bag not in output:
            if path := find_bags_in_bag(graph, bag, "shiny gold"):
                output = output | set(path)

    return output


def count_bags_in_bag(graph, start):
    # here's a great chance to do some recursion!
    total = 0
    if start not in totals_graph:
        for bag in graph[start]:
            total += graph[start][bag] * count_bags_in_bag(graph, bag)
        if total:
            totals_graph[start] = total
            # don't forget to include the bag we're looking in!
            return total + 1
    else:
        # don't forget to include the bag we're looking in!
        return totals_graph[start] + 1

    return 1


if __name__ == '__main__':
    with open("rules.txt", "r") as f:
        raw_rules = f.read().splitlines()

    # create a graph containing the bags in each bag, with counts
    bag_graph = create_graph(raw_rules)

    bags_with_gold_bag_in = find_bags_with_gold_bag_in(bag_graph)

    print(f"Total number of bags that contain a gold bag in are {len(bags_with_gold_bag_in)}")

    # evil scoping on this variable - sorry!
    totals_graph = {}

    total_bags = count_bags_in_bag(bag_graph, "shiny gold")
    # we aren't supposed to count the shiny gold bag, so take off 1
    print(f"Total bags inside a gold bag is {total_bags - 1}")
