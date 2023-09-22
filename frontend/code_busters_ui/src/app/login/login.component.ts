import { Component, NgModule } from '@angular/core';
import { FormBuilder, FormGroup, FormControl, Validators } from '@angular/forms';


@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})

export class LoginComponent {
 
  loginForm = this.fb.group({
    userName: ['',Validators.required],
    secret: ['', Validators.required]
  });

  constructor(private fb: FormBuilder) { }
  
  onSubmit() {
    // TODO: Use EventEmitter with form value
    console.log(this.loginForm.value);
  }
}
