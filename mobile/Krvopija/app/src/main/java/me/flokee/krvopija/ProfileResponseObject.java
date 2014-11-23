package me.flokee.krvopija;

import me.flokee.krvopija.model.Profile;

/**
 * Created by kfrane on 22/11/14.
 */
public class ProfileResponseObject {
    private String status;
    private Profile profile;

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    public Profile getProfile() {
        return profile;
    }

    public void setProfile(Profile profile) {
        this.profile = profile;
    }

    public boolean ok() {
        if ("OK".equals(status)) return true;
        return false;
    }

}
