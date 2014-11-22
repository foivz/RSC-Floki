package me.flokee.krvopija;

import retrofit.RestAdapter;
import retrofit.android.AndroidLog;

/**
 * Created by kfrane on 22/11/14.
 */
public class Services {
    private static KrvopijaService krvopijaService;
    private static RestAdapter restAdapter;

    static {
        restAdapter = new RestAdapter.Builder()
                .setLogLevel(RestAdapter.LogLevel.FULL)
                .setLog(new AndroidLog("RestAdapter"))
                .setEndpoint("http://rsc.flokee.me")
                .setErrorHandler(new MyErrorHandler())
                .build();
        krvopijaService = restAdapter.create(KrvopijaService.class);
    }

    public static KrvopijaService getKrvopijaService() {
        return krvopijaService;
    }
}
