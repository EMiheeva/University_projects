<?php
$very_bad_unclear_name = "15 chicken wings";

$order =& $very_bad_unclear_name; //  ссылку на переменную $very_bad_unclear_name
$order .= " is very tasty!"; //конкатенация

echo "\nYour order is: $very_bad_unclear_name.";
?>