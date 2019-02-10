// import {Http} from '@angular/common/http';
// import { Injectable } from '@angular/core';

export interface Info {
  type: string;
  info: string;
}

export interface BadgeData {
  badgeName: string;
  badgeImg: string;
}

export class User {
  firstName: string;
  lastName: string;
  picture: HTMLImageElement;
  slackUsername: string;
  userInfo: Info[];

  static create(data: any) {
    return new User(data);
  }

  constructor(data: any) {
    this.firstName = data.firstName;
    this.lastName = data.lastName;
    this.picture = data.picture;
    this.slackUsername = data.slackUsername;
  }
}

export class SampleData {
  user: User;
  userData = {
    firstName: 'Alex',
    lastName: 'Tapley',
    picture: 'assets/user.jpg',
    slackUsername: 'atapley'
  };

  contacts: User[];
  contact1 = {
    firstName: 'Matt',
    lastName: 'Kachmar',
    picture: 'assets/user.jpg',
    slackUsername: 'mkach'
  };
  contact2 = {
    firstName: 'Thomas',
    lastName: 'Vboy',
    picture: 'assets/user.jpg',
    slackUsername: 'tvoy'
  };
  contact3 = {
    firstName: 'Natt',
    lastName: 'Tuck',
    picture: 'assets/user.jpg',
    slackUsername: 'ntuck'
  };

  constructor() {
    this.user = new User(this.userData);
    this.contacts = [new User(this.contact1), new User(this.contact2), new User(this.contact3)];
  }

  getUser(): User {
    return this.user;
  }

  getContacts(): User[] {
    return this.contacts;
  }
}

// @Injectable()
// export class UserData {
//   constructor(private http: Http){
//     this.customers = http.get('http://beta.json-generator.com/api/json/get/VkCoTefEg')
//       .map(res => res.json())
//       .map(rawCustomers => rawCustomers.map(Customer.create));
//   }
// }
