def solution(todo_list, finished):
    answer = []
    for i in range(len(finished)):
        if finished[i] == False:
            answer.append(todo_list[i])
        else:
            continue
    return answer