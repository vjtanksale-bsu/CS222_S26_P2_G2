from src.file_reader import FileReader
from src.course_catalog import CourseCatalog

def main():
    file_path="data/courses.txt"
    reader=FileReader()
    lines=reader.read_lines(file_path)
    if not lines:
        print("No data found in the file.")
        return
    catalog=CourseCatalog()
    unique_courses=catalog.extract_unique_courses(lines)
    
    print(f"Found {len(unique_courses)} unique courses:")
    
    for course in unique_courses:
        print(course)

if __name__=="__main__":
    main()