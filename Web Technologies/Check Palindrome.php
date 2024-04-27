<?php
$input = readline("Enter a string: ");
$input = strtolower(str_replace(' ', '', $input));
$reversed = strrev($input);
if ($input === $reversed) {
    echo "The input is a palindrome.";
} else {
    echo "The input is not a palindrome.";
}
?>
