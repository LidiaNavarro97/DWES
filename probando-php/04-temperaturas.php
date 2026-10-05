<?php

$numeros = [];

for($i = 0; $i < 10; $i++){
    $numeros[$i] = rand(1,30);
}
for($i = 0; $i < 10; $i++){
    echo " Temperatura: " .$numeros[$i] . "<br>";
}

$media = array_sum($numeros)/count($numeros);
echo "Media : " . $media . "<br>";

$maximo = max($numeros);
echo "Maximo : " . $maximo . "<br>";

$minimo = min($numeros);
echo "Mínimo : " . $minimo . "<br>";


?>