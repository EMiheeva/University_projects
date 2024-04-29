package lab2.registration.model;


/**
 * Класс для информации о студенте
 */
public class Student extends Person {

    /**
     * список идентификаторов курсов (CourseInstance.id), пройденных студентом
     */
    private long[] completedCourses;

    // TODO: добавить геттеры и сеттеры {ГОТОВО}
    private StudentCategory category;

    public long[] getCourses() {
        return completedCourses;
    }

    public void setCourses(long[] value) {
        completedCourses = value;
    }

    public StudentCategory getCategory() {
        return this.category;
    }

    public void setCategory(StudentCategory value) {
        this.category = value;
    }

}