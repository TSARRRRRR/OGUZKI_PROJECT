<?php
 require_once('db.php')
$login = $_POST['login']
$username = $_POST['username']
$email = $_POST['email']
$password = $_POST['password']

if(empty($login) || empty($password) || empty($username) || empty($email)){
    echo "заполните все поля"
}else{
    $sql = "INSERT INTO `users` (login,username,email,pass) VALUES (`$login`, `$password`, `$email`)"

    $conn -> query($sql);
}
