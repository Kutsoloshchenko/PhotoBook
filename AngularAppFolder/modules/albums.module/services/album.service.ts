// Service that makes http request to server reguarding authorization 

import { Injectable } from '@angular/core';
import { Http, Headers } from "@angular/http";
import { Album } from '../classes/album';

import 'rxjs/add/operator/toPromise';



@Injectable()
export class AlbumService{

    // Rest API link
    private restAPILink = "http://127.0.0.1:8000"

    // constructor that injects HTTP client
    constructor(private http : Http){}

    public GetUserAlbums(username: string, token: string): Promise<Album[]> {
        const body = ({username: username,
                       token: token})
        
        return this.http
                   .post(this.restAPILink+"/get_albums/", body)
                   .toPromise()
                   .then(result => result.json() as Album[])

    }

    public DeleteAlbum(username: string, token: string, folder_name: string): Promise<Album> {
        const body = ({username: username,
                       token: token,
                       folder_name: folder_name})
        
        return this.http
                   .post(this.restAPILink+"/delete_album/", body)
                   .toPromise()
                   .then(result => result.json() as Album)

    }

    public ChangeUserAlbums(username: string, token: string, folder_name: string, new_name: string): Promise<Album> {
        const body = ({username: username,
                       token: token,
                       folder_name: folder_name,
                       new_name: new_name})
        
        return this.http
                   .post(this.restAPILink+"/change_album_name/", body)
                   .toPromise()
                   .then(result => result.json() as Album)

    }

    public CreateAlbum(username: string, token: string, folder_name: string): Promise<Album> {
        const body = ({username: username,
                       token: token,
                       folder_name: folder_name})
        
        return this.http
                   .post(this.restAPILink+"/create_album/", body)
                   .toPromise()
                   .then(result => result.json() as Album)

    }


}