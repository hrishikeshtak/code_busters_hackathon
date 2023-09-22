export class Category {
    first_name : String;
    last_name : String;
    date_of_birth: Date;
    location: String;
    navigator_id: number;
    contact_number: String;

    constructor(first_name : String, last_name : String, date_of_birth: Date, location: String, navigator_id: number,
        contact_number: String){
        this.first_name=first_name;
        this.last_name=last_name;
        this.date_of_birth=date_of_birth;
        this.location = location;
        this.navigator_id=navigator_id;
        this.contact_number=contact_number;
    }
}