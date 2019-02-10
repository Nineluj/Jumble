import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})

// This class represents the data for the user currently on top
// of the card stack. When the checkmark or X is clicked, we will make
// an ajax call from the swipe comonent to Matt's endpoint that returns
// the next user data JSON. Our callback function will update the data in
// this service (and components looking at this service will display the new data).
export class CurrentCardDataService {

  private firstName: string;
  private lastName: string;
  private email: string;
  private major; string;
  private slack: string;
  private interests: string;
  private ideas: string;
  private skills: string;
  private picture: HTMLImageElement;

  constructor() {
    // For testing only.
    this.firstName = 'Test Name 1';
    this.email = 'boost@dorial.com';
    this.major = 'Psychology';
    this.slack = 'mkach_slack';
  }

  getFirstName(): string {
    return this.firstName;
  }
  getEmail(): string {
    return this.email;
  }
  getMajor(): string {
    return this.major;
  }
  getSlack(): string {
    return this.slack;
  }
}
