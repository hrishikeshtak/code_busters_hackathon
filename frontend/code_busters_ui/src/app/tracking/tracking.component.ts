import { Component } from '@angular/core';
import { ApiService } from '../services/api-services';

@Component({
  selector: 'app-tracking',
  templateUrl: './tracking.component.html',
  styleUrls: ['./tracking.component.css']
})
export class TrackingComponent {
  constructor(private apiService : ApiService){

	}
}
