INPUT student_name, score
IF score >= 70 AND score <= 100 THEN
    grade = "A"
ELSE IF score >= 60 AND score <= 69 THEN
    grade = "B"
ELSE IF score >= 50 AND score <= 59 THEN
    grade = "C"
ELSE IF score >= 45 AND score <= 49 THEN
    grade = "D"
ELSE IF score >= 40 AND score <= 44 THEN
    grade = "E"
ELSE IF score < 40 THEN
    grade = "F"
END IF
PRINT student_name, score, grade
