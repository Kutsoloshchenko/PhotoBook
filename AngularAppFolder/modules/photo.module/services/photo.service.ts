// Service that makes http request to server reguarding authorization 

import { Injectable } from '@angular/core';
import { Http, Headers } from "@angular/http";
import { Photo } from '../classes/photo';

import 'rxjs/add/operator/toPromise';



@Injectable()
export class PhotoService{

    // Rest API link
    private restAPILink = "http://127.0.0.1:8000"

    // constructor that injects HTTP client
    constructor(private http : Http){}

    public GetPhotos(username: string, token: string, album: string): Promise<Photo[]> {
        const body = ({username: username,
                       token: token,
                       album: album})
        
        return this.http
                   .post(this.restAPILink+"/get_files/", body)
                   .toPromise()
                   .then(result => result.json() as Photo[])

    }

    public DeletePhotos(username: string, token: string, folder_name: string, file_names: string): Promise<Photo> {
        const body = ({username: username,
                       token: token,
                       folder_name: folder_name,
                       file_names: file_names})
        
        return this.http
                   .post(this.restAPILink+"/delete_files/", body)
                   .toPromise()
                   .then(result => result.json() as Photo)

    }

    public ChangePhoto(username: string, token: string, folder_name: string, file_name: string, image_dict: Photo): Promise<Photo> {
        const body = ({username: username,
                       token: token,
                       folder_name: folder_name,
                       file_name: file_name,
                       image_dict: image_dict})
        
        return this.http
                   .post(this.restAPILink+"/change_file/", body)
                   .toPromise()
                   .then(result => result.json() as Photo)

    }

    public CreateFile(username: string, token: string, folder_name: string, image_dict: Photo): Promise<Photo> {
        const body = ({username: username,
                       token: token,
                       folder_name: folder_name,
                       image_dict: image_dict})
        
        return this.http
                   .post(this.restAPILink+"/create_file/", body)
                   .toPromise()
                   .then(result => result.json() as Photo)

    }


}