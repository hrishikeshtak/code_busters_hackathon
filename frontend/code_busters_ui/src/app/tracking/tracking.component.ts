import { Component, OnInit } from '@angular/core';
import { ApiService } from '../services/api-services';

@Component({
  selector: 'app-tracking',
  templateUrl: './tracking.component.html',
  styleUrls: ['./tracking.component.css']
})
export class TrackingComponent implements OnInit{
  navigators : any;
  constructor(private apiService : ApiService){

	}
  ngOnInit(): void {
    this.apiService.listHelpseeker(1).subscribe((data: any) => {
      this.navigators = data;
    },(error) => {
      console.log('Error'+error);
    });
  }
}
