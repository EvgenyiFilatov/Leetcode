"""Хард задачка."""


def run(s):
    """Решение которое не проходит по времени."""
    def IsValid(item):
        delta = 0
        for ch in item:
            if ch == '(':
                delta += 1
            else:
                delta -= 1

            if delta < 0:
                return False
        return delta == 0

    def GetItems():
        N = len(s)
        items = []
        for i in range(N):
            tmp = []
            for j in range(i, N):
                tmp.append(s[j])
                items.append("".join(tmp))
        return items

    def FilterValidItemsOnly(items):
        ans = []
        for item in items:
            if IsValid(item):
                ans.append(item)
        return ans

    def GetTheLongetsItem(items):
        ans = "" if not items else items[0]
        for item in items:
            if len(item) > len(ans):
                ans = item
        return ans

    items = GetItems()
    valid_items = FilterValidItemsOnly(items)
    longest_item = GetTheLongetsItem(valid_items)
    return len(longest_item)


def run2(s):
    """Решение подглядел, не проходит по памяти."""
    N = len(s)
    INF = 10**10

    @cache
    def run(idx, delta, taken):
        if idx == N and delta != 0:
            return -INF
        if idx == N and delta == 0:
            return 0
        if delta < 0:
            return -INF
        if s[idx] == '(' and not taken:
            return max(run(idx + 1, delta, 0), 1 + run(idx + 1, delta + 1, 1))
        if s[idx] == ')' and not taken:
            return max(run(idx + 1, delta, 0), 1 + run(idx + 1, delta - 1, 1))
        if s[idx] == '(' and delta == 0:
            return max(0, 1 + run(idx + 1, delta + 1, 1))
        if s[idx] == ')' and delta == 0:
            return max(0, 1 + run(idx + 1, delta - 1, 1))
        if s[idx] == '(':
            return 1 + run(idx + 1, delta + 1, 1)
        return 1 + run(idx + 1, delta - 1, 1)

    return run(0, 0, 0)
