<?php
function first($a, $b) {
    if ($a + $b > 10)
        return true;
    else
        return false;
}


function second($a, $b) {
    if ($a === $b)
        return true;
    else
        return false;
}


$test = rand(0,1);
if (!$test)
    echo "Верно \n";


echo "\n";
$age = rand (1, 200);
echo $age, " ";
if ($age > 99 || $age < 10) {
    if ($age >99)
        echo'Число больше 99';
     else
        echo 'Число меньше 10';
}
else {
  $arr = str_split($age, 1);
  $c = array_sum($arr);
  if ($c <= 9)
    echo 'Cумма цифр однозначна';
  else
    echo 'Cумма цифр двузначна';
}


$arr5 = [1,6,5];
if (count($arr5) == 3)
    echo "\n" . array_sum($arr5);
?>
