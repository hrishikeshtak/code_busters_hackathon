import { Component } from '@angular/core';
import { FormBuilder, FormGroup, FormControl, Validators } from '@angular/forms';

@Component({
  selector: 'app-registration-form',
  templateUrl: './registration-form.component.html',
  styleUrls: ['./registration-form.component.css']
})
export class RegistrationFormComponent {
  registrationForm:FormGroup;

  constructor(private fb: FormBuilder) { 
    this.registrationForm = this.fb.group({
      firstName: ['',Validators.required],
      lastName: ['', Validators.required],
      dob: [new Date(), Validators.required],
      contactNumber: ['(000) 000 0000', Validators.required],
      location: ['', Validators.required]
    });
  }
  
  onSubmit() {
    // TODO: Use EventEmitter with form value
    console.log(this.registrationForm.value);
  }
}
