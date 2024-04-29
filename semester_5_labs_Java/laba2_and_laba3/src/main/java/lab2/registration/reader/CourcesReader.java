package lab2.registration.reader;

import com.fasterxml.jackson.databind.ObjectMapper;
import lab2.registration.model.CourseInstance;

import java.io.File;
import java.io.IOException;

// Добавлен мною класс-ридер по примеру класса StudentDataReader
public class CourcesReader {

    private ObjectMapper objectMapper = new ObjectMapper();

    /**
     * @return список студентов-бакалавров
     */
    public CourseInstance[] readValues() throws IOException {
        return objectMapper.readValue(new File("src/main/resources/courseInstances.json"), CourseInstance[].class);
    }
}
