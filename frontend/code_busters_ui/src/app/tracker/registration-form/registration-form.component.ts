import { Component } from '@angular/core';
import { FormBuilder, FormGroup, FormControl, Validators } from '@angular/forms';

@Component({
  selector: 'app-registration-form',
  templateUrl: './registration-form.component.html',
  styleUrls: ['./registration-form.component.css']
})
export class RegistrationFormComponent {
  registrationForm: FormGroup;

  constructor(private formBuilder: FormBuilder){
    this.registrationForm = formBuilder.group([
      // firstName = ['', Validators.required],
      // lastName = ['', Validators.required]
    ]);
  }

  onSubmit(){
    console.log(this.registrationForm.value);
  }
}
