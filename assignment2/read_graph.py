import sys

if __name__ == '__main__':
    v, e, n = map(int, sys.stdin.readline().split())
    vertices = sys.stdin.readline().split()
    graph = {x: [] for x in vertices}
    for _ in range(e):
        inp = sys.stdin.readline().split()
        graph[inp[0]].append((inp[1], inp[2]))
    #print(graph)
    # for x in graph.keys():
    #     print(x, graph[x])

    for _ in range(n):
        cmd = sys.stdin.readline().split()
        if cmd[0] == "1":
            edge_weight = None
            for x in graph[cmd[1]]:
                if x[0] == cmd[2]:
                    edge_weight = x[1]
                    break
            print("FALSE" if edge_weight is None else edge_weight)

        else:
            if len(graph[cmd[1]]) == 0:
                print("NONE")
            else:
                graph[cmd[1]].sort(key=lambda x: vertices.index(x[0]))
                sys.stdout.writelines(" ".join(x[1] for x in graph[cmd[1]]) + "\n")

