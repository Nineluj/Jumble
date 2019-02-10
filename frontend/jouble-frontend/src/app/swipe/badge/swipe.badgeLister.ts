import { Component, Input } from '@angular/core';
import { BadgeData } from 'app/userService';

@Component({
  selector: 'badge-lister',
  templateUrl: './swipe.badgeLister.html',
  styleUrls: ['./swipe.badgeLister.scss']
})
export class BadgeLister {
  title = 'badge_module';

  @Input() badgeData: BadgeData[];

  constructor() { }
}
