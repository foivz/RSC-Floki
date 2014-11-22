package me.flokee.krvopija;

import retrofit.Callback;
import retrofit.http.GET;
import retrofit.http.POST;
import retrofit.http.Query;

/**
 * Created by kfrane on 22/11/14.
 */
public interface KrvopijaService {
    @POST("/REST/login")
    void login(
            @Query("username") String username,
            @Query("password") String password,
            Callback<LoginResponseObject> cb);

}

/*
 User:donor1
 Pass:test
 */