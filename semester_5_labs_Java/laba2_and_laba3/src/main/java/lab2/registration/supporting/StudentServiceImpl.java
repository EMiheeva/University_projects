package lab2.registration.supporting;

import lab2.registration.model.*;
import lab2.registration.service.StudentService;
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.Arrays;

// Назвала класс соответственно интерфейсу, который имплементирует
public class StudentServiceImpl implements StudentService {
    private Student[] students;
    private CourseInstance[] courses;
    private CourseInfo[] infos;

    private ArrayList<Pair<Long, Long>> subscriptions = new ArrayList<>();
    // Пара: ({ID студента} - {ID курса})

    // Конструктор класса, который имплементирует интерфейс
    // Класс назван соответственно интерфейсу.
    public StudentServiceImpl(
            Student[] students,
            CourseInstance[] courses,
            CourseInfo[] infos) {
        this.students = students;
        this.courses = courses;
        this.infos = infos;
    }

    @Override
    public ActionStatus subscribe(long studentId, long courseId) {

        Student student = Arrays.stream(students).filter(s -> s.getId() == studentId).findFirst().orElse(null);

        if (student == null) {
            return ActionStatus.NOK;
        }

        for (CourseInfo info: infos) {
            if (info.getId() == courseId) {
                if (Arrays.stream(info.getStudentCategories()).noneMatch(x -> x == student.getCategory())) {
                    return ActionStatus.NOK;
                }

                if (!Arrays.stream(info.getPrerequisites()).allMatch(x -> Arrays.stream(student.getCourses()).anyMatch(y -> y == x))) {
                    return ActionStatus.NOK;
                }
            }
        }

        for (CourseInstance c: courses) {
            if (c.getCourseId() == courseId && c.getStartDate().isBefore(LocalDate.now())) {
                return ActionStatus.NOK;
            }
        }

        this.subscriptions.add(new Pair<>(studentId, courseId));
        return ActionStatus.OK;
    }

    @Override
    public ActionStatus unsubscribe(long studentId, long courseId) {
        if (this.subscriptions.removeIf(x -> x.getKey() == studentId && x.getValue() == courseId) ) {
            return ActionStatus.OK;
        }
        return ActionStatus.NOK;
    }

    @Override
    public CourseInstance[] findAllSubscriptionsByStudentId(long studentId) {

        ArrayList<CourseInstance> list_courses = new ArrayList<>();

        for (Pair<Long, Long> s: subscriptions) {
            if (s.getKey() == studentId) {
                for (CourseInstance c: courses) {
                    if (c.getCourseId() == s.getValue()) {
                        list_courses.add(c);
                        break;
                    }
                }
            }
        }
        return list_courses.stream().toArray(CourseInstance[]::new);
    }
}
