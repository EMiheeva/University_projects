<?php
$array_one = [65, 634, 891, 20, 0, 7, 14];
$result = array_sum($array_one) / count($array_one);
echo "\n" . $result;


echo "\n" . array_sum(range(1, 100));

echo "\n";

$array_two = [16, 52, 43, 34, 25, 16];
function sq($a) {
    return sq($a);
}
$array_two = array_map('sqrt', $array_two);
foreach ($array_two as $value)
    echo $value . "\n";


$array_three = array_combine(range('a', 'z'), range(1, 26));
$flag = 1;
while ($flag <= 26) {
    echo key($array_three) . "\n" . current($array_three) . "\n";
    next($array_three);
    $flag++;
}  


$digit = "1234567890";
$array_four = str_split($digit, 2);
echo array_sum($array_four);
?>