<head>
	<link rel="stylesheet" type="text/css" href="/static/css/login_form.css">
</head>
<body>
	<form action="/register" method="POST">
	  <div class="container">
		<label for="username"><b>Username</b></label>
		<input type="text" placeholder="Enter Username" name="username" required>

		<label for="password"><b>Password</b></label>
		<input type="password" placeholder="Enter Password" name="password" required>

		<input value="Register" type="submit" />
	  </div>

	  <div class="container" style="background-color:#f1f1f1">
		<button type="button" class="cancelbtn">Cancel</button>
	  </div>
	  
	</form> 
</body>

