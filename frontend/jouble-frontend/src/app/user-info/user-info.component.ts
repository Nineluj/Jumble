import { Component, OnInit } from '@angular/core';
import * as $ from 'jquery';

@Component({
  selector: 'app-user-info',
  templateUrl: './user-info.component.html',
  styleUrls: ['./user-info.component.scss']
})
export class UserInfoComponent implements OnInit {

  constructor() { }

  ngOnInit() {
  }

    // Submits the user info, posting any changes.
    public submitLogin() {
      $.ajax({
        type: "POST",
        url: "http://localhost:5000",
        data: { },
        success: this.userInfoSuccessHandler
      });
    }
  
    private userInfoSuccessHandler() {
      // this.router.navigate(['swipe']);
      // route to the user info page within this function.
    }

}
