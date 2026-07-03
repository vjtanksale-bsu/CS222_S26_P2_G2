class CourseCatalog:
    def extract_unique_courses(self, raw_lines):
        unique_courses=set()
        
        for line in raw_lines:
            clean_line = line.strip()
            if clean_line:
                unique_courses.add(clean_line)
         
        return sorted(list(unique_courses))
