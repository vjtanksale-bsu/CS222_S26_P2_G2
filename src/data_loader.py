import os

def load_courses(filename='data/courses.txt'):
    courses = []
    file_path = os.path.join(os.path.dirname(__file__), '..', filename)
    with open(file_path, 'r') as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) >= 5:
                courses.append({
                    'code': parts[0],
                    'section': parts[1],
                    'days': parts[2],
                    'start': int(parts[3]),
                    'end': int(parts[4])
                })
    return courses