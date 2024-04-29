<?php

function redirectToHome():void{
    header('Location: laba3_1.php');

    exit();
}

if (false === isset($_POST['Email'], $_POST['Title'], $_POST['Description'])){
  
    redirectToHome();
}

$category = $_POST['Category'];
$title = $_POST['Title'];
$desc = $_POST['Description'];
$em = $_POST['Email'];


$dir = "categories/{$category}/{$em}";
if (is_dir($dir)){
    $filePath = "categories/{$category}/{$em}/{$title}.txt";
} else{
    $folder = "categories/{$category}/{$em}";
    $result = mkdir($folder); 
    
    $filePath = "categories/{$category}/{$em}/{$title}.txt";
}


if (false ===  file_put_contents($filePath, $desc))
{
    throw new Exception('Something went wrong');
}
chmod($filePath, 0777);
redirectToHome();