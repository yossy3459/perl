#!/usr/local/bin/perl
print "Content-Type: text/html;\n\n";

$a = 2;
$b = 3;

print "Hello World!<br>\n" x 3;
print $a * $b,"<br>\n";

print $a . $b,"<br>\n";

print $a <=> $b,"<br>\n";

print $a lt $b,"<br>\n";

@fruit = ("apple","orange","banana");

# 配列の個数
$num = @fruit;

print "この配列の要素は$num個あります。<br>\n";

@char = ("C","A","D","B");

@char = sort{ $b cmp $a } @char;
print "@char<br>\n";

@char = sort{ $a cmp $b } @char;
print "@char<br>\n";

@list = (
    ['a','b','c'],
    ['d','e','f'],
    ['g','h','i'],
    );

print "$list[1][1]<br>\n";

print "@{$list[0]}<br>\n";

foreach $tmp (@list) {
    print "@{$tmp}<br>\n";
}

foreach $t
