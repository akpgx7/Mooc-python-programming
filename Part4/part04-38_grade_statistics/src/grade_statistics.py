# Write your solution here
def collect_input():
    results = []
    
    while True:
        line = input("Exam points and exercises completed:")
        if line == "":
            break
        parts = line.split()
        exam = int(parts[0])
        exercise = int(parts[1])
        results.append((exam,exercise))
    return results

def exercise_point(exercise):
    return exercise//10

def grade(total_points,exam_point):
    if exam_point < 10:
        return 0
    if total_points <= 14:
        return 0
    elif total_points <= 17:
        return 1
    elif total_points <=20:
        return 2
    elif total_points <= 23:
        return 3
    elif total_points <= 27:
        return 4
    else:
        return 5

def print_statistics(results):
    grades = []
    total_point_list = []

    for exam, exercise in results:
        ex_point = exercise_point(exercise)
        total = exam + ex_point
        g = grade(total,exam)
        grades.append(g)
        total_point_list.append(total)
    
    avg = sum(total_point_list)/len(total_point_list)
    passed = sum(1 for g in grades if g > 0)
    pass_pct = passed / len(grades) * 100
    print(f"Points average: {avg:.1f}")
    print(f"Pass percentage: {pass_pct:.1f}")
    print(f"Grade distribution:")
    for g in range(5,-1,-1):
        stars = "*"* grades.count(g)
        print(f"  {g}: {stars}")

def main():
    results = collect_input()
    print("\nStatistics:")
    print_statistics(results)

main()