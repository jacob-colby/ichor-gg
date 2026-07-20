"""Validation harness: how well do our suggested builds and item scores agree
with SmiteBrain's community win rates? Writes Analysis/_validation.md and a
tag-audit report. Agreement is a proxy (win rate is popularity-biased,
Conquest-only) — a falsifiable dashboard, not ground truth."""
import math

from smite import recommend, scoring, efficiency, assemble


def coverage(core, community_names):
    ci = set(community_names)
    if not ci:
        return 0.0
    return len(set(core) & ci) / len(ci)


def win_weighted_coverage(core, community):
    total = sum(c["win_rate"] for c in community if c.get("win_rate") is not None)
    if not total:
        return 0.0
    inc = sum(c["win_rate"] for c in community
              if c.get("win_rate") is not None and c["name"] in set(core))
    return inc / total


def spearman(xs, ys):
    n = len(xs)
    if n < 2:
        return None

    def ranks(v):
        order = sorted(range(n), key=lambda i: v[i])
        r = [0.0] * n
        i = 0
        while i < n:
            j = i
            while j + 1 < n and v[order[j + 1]] == v[order[i]]:
                j += 1
            avg = (i + j) / 2.0
            for k in range(i, j + 1):
                r[order[k]] = avg
            i = j + 1
        return r

    rx, ry = ranks(xs), ranks(ys)
    mx, my = sum(rx) / n, sum(ry) / n
    cov = sum((rx[i] - mx) * (ry[i] - my) for i in range(n))
    denom = math.sqrt(
        sum((rx[i] - mx) ** 2 for i in range(n)) * sum((ry[i] - my) ** 2 for i in range(n))
    )
    return cov / denom if denom else None
