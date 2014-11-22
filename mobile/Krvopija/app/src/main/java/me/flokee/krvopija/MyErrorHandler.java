package me.flokee.krvopija;

import android.util.Log;

import retrofit.ErrorHandler;
import retrofit.RetrofitError;

/**
 * Created by kfrane on 22/11/14.
 */
public class MyErrorHandler implements ErrorHandler {

    @Override
    public Throwable handleError(RetrofitError cause) {
        Log.e("moj1", "neuspjesan get " + cause.getMessage());
        return cause;
    }
}
