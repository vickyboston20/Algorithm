# Stable Matching Algorithm

# Interviewers = {
#     'X':    ['java', 'Shell', 'angular', 'html', 'css', 'javascript'],
#     'y':    ['aws', 'jenkins', 'chef', 'docker', 'terraform'],
#     'z':    ['python', 'django']
# }
#
# Candidates = {
#     'A':    ['java', 'angular', 'html', 'css', 'javascript'],
#     'B':    ['python', 'django', 'flask', 'scrapy', 'pyqt'],
#     'C':    ['terraform', 'jenkins', 'aws', 'chef']
# }

Interviewers = {
    'X':    ['B', 'A', 'C'],
    'Y':    ['B', 'C', 'A'],
    'Z':    ['A', 'C', 'B']
}

Candidates = {
    'A':    ['X', 'Y', 'Z'],
    'B':    ['X', 'Z', 'Y'],
    'C':    ['Z', 'Y', 'X']
}

tentative_matching = []


# Candidates who need to be interviewed
free_candidates = []


def init_free_candidates():
    for candidate in Candidates.keys():
        free_candidates.append(candidate)


def begin_matching(candidate):
    print(f"Dealing with {candidate}")
    for interviewer in Candidates[candidate]:

        not_available = [match for match in tentative_matching if interviewer in match]

        if len(not_available) == 0:
            tentative_matching.append([candidate, interviewer])
            free_candidates.remove(candidate)
            print(f"{candidate} is no longer is free and interviewed schedule with {interviewer}")
            break
        elif len(not_available) > 0:
            print(f"{interviewer} is not available.")
            current_candidate = Interviewers[interviewer].index(not_available[0][0])
            potential_candidate = Interviewers[interviewer].index(candidate)

            if current_candidate < potential_candidate:
                print(f"Interviwer is ok with {not_available[0][0]}")
            else:
                print(f"{candidate} is better than {not_available[0][0]}")
                print(f"Making {not_available[0][0]} free again and tentatively engaging {candidate} and {interviewer}")
                free_candidates.remove(candidate)
                free_candidates.append(not_available[0][0])
                not_available[0][0] = candidate
                break


def stable_matching():
    while len(free_candidates) > 0:
        for candidate in free_candidates:
            begin_matching(candidate)


def main():
    print("Scheduling Interview for candidate")
    init_free_candidates()
    stable_matching()
    print(tentative_matching)


if __name__ == '__main__':
    main()
