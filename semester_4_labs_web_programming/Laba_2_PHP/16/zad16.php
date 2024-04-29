<?php
function increaseEnthusiasm($a) {
    return $a .= "!";
}

$b = "I want to sleep very much ";
echo increaseEnthusiasm($b);

function repeatThreeTimes($a) {
    $j = $a;
    for($i = 0; $i < 2; $i++)
        $j .= $a;
    return $j;
}

echo "\n";
echo repeatThreeTimes($b);
echo "\n";
echo repeatThreeTimes(increaseEnthusiasm($b));

function cut($a, $d = 10) {
    $j = "";
    for($i = 0; $i < $d; $i++)
        $j .= $a[$i];
    return $j;
}
echo "\n";
echo cut(repeatThreeTimes($b), 15);


$number = 2023;
function sum_of_number($a) {
    $arr = str_split($a, 1);
    $result = array_sum($arr);
    if ($result > 9)
        return sum_of_number($result);
    else
        return $result;
}
echo "\n";
echo sum_of_number($number);
?>