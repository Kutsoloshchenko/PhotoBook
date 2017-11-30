// Service that makes http request to server reguarding authorization 

import { Injectable } from '@angular/core';
import { Http, Headers } from "@angular/http";

import 'rxjs/add/operator/toPromise';



@Injectable()
export class AuthService{

    // Rest API link
    private restAPILink = "http://127.0.0.1:8000"

    // constructor that injects HTTP client
    constructor(private http : Http){}