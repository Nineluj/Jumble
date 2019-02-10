import { Component, OnInit } from '@angular/core';
import * as $ from 'jquery';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {

  constructor(private router: Router) { }

  ngOnInit() {
  }

  // Submits the user email and password.
  public submitLogin() {
    // $.ajax({
    //   type: "POST",
    //   url: "http://localhost:5000",
    //   data: { username: $('#emailInput').val(), password: $('password').val() },
    //   success: this.loginSuccessHandler
    // });
  }

  private loginSuccessHandler() {
    // this.router.navigate(['userInfo']);
    // route to the user info page within this function.
  }

}
