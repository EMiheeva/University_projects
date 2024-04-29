package lab2.registration.supporting;

// Класс Pair используется в качестве базовой структуры для хранения двух связанных объектов
// В моем случае пара {ID студент} - {ID курс}
public class Pair<Key, Value> {
    private final Key key;
    private final Value value;

    public Pair(Key key, Value value) {
        this.key = key;
        this.value = value;
    }

    public Key getKey() {
        return this.key;
    }

    public Value getValue() {
        return this.value;
    }
}