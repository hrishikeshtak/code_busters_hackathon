import { HttpClient } from "@angular/common/http";
import { Injectable } from "@angular/core";
import { Observable } from "rxjs";

@Injectable({
    providedIn: "root"
})

export class ApiService {
    private baseURl = '';

    constructor(private httpClient: HttpClient) {
    }

    public navigatorLogin(): Observable<any> {
        return this.httpClient.get(this.baseURl + '/login', {
            headers: {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            }
        });
    }
}