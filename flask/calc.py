
target_score_state = 67.76

score_equivalent_cbse = 75.67
score_equivalent_icse = 70.41

scaling_factor_cbse = target_score_state / score_equivalent_cbse
scaling_factor_icse = target_score_state / score_equivalent_icse

def adjust_score(board_name, student_score):
    if board_name == "cbse":
        adjusted_score = student_score * scaling_factor_cbse
    elif board_name == "icse":
        adjusted_score = student_score * scaling_factor_icse
    else:  
        adjusted_score = student_score
    return adjusted_score

board_name = input("Enter the name of your education board (cbse, icse, state): ").lower()
student_score = float(input("Enter your percentage: "))

adjusted_score = adjust_score(board_name, student_score)
print(f"Your score adjusted to the State board's scale is: {adjusted_score:.2f}")
