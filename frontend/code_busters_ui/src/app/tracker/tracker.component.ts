import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-tracker',
  templateUrl: './tracker.component.html',
  styleUrls: ['./tracker.component.css']
})
export class TrackerComponent {

  constructor(private _router: Router){ }
  
  navigateTo(path: string){
    this._router.navigate([path]);
  }
}
