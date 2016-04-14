<?php
	
	$name = $_POST['contactName'];
	$email = $_POST['contactEmail'];
	$message = $_POST['contactMessage'];
	$subject = $_POST['contactSubject'];
	
	$formcontent="Name: $name \n\nEmail: $email \n\nMessage: $message";
	
	// Enter the email where you want to receive the notification when someone submit form
	$recipient = "livin@lmntrx.com";
	
	$subject = $subject.": Contact Form - livinmathew.me";
	
	$mailheader = "From: $email\\r\\n";
	$mailheader .= "Reply-To: $email\\r\\n";
	$mailheader .= "MIME-Version: 1.0\\r\\n";
	
	$success = mail($recipient, $subject, $formcontent, $mailheader);
	
	if ($success == true){
	
?>
	
	<script language="javascript" type="text/javascript">
		alert('Thank you for your message. We will contact you shortly.');
		window.location = "../index.html";
	</script>
	
<?php
	
	} else {
	
?>

    <script language="javascript" type="text/javascript">
		alert('Message not sent.');
		window.location = "../index.html";
    </script>
	
<?php

    }
	
?>