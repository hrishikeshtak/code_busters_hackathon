import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { UserService } from './services/user-services';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'code_busters_ui';
  navigatorDetails : any;
  isLoggedIn :Boolean = false;
  nDetails :any;
  constructor(private _router : Router, private navDetails: UserService) { 
    this.nDetails = navDetails;
  }
    navigateTo(path: String){
      console.log([path])
      this._router.navigate([path])
    }
    ngOnInit(): void {
      console.log('AppComponent--' +this.navDetails.navigatorDetails)
      
      this.navigatorDetails = this.nDetails.navigatorDetails;
      let name:string =this.nDetails.navigatorDetails.firstname;
      console.log(name.length)
      this.isLoggedIn = ( name != null && name.length>0);
      console.log('AppComponent' + this.navigatorDetails);
    }
}
