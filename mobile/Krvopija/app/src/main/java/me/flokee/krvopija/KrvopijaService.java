package me.flokee.krvopija;

import java.util.Map;

import retrofit.Callback;
import retrofit.http.GET;
import retrofit.http.POST;
import retrofit.http.Query;
import retrofit.http.QueryMap;

/**
 * Created by kfrane on 22/11/14.
 */
public interface KrvopijaService {
    @POST("/REST/login")
    void login(
            @Query("username") String username,
            @Query("password") String password,
            Callback<LoginResponseObject> cb);

    @GET("/REST/profile")
    void profile(@Query("token") String token,
                 Callback<ProfileResponseObject> cb);

    @GET("/REST/subscribe")
    void subscribe(@Query("token") String token, @Query("notificationToken") String notificationToken, Callback<Object> cb);

    @POST("/REST/profile")
    void updateProfile(
            @Query("token") String token,
            @Query("data") String data,
            Callback<ProfileUpdateResponseObject> cb);

    @GET("/REST/events")
    void addEvent(
            @Query("token") String token,
            @Query("type") String data,
            Callback<EventResponseObject> cb);
}

/*
 User:donor1
 Pass:test
 */
