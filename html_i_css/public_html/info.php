
<?php  //zancznik otwierający skrypt php
    //phpinfo();
    print_r($_POST);
?>
<!-- znacznik zamykający skrypt -->



<form name="formularz" id="formularz" method="POST">
  <table class="table">
    <tr>
      <td><label for="imie">Imie:</label></td>
      <td>  <input type="text" name="imie" value=""></td>
    </tr>
    <tr>
      <td>  <label for="nazwisko">Nazwisko:</label> </td>
      <td><input type="text" name="nazwisko" value=""></td>
    </tr>
  </table>

  <fieldset>
    <legend>Wybierz plec:</legend>
    <input type="radio" name="gender" value="m" checked> Mezczyzna<br>
    <input type="radio" name="gender" value="f"> Kobieta<br>
    <input type="radio" name="gender" value="o"> Nie wiadomo co

  </fieldset>

  <fieldset>
    <legend>Wybierz pojazd</legend>
    <input type="checkbox" name="vehicle1" value="Bike"> I have a bike<br>
    <input type="checkbox" name="vehicle2" value="Car"> I have a car
</fieldset>

<select name="cars">
  <option value="volvo">Volvo</option>
  <option value="saab">Saab</option>
  <option value="fiat" selected>Fiat</option>
  <option value="audi">Audi</option>
</select>

<select name="cars2" multiple>
  <option value="volvo">Volvo</option>
  <option value="saab">Saab</option>
  <option value="fiat">Fiat</option>
  <option value="audi">Audi</option>
</select>

<br>
  <textarea name="message" rows="10" cols="30">
    Kot
  </textarea>
<br>

    <input type="submit" name="przycisk" value="Prześlij">
    <input type="reset" name="przycisk2" value="Resetuj">
</form>
