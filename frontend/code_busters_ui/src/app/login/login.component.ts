import { Component, NgModule, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, FormControl, Validators } from '@angular/forms';
import { ApiService } from '../services/api-services'
import { Router } from '@angular/router';
import { UserService } from '../services/user-services';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})

export class LoginComponent implements OnInit{
 
  loginForm = this.login.group({
    userName: ['',Validators.required],
    secret: ['', Validators.required]
  });
  navigatorDetails : any;

  constructor(private apiService : ApiService, private login: FormBuilder, private _router : Router, private navDetails : UserService) { }
  ngOnInit(): void {
      this.navigatorDetails ={
        "firstname":"",
        "lastname":"",
        "navigatorId":"",
        "role":""
    };
  }
  onSubmit() {
    // TODO: Use EventEmitter with form value
    console.log(this.loginForm.value);

    const loginData = new FormData();
    let password = this.loginForm.value.secret;
    let username = this.loginForm.value.userName;
    loginData.append('username', username??'');
    loginData.append('password',  password??'');
    let lData = {
      'username': username,
      'password': password
    }
    this.apiService.navigatorLogin(lData).subscribe((data: any) => {
      console.log('Response'+data.id+data.first_name+data.last_name+data.role);

      // this.navigatorDetails= {
      //   firstname: data.first_name,
      //   lastname: data.last_name,
      //   navigatorId: data.id,
      //   role: data.role
      // };
      // console.log('Login --' + this.navigatorDetails);
      // this.navDetails.navigatorDetails = this.navigatorDetails
      // console.log('Login Details -- ' + this.navDetails.navigatorDetails);
     // this.navDetails.isLoggedIn = true;
      this._router.navigateByUrl('dashboard');
    },(error) => {
      console.log('Error'+error);
    })
  }
}
