package lab2.registration.supporting;

import lab2.registration.model.Instructor;
import lab2.registration.model.Student;
import lab2.registration.service.CourseInstructorService;
import java.util.ArrayList;

// Назвала класс соответственно интерфейсу, который имплементирует
public class CourseInstructorServiceImpl implements CourseInstructorService {

    private Student[] students;
    private Instructor[] instructors;

    public CourseInstructorServiceImpl(
            Student[] students,
            Instructor[] instructors
    ) {
        this.students = students;
        this.instructors = instructors;
    }
    @Override
    public Student[] findStudentsByCourseId(long courseId) {

        ArrayList<Student> list_students = new ArrayList<>();

        for (Student student : students) {
            for (long id: student.getCourses()) {
                if (id == courseId) {
                    list_students.add(student);
                    break;
                }
            }
        }
        return list_students.stream().toArray(Student[]::new);
    }

    @Override
    public Student[] findStudentsByInstructorId(long instructorId) {

        ArrayList<Student> list_students = new ArrayList<>();

        for (Instructor i: this.instructors) {
            if (i.getId() == instructorId) {
                for (long courseId: i.getCourses()) {
                    for (Student s: this.findStudentsByCourseId((courseId))) {
                        list_students.add(s);
                    }
                }
            }
        }
        return list_students.stream().distinct().toArray(Student[]::new);
    }

    @Override
    public Instructor[] findReplacement(long instructorId, long courseId) {

        ArrayList<Instructor> list_instructors = new ArrayList<>();

        for (Instructor i: this.instructors) {
            if (i.getId() != instructorId) {
                for (long id: i.getCourses()) {
                    if (id == courseId) {
                        list_instructors.add(i);
                    }
                }
            }
        }
        return list_instructors.stream().distinct().toArray(Instructor[]::new);
    }
}
