from collections import deque


def find_word(wordLst, word):
    result = []
    for example in wordLst:
        count = 0
        for k in range(len(example)):
            if example[k] != word[k]:
                count += 1
        if count == 1:
            result.append(example)
    return result

# 큐에다가 단어랑 몇 단계인지 숫자 같이 넣어서 확인하면 될 듯


def solution(begin, target, words):
    answer = 50
    queue = deque()
    queue.append([begin, 0])
    visited = set()

    while queue:
        w, count = queue.popleft()
        visited.add(w)
        if w == target:
            answer = count
            break
        lst = find_word(words, w)
        for word in lst:
            if word not in visited:
                visited.add(word)
                queue.append([word, count + 1])
    if answer == 50:
        return 0
    else:
        return answer
