<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>week 8 - forms with many inputs</title>
  </head>
  <body>


      <form method="post">
      <p>User Data</p>
      <p><label for="inp01">Full Name</label> <br>
      <input type="text" name="fullName" id="inp01" size="25" value=""></p>
      <p><label for="inp02">Password</label> <br>
      <input type="password" name="password" id="inp02" size="25" value=""></p>
      <p><label for="inp03">StudentID</label> <br>
      <input type="text" name="studentID" id="inp03" size="25" value=""></p>

      <p>Prefered Time <br>
      <input type="radio" name="time" value="am">AM</input> <br>
      <input type="radio" name="time" value="pm" checked>PM</input></p>

      <p>Classes: <br>
        <input type="checkbox" name="class1" value="FrontEnd">
          Michigan Uni - Front End Specilization <br>
        <input type="checkbox" name="class2" value="Backend">
          Michigan Uni - Back End Specilization <br>
        <input type="checkbox" name="class3" value="DataScience">
          Michigan Uni - Data Science Specilization <br> </p>

      <p><label for="inp05">Preferred Language:</label> <br>
        <select class="" id="inp05" name="Language">
          <option value="0">--Select One--</option>
          <option value="1">C++</option>
          <option value="2">Java</option>
          <option value="3">R</option>
          <option value="4">Python</option>
          <option value="5">JavaScript</option>
          <option value="6">C#</option>
        </select></p>

      <p> <label for="inp06">Tell us about yourself:</label> <br>
        <textarea name="aboutUser" rows="10" cols="40">I love STEM...and lasagna</textarea></p>

      <br>

      <p>
      <input type="submit" name="userData" value="Submit">
      <input type="button" name="" value="Escape" onclick="location.href='http://localhost:8888/week%208/formsWithInputs.php'; return false;">
      </p>

    </form>

    <br>
    <hr>

    <p><b>Dev Area:</b></p>

    <pre>
      $_POST:

      <?php
      print_r($_POST);
       ?>
    </pre>
  </body>
</html>
