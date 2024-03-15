def one_two_three(n):
    return [int(o or 0) for o in (f"{'9'*(n // 9)}{n % 9 or ''}", "1" * n)]