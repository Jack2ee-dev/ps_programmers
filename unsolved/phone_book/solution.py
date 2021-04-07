def solution(phone_book):
    phone_book = sorted(phone_book, key=len)

    if len(phone_book) <= 1:
        return True

    idx = 0
    compared = 1
    while compared < len(phone_book):
        min_len_number = phone_book[idx]
        min_len = len(min_len_number)
        dic = dict({min_len_number: True})
        for i in range(compared, len(phone_book)):
            split = phone_book[i][:min_len]
            if split in dic:
                return False
            else:
                dic[split] = True
        idx += 1
        compared += 1

    return True


if __name__ == "__main__":
    print(solution(["119", "97674223", "1195524421"]))
    print(solution(["123", "456", "789"]))
    print(solution(["12", "123", "1235", "567", "88"]))
    print(solution(["112", "44", "4544"]))
