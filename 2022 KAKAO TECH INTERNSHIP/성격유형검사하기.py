# LV.1
# String
def solution(survey, choices):
    answer = ''
    dict = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M':0, 'A':0, 'N':0}
    
    for i in range(len(survey)):
        score = choices[i]
        if score == 4:
            continue
        elif score < 4:
            if score == 1:
                dict[survey[i][0]] += 3
            elif score == 2:
                dict[survey[i][0]] += 2
            else:
                dict[survey[i][0]] += 1
        else:
            if score == 5:
                dict[survey[i][1]] += 1
            elif score == 6:
                dict[survey[i][1]] += 2
            else:
                dict[survey[i][1]] += 3
    
    answer += 'R' if dict['R'] >= dict['T'] else 'T'
    answer += 'C' if dict['C'] >= dict['F'] else 'F'
    answer += 'J' if dict['J'] >= dict['M'] else 'M'
    answer += 'A' if dict['A'] >= dict['N'] else 'N'
    
    return answer