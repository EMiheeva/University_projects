<?php
function printStringReturnNumber() {
    echo "Возвращаемое значение будет равняться: ";
    return rand();
}
$my_num = printStringReturnNumber();
echo $my_num;
?>