# wp_passgenerator

Wordpress(WP) password generator based on the wordpress wp_generate_password method. This is meant to be used with the XMLRPC Bruteforce Attack Vector.

The wp_generate_password method is the wordpress function used to generate random passwords during initial installations. Please see https://developer.wordpress.org/reference/functions/wp_generate_password/ for more information. 

The idea behind this is to mimic this method to generate your own wordlist for a potential bruteforce attack to primarily target those installations that do not change the default generated password. 

The minimum number of chars based on the wordpress documentation is 12 up to N number of chars. This generator uses Alpha Numeric Chars, Digits, Special and Extended Special Characters to generate the random passwords. 

You can actually also use this password generator for all other purposes. 
