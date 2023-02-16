def solution(phone_book):
    phone_book.sort()
    b = []
    
    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            b.append('false')
            break
        else:
            b.append('true')
            
    if 'false' in b:
        answer = False
    else:
        answer = True
    return answer