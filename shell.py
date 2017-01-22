#!/bin/sh


echo_msg()
{
    echo $1
}

say_hi()
{
    echo $1" say hi to all:)"
}

say_bye()
{
    echo $1" say goodbye to all:("
}

echo_msg "Hello, "
echo_msg "Welcome to git new world!"

say_hi Jack
say_bye Jack
