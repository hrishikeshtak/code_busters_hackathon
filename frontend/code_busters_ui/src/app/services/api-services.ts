import { HttpClient } from "@angular/common/http";
import { Injectable } from "@angular/core";
import { Observable } from "rxjs";

@Injectable({
    providedIn: "root"
})

export class ApiService {
    private baseURl = 'https://mibg93bqyi.us-east-1.awsapprunner.com';

    constructor(private httpClient: HttpClient) {
    }

     public navigatorLogin (loginData : any): Observable<any> {
        console.log('navigatorLogin Request'+loginData);
        return this.httpClient.post(this.baseURl+'/login', loginData, {
            headers: {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            responseType : 'json'
        });
        
    }
    public registration (loginData : any): Observable<any> {
        console.log('registration Request'+loginData);
        return this.httpClient.post(this.baseURl+'/register', loginData, {
            headers: {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            responseType : 'json'
        });
    }
    public listHelpseeker (navId : any): Observable<any> {
        console.log('listHelpseeker Request'+navId);
        return this.httpClient.get(this.baseURl+'/list_helpseekers/'+navId, {
            headers: {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            responseType : 'json'
        });
    }
    public stats (): Observable<any> {
        console.log('stats Request');
        return this.httpClient.get(this.baseURl+'/stats', {
            headers: {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            responseType : 'json'
        });
    }

    public listCategories (): Observable<any> {
        console.log('listCategories Request');
        return this.httpClient.get(this.baseURl+'/category', {
            headers: {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            responseType : 'json'
        });
    }
}