import { Component, OnInit } from '@angular/core';
import { ApiService } from '../services/api-services'
import { CanvasJS, CanvasJSAngularChartsModule } from '@canvasjs/angular-charts';

@Component({
  selector: 'app-reporting',
  templateUrl: './reporting.component.html',
  styleUrls: ['./reporting.component.css']
})
export class ReportingComponent implements OnInit{
	categoryChartOptions : any;
	cStats =[]
	organizationChartOptions : any;
	statusChartOptions :any;
	navigatorChartOptions :any;
	chartOptions : any;
	constructor(private apiService : ApiService){
		this.categoryChartOptions={};	  
	}
	
	
	ngOnInit(): void {
		this.apiService.stats().subscribe((data: any) => {
			console.log("data" + data[0].category_stats[0].y);
			this.cStats = data[0].category_stats;
			console.log("---"+this.cStats)
			
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
				  dataPoints: this.cStats
				}]
			  }	
			  
			  let oStats = data[0].organization_stats;
			  this.organizationChartOptions = {
				animationEnabled: true,
				title: {
				  text: "Organization Stats"
				},
				data: [{
				  type: "pie",
				  startAngle: -80,
				  indexLabel: "{key}: {y}",
				  yValueFormatString: "#,###.##'%'",
				  dataPoints: oStats
				}]
			  }	
			  let sStats = data[0].status_stats;
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
				  dataPoints: sStats
				}]
			  }	
			  let nStats = data[0].status_stats;
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
				  dataPoints: nStats
				}]
			  }	
		},(error) => {
		console.log('Error'+error);
		});
	}
  
}
