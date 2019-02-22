<?php
    $data1 = 'Adam Słowdowy';
    $data2 = 'Adam Słowdowx';
    echo hash('md5', $data1);
    echo'
';
    echo hash('md5', $data2);
    echo'
';
    echo hash('sha256', $data2);
    echo'
';
    echo hash('haval256,5', $data2);
?>
