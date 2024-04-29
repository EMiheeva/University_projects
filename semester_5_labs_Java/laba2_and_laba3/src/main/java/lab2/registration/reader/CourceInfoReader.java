package lab2.registration.reader;

import com.fasterxml.jackson.databind.ObjectMapper;
import lab2.registration.model.CourseInfo;

import java.io.File;
import java.io.IOException;

// Добавлен мною класс-ридер по примеру класса StudentDataReader
public class CourceInfoReader {
    private ObjectMapper objectMapper = new ObjectMapper();

    /**
     * @return список студентов-бакалавров
     */
    public CourseInfo[] readValues() throws IOException {
        return objectMapper.readValue(new File("src/main/resources/courseInfos.json"), CourseInfo[].class);
    }
}
