import { Injectable, Injector } from "@angular/core";
@Injectable({
    providedIn:'root',
})
export class UserService {
    constructor(){}
    isLoggedIn: Boolean= false;
    public navigatorDetails!:{
        "firstname":"",
        "lastname":"",
        "navigatorId":"",
        "role":""
    };
}