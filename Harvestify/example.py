def smallest_prime_factor(n):
    if n % 2 == 0:
        return 2
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return i
    return n

def Divisor_Queries(N, Q, a, Queries):
    result = []

    for query in Queries:
        query_type = query[0]
        l = query[1]
        r = query[2]

        if query_type == 1:
            for i in range(l - 1, r):
                smallest_factor = smallest_prime_factor(a[i])
                a[i] //= smallest_factor

        elif query_type == 2:
            result.append(sum(a[l - 1:r]))

        elif query_type == 3:
            i = query[1]
            k = query[2]
            a[i - 1] = k

    return result


N,Q=map(int,input().split())
a=list(map(int,input().split()))
Queries=[list(map(int,input().split())) for _ in range(Q)]
result = Divisor_Queries(N, Q, a, Queries)
for e in result:
    print(e)
