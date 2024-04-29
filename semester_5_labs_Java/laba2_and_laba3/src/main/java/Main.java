import lab2.registration.model.*;
import lab2.registration.reader.CourceInfoReader;
import lab2.registration.reader.CourcesReader;
import lab2.registration.reader.InstructorsReader;
import lab2.registration.supporting.CourseInstructorServiceImpl;
import lab2.registration.service.StudentService;
import lab2.registration.supporting.StudentServiceImpl;
import java.util.Arrays;
import java.util.stream.Stream;

// Добавлен мною класс-main, чтобы посмотреть, как всё работает
public class Main {
    public static void main(String[] args) {
        try {
             Student[] masters = new lab2.registration.reader.StudentDataReader().readBachelorStudentData();
             Student[] bachelors = new lab2.registration.reader.StudentDataReader().readMasterStudentData();

             for (Student b: bachelors) {
                 b.setCategory(StudentCategory.BACHELOR);
             }

             for (Student m: masters) {
                m.setCategory(StudentCategory.MASTER);
             }

             Student[] students = Stream.concat(Arrays.stream(masters), Arrays.stream(bachelors)).toArray(Student[]::new);

             Instructor[] instructors = new InstructorsReader().readValues();
             CourseInstance[] courses = new CourcesReader().readValues();
             CourseInfo[] courseInfos = new CourceInfoReader().readValues();

             CourseInstructorServiceImpl instructorService = new CourseInstructorServiceImpl(students, instructors);
             StudentService studentService = new StudentServiceImpl(students, courses, courseInfos);
        } catch (Exception ex) {
            System.out.println("Где-то ошибка!");
        }
        System.out.println("Программа работает!");
    }
}

