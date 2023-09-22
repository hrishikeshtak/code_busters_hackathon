import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, FormControl, Validators } from '@angular/forms';
import { ApiService } from 'src/app/services/api-services';

@Component({
  selector: 'app-registration-form',
  templateUrl: './registration-form.component.html',
  styleUrls: ['./registration-form.component.css']
})
export class RegistrationFormComponent implements OnInit{
  registrationForm:FormGroup;
  categories=[];

  constructor(private fb: FormBuilder, private apiService: ApiService) { 
    this.registrationForm = this.fb.group({
      firstName: ['',Validators.required],
      lastName: ['', Validators.required],
      dob: [new Date(), Validators.required],
      contactNumber: ['(000) 000 0000', Validators.required],
      location: ['', Validators.required]
    });
  }

  ngOnInit(): void {
    this.apiService.listCategories().subscribe((data: any) => {
      console.log('Response'+data);
      this.categories=data;
      console.log(this.categories.length)
    },(error) => {
      console.log('Error'+error);
    })

  }
  
  onSubmit() {
    // TODO: Use EventEmitter with form value
    console.log(this.registrationForm.value);
  }
}
