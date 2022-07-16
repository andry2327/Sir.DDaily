<?php
if(isset($_POST['submit'])){
  $message=$_POST['inputbox'];
  $to='YOUR_MAIL'; // Receiver Email ID, Replace with your email ID
  $subject='Form Submission';
  $email = "YOUR_MAIL"
  $headers="From: ".$email;

  if(mail($to, $subject, $message, $headers)){
    echo "<h1>Success! Thank you, you can return to Sir.Ddaily</h1>";
  }
  else{
    echo "Something went wrong!";
  }
}
?>
