<?php

$numeros = [];

for ($i = 0; $i < 10; $i++){
    $numeros[$i] = rand(1,30);
}

for ($i = 0; $i < 10; $i++){
    echo "La posicion : " . $i . $numeros[$i];
}



?>