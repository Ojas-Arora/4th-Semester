<?php
function factorial($n) {
    if ($n <= 1) {
        return 1;
    } else {
        return $n * factorial($n - 1);
    }
}
$number = readline("Enter a number: ");
$result = factorial($number);
echo "The factorial of $number is: $result";
?>
