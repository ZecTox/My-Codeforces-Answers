import sys
input = sys.stdin.readline

questions, time = map(int, input().split())

time_left = 240 - time
solved_questions = 0

for i in range(1, questions + 1):
    time_required = 5 * i
    if time_left >= time_required:
        time_left -= time_required
        solved_questions += 1
    else:
        break

print(solved_questions)
