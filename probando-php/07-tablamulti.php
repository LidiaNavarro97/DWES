<?php
function tablaMultiplicar($numero) {
    echo "Tabla del : " . $numero;
    
    for ($i = 1; $i <= 10; $i++) {
        $resultado = $numero * $i;
        echo $numero . " x " . $i . " = " . $resultado . "<br>";
    }
}

function tablasParametros($inicio, $fin) {
    for ($i = $inicio; $i <= $fin; $i++) {
        tablaMultiplicar($i);
    }
}
?>