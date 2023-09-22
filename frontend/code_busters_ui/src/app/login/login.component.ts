import { Component, NgModule } from '@angular/core';
import { FormBuilder, FormGroup, FormControl, Validators } from '@angular/forms';
import { ApiService } from '../services/api-services'
import { LoginData } from '../modules/LoginData';
import { LoginResponse } from '../modules/LoginResponse';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})

export class LoginComponent {
 
  loginForm = this.login.group({
    userName: ['',Validators.required],
    secret: ['', Validators.required]
  });

  constructor(private apiService : ApiService, private login: FormBuilder, private _router : Router) { }
  
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
      //this.navigateTo('/dashboard');
    },(error) => {
      console.log('Error'+error);
    })
  }
  navigateTo(page:String) {
    this._router.navigate([page]);
  }
}
