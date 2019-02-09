import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { SwipePanelComponent } from './swipe-panel/swipe-panel.component';
import { UserInfoComponent } from './user-info/user-info.component';
import { LoginComponent } from './login/login.component';

const routes: Routes = [
  { path: 'swipe', component: SwipePanelComponent },
  { path: 'userInfo', component: UserInfoComponent },
  { path: '', component: LoginComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
