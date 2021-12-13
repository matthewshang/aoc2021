from collections import defaultdict

edges = [line.split('-') for line in open('day12.txt').read().splitlines()]
adj = defaultdict(list)
for u, v in edges:
    adj[u].append(v)
    adj[v].append(u)
paths = set()


def dfs1(cur: str, path: list[str]):
    for next in adj[cur]:
        if next == 'start':
            continue
        elif next == 'end':
            paths.add(','.join(path + [next]))
        elif next[0].isupper():
            dfs1(next, path + [next])
        elif next not in path:
            dfs1(next, path + [next])


def dfs2(cur: str, path: list[str], used: bool):
    for next in adj[cur]:
        if next == 'start':
            continue
        elif next == 'end':
            paths.add(','.join(path + [next]))
        elif next[0].isupper():
            dfs2(next, path + [next], used)
        else:
            count = path.count(next)
            if count == 0:
                dfs2(next, path + [next], used)
            elif count == 1 and not used:
                dfs2(next, path + [next], True)


dfs1('start', ['start'])
print(f'Part 1: {len(paths)}')

paths.clear()
dfs2('start', ['start'], False)
print(f'Part 2: {len(paths)}')
