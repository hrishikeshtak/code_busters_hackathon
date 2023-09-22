export class Category {
    category_id : number;
    organization_id : number;
    notes: String

    constructor(category_id : number, organization_id:number, notes:String){
        this.category_id = category_id;
        this.organization_id = organization_id;
        this.notes=notes;
    }
}