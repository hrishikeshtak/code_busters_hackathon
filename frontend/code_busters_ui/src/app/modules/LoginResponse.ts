export class LoginResponse{
    fname : String;
    lname : String;
    role : String;
    navId : Number

    constructor(first_name : String, last_name:String, role:String, id: Number){
        this.fname = first_name;
        this.lname = last_name;
        this.role = role;
        this.navId = id;
    }
}