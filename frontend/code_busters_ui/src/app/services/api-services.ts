import { HttpClient } from "@angular/common/http";
import { Injectable } from "@angular/core";
import { Observable } from "rxjs";
import { LoginResponse } from "../modules/LoginResponse";

@Injectable({
    providedIn: "root"
})

export class ApiService {
    private baseURl = 'https://mibg93bqyi.us-east-1.awsapprunner.com';

    constructor(private httpClient: HttpClient) {
    }

     public navigatorLogin (loginData : any): Observable<any> {
        console.log('Request'+loginData);
        return this.httpClient.post('https://mibg93bqyi.us-east-1.awsapprunner.com/login', loginData, {
            headers: {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            responseType : 'json'
        });
    }

    // public navigatorLogin (loginData :FormData): Observable<LoginResponse> {
    //     console.log('Request'+loginData);
    //     return this.httpClient.get<LoginResponse>(this.baseURl + '/login', {
    //         headers: {
    //             'Content-Type': 'application/json',
    //             'Access-Control-Allow-Origin': '*'
    //         },
    //         responseType : 'json'
    //     });
    // }
}