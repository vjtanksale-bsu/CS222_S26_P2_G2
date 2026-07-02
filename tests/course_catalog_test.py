from src.course_catalog import CourseCatalog

def test_course_catalog():
    data=["CS120\n", " MATH165 ", "CS120", "\n", "CS121"]
    catalog=CourseCatalog()
    result=catalog.extract_unique_courses(data)
    expected=["CS120", "CS121", "MATH165"]
    assert result==expected
