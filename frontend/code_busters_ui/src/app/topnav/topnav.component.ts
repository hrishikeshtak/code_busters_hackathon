import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { UserService } from '../services/user-services';

@Component({
  selector: 'app-topnav',
  templateUrl: './topnav.component.html',
  styleUrls: ['./topnav.component.css']
})
export class TopnavComponent implements OnInit{
  navigatorDetails : any;
  constructor(private _router : Router, private navDetails: UserService) { }
    navigateTo(path: String){
      console.log([path])
      this._router.navigate([path])
    }
    ngOnInit(): void {
      //console.log('TopNav--' +this.navDetails.isLoggedIn)
      this.navigatorDetails = this.navDetails.navigatorDetails;
      console.log('topNav' + this.navigatorDetails);
    }
}
