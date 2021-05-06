def solution(new_id):
    # new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
    def check_1(new: str):
        return new.lower()

    # new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
    def check_2(new: str):
        new_str: str = ''
        for c in new:
            if (('a' <= c and c <= 'z') or
               ('1' <= c and c <= '9') or
               ('-' == c) or ('_' == c) or
               ('.' == c)):
                new_str += c
        return new_str

    # new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
    def check_3(new: str):
        new_str: str = str('')
        if len(new) == 0:
            return new_str
        for c in new:
            if new_str == '':
                new_str += c
            else:
                if c == '.' and new_str[-1] == '.':
                    continue
                else:
                    new_str += c
        return new_str

    # new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
    def check_4(new: str):
        new_str: str = str('')
        if len(new) == 0:
            return new_str
        elif len(new) == 1:
            if new[0] == '.':
                return ''
            else:
                return new
        else:
            if new[0] == '.' and new[-1] == '.':
                new_str = new[1:-1]
            elif new[0] == '.':
                new_str = new[1:]
            elif new[-1] == '.':
                new_str = new[:-1]
            else:
                new_str = new
            return new_str

    # new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
    def check_5(new: str):
        if len(new) == 0:
            return str('a')
        else:
            return new

    # new_id
    def check_6(new: str):
        new_str:str = ''
        if len(new) >= 16:
            new_str = new[:15]
        else:
            new_str = new
        if len(new_str) >= 2 and new_str[-1] == '.':
            new_str = new_str[:-1]
        elif len(new_str) == 1 and new_str[0] == '.':
            return ''
        return new_str

    def check_7(new: str):
        new_str:str = new
        if len(new_str) <= 2:
            while len(new_str) <= 2:
                new_str += new[-1]
        return new_str
    new_id = check_1(new_id)
    print("after1: " + new_id)
    new_id = check_2(new_id)
    print("after2: " + new_id)
    new_id = check_3(new_id)
    print("after3: " + new_id)
    new_id = check_4(new_id)
    print("after4: " + new_id)
    new_id = check_5(new_id)
    print("after5: " + new_id)
    new_id = check_6(new_id)
    print("after6: " + new_id)
    new_id = check_7(new_id)
    print("after7: " + new_id)
    return new_id


#solution("...!@BaT#*..y.abcdefghijklm")
#solution("z-+.^.")
#solution("=.=")
solution("123_.def")
#solution("")