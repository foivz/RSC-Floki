package me.flokee.krvopija;

import java.util.Map;

/**
 * Created by kfrane on 22/11/14.
 */
public class LoginResponseObject {
    private String status;
    private String token;

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    public String getToken() {
        return token;
    }

    public void setToken(String token) {
        this.token = token;
    }

    public boolean ok() {
        if ("OK".equals(status)) return true;
        return false;
    }

}
