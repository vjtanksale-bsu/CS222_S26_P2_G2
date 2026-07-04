def filter_courses(course_list, criteria):
    if not course_list:
        return []
    return [c for c in course_list if criteria.upper() in c.upper()]