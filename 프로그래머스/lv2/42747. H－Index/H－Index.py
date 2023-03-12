def solution(citations):
    citations.sort(reverse=True)
    for i, j in enumerate(citations):
        if i >= j:
            return i
    return len(citations)