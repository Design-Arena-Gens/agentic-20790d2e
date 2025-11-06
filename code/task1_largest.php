<?php
/**
 * Program: Largest of three numbers using nested if statements.
 * Usage: php task1_largest.php
 */

$numbers = [56, 92, 37]; // Sample dataset; adjust as needed.

$a = $numbers[0];
$b = $numbers[1];
$c = $numbers[2];

$largest = $a;

if ($largest < $b) {
    if ($b > $c) {
        $largest = $b;
    } else {
        $largest = $c;
    }
} else {
    if ($largest < $c) {
        $largest = $c;
    }
}

echo "Input numbers: {$a}, {$b}, {$c}\n";
echo "Largest number: {$largest}\n";
