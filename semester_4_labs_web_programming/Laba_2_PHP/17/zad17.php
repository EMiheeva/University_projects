<?php
$array__arrays = array();
$d = 10;
for ($i = 0; $i < 10; $i++) {
    $array__arrays[$i] = "";
    for ($j = 0; $j < $i+1; $j++) {
        $array__arrays[$i] .= "x";
    }
}
for ($i = 0; $i < count($array__arrays); $i++)
    echo $array__arrays[$i] . "\n";


function arrayFill($a, $b = 5) {
    $arr = array();
    for ($i = 0; $i < $b; $i++) {
        $arr[$i] = "";
        $arr[$i] .= $a;
    }
    return $arr;
}
$arr1 = arrayFill('x',5);
for ($i = 0; $i < count($arr1); $i++)
    echo $arr1[$i] . "\n";


$array_functions_2 = [[1, 2, 3], [4, 5], [6]];
$sum = 0;
for ($i = 0; $i < count($array_functions_2); $i++) {
    $sum += array_sum($array_functions_2[$i]);
}
echo $sum . "\n";


$arr2 = array();
$count1 = 0;
for ($i = 0; $i < 3; $i++) {
    $arr2_help = array();
    for( $j = 0; $j < 3; $j++) {
        $arr2_help[$j] = ++$count1;
        echo $arr2_help[$j] . "\n";
    }
    $arr2[$i] = $arr2_help;
}


$arr3 = [2,5,3,9];
$result = $arr3[0] * $arr3[1] + $arr3[2] * $arr3[3];
echo $result . "\n";


$user = array(
    'name' => 'Zinaida ', 
    'surname' => 'Volkova', 
    'patronymic' => 'Stepanovna');
echo $user['surname'], " ", $user['name'], " ", $user['patronymic'], "\n", "\n";


$date = array (
    'year' => '2023', 
    'month'=>'3' , 
    'day'=>'24');
echo $date['year'],'-',$date['month'], "-",$date['day'], "\n", "\n";


$arr4 = ['a', 'b', 'c', 'd', 'e'];
echo count($arr4) . "\n";

echo end($arr4), " ", prev($arr4);
?>
