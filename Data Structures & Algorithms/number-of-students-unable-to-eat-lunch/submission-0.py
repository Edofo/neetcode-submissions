class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = len(students)
        idx_student = 0
        idx_sandwich = 0

        while idx_sandwich < len(sandwiches) and idx_student < len(students):
            if students[idx_student] == sandwiches[idx_sandwich]:
                count -= 1
                students[idx_student] = -1
                idx_student = 0
                idx_sandwich += 1
            else: 
                idx_student += 1



        return count