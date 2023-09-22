import { Component, OnInit } from '@angular/core';
import { ApiService } from '../services/api-services'
import { CanvasJSAngularChartsModule } from '@canvasjs/angular-charts';

@Component({
  selector: 'app-reporting',
  templateUrl: './reporting.component.html',
  styleUrls: ['./reporting.component.css']
})
export class ReportingComponent implements OnInit{
	categoryChartOptions : any;
	organizationChartOptions : any;
	statusChartOptions :any;
	navigatorChartOptions :any;
	constructor(private apiService : ApiService){

	}
	ngOnInit(): void {
		this.apiService.stats().subscribe((data: any) => {
			console.log("data" + data[0].category_stats);
			this.categoryChartOptions = {
				animationEnabled: true,
				title: {
				  text: "Category Stats"
				},
				data: [{
				  type: "pie",
				  startAngle: -90,
				  indexLabel: "{key}: {y}",
				  yValueFormatString: "#,###.##'%'",
				  dataPoints: data[0].category_stats
				}]
			  }	
			  this.organizationChartOptions = {
				animationEnabled: true,
				title: {
				  text: "Organization Stats"
				},
				data: [{
				  type: "pie",
				  startAngle: -90,
				  indexLabel: "{key}: {y}",
				  yValueFormatString: "#,###.##'%'",
				  dataPoints: data[0].organization_stats
				}]
			  }	
			  this.statusChartOptions = {
				animationEnabled: true,
				title: {
				  text: "Helpseeker Status Stats"
				},
				data: [{
				  type: "pie",
				  startAngle: -90,
				  indexLabel: "{key}: {y}",
				  yValueFormatString: "#,###.##'%'",
				  dataPoints: data[0].status_stats
				}]
			  }	
			  this.navigatorChartOptions = {
				animationEnabled: true,
				title: {
				  text: "Navigator Stats"
				},
				data: [{
				  type: "pie",
				  startAngle: -90,
				  indexLabel: "{key}: {y}",
				  yValueFormatString: "#,###.##'%'",
				  dataPoints: data[0].navigator_stats
				}]
			  }	
		},(error) => {
		console.log('Error'+error);
		});
	}
  
}
