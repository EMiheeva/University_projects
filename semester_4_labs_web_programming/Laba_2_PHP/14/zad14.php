<?php
//Задание 14: работа с %
$a = 10;
$b = 3;
echo $a % $b;
if ($a % $b == 0)
    echo "\n Делится";
else {
    echo "\n Делится с остатком";
    echo "\n";
    echo $a % $b;
}
?>

<?php
//Задание 14: работа со степенью и корнем
$st = pow(2, 10);
echo $st;
echo "\n";
echo sqrt(245);
echo "\n";

$array = Array(4, 2, 5, 19, 13, 0, 10);
$sum_sqrts = 0;
foreach ($array as $value)
    $sum_sqrts += pow($value,2);
echo sqrt($sum_sqrts);
?>

<?php
//Задание 14: работа с функциями округления
echo round(sqrt(379), 0);
echo "\n";
echo round(sqrt(379), 1);
echo "\n";
echo round(sqrt(379), 2);
echo "\n";
$array_587 = Array('floor', 'ceil');
$array_587['floor'] = floor(sqrt(587));
$array_587['ceil'] = ceil(sqrt(587));
?>

<?php
//Задание 14: работа с min и max
$max = max(4, -2, 5, 19, -130, 0, 10);
echo "\n $max";
$min = min(4, -2, 5, 19, -130, 0, 10);
echo "\n $min";
?>

<?php
//Задание 14: работа с рандомом
echo rand(1,100);
$array_rand = Array();
for ($i = 0; $i < 10; $i++)
    $array_rand[$i] = rand();
?>


<?php
//Задание 14: работа с модулем
$a = rand();
$b = rand();
echo abs($a - $b);
$array_abs = array(1, 2, -1, -2, 3, -3);
for ($i = 0; $i < count($array_abs); $i++)
    if ($array_abs[$i] < 0)
        $array_abs[$i] = abs($array_abs[$i]);
?>

<?php
//Задание 14: общее
//первый пункт
$number = 30;
$array_del = array();
$count = 0;
for ($i = 1; $i < $number; $i++)
    if ($number % $i == 0) {
        $array_del[$count] = $i;
        $count++;
        }

echo $number;
foreach ($array_del as $value)
        echo "\n $value";
?>

<?php
//второй пункт
$array_number = array(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);
$count = 0;
$sum = 0;
foreach ($array_number as $value) {
    $sum += $value;
    $count++;
    if ($sum > 10) {
        echo "\n$count";
        break;
    }
}
?>