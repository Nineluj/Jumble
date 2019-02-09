import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { Card } from './swipe/card.component';
import { ContactsComponent } from './contacts/contacts.component';
import { ContactsCardComponent } from './contacts/contact_card/contacts.contacts_card';
import { InfoComponent } from './info/info.component';
import { BadgeLister } from './swipe/badge/swipe.badgeLister';
import { SwipePanelComponent } from './swipe-panel/swipe-panel.component';
import { LoginComponent } from './login/login.component';
import { UserInfoComponent } from './user-info/user-info.component';


@NgModule({
  declarations: [
    AppComponent,
    ContactsComponent,
    ContactsCardComponent,
    InfoComponent,
    Card,
    BadgeLister,
    SwipePanelComponent,
    UserInfoComponent,
    LoginComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
