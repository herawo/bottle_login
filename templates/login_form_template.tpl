<head>
	<link rel="stylesheet" type="text/css" href="/static/css/login_form.css">
</head>
<body>
	<form action="/login" method="POST">
	  <div class="imgcontainer">
		<img src="/static/image/login.png" alt="Avatar" class="avatar">
	  </div>

	  <div class="container">
		<label for="username"><b>Username</b></label>
		<input type="text" placeholder="Enter Username" name="username" required>

		<label for="password"><b>Password</b></label>
		<input type="password" placeholder="Enter Password" name="password" required>

		<input value="Login" type="submit" />
	<!--
		<label>
		  <input type="checkbox" checked="checked" name="remember"> Remember me
		</label>
	-->
	  </div>

	  <div class="container" style="background-color:#f1f1f1">
		<button type="button" class="cancelbtn">Cancel</button>
	<!--
		<span class="psw">Forgot <a href="#">password?</a></span>
	-->
	  </div>
	</form> 
</body>
