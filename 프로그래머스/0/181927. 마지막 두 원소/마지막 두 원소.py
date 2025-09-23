def solution(num):
    num.append(num[-1]-num[-2] if num[-2] < num[-1] else num[-1]*2)
    return num