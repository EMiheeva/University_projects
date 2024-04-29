package lab2.registration.model;


/**
 * Класс для информации о преподавателе
 */
public class Instructor extends Person {

    /**
     * Идентификаторы курсов, которые может вести преподаватель
     */
    int[] canTeach;

    // TODO: добавить геттеры и сеттеры {ГОТОВО}

    public int[] getCourses() {
        return canTeach;
    }

    public void setCourses(int[] value) {
        canTeach = value;
    }

}
