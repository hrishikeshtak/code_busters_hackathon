import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { UserService } from './services/user-services';
import { TopnavComponent } from './topnav/topnav.component';
import { BottomnavComponent } from './bottomnav/bottomnav.component';
import { LoginComponent } from './login/login.component';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'code_busters_ui';
  navigatorDetails : any;
  isLoggedIn :Boolean = false;
  constructor(private _router : Router, private navDetails: UserService) { }
    navigateTo(path: String){
      console.log([path])
      this._router.navigate([path])
    }
    ngOnInit(): void {
      console.log('TopNav--' +this.navDetails.isLoggedIn)
      this.isLoggedIn = this.navDetails.isLoggedIn;
      this.navigatorDetails = this.navDetails.navigatorDetails;
      console.log('topNav' + this.navigatorDetails);
    }
}
