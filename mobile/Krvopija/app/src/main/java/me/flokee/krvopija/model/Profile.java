package me.flokee.krvopija.model;

import java.util.List;

public class Profile {
    private String country;
    private int numDonations;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getSurname() {
        return surname;
    }

    public void setSurname(String surname) {
        this.surname = surname;
    }

    private List<String> achivements;
    private BloodType bloodType;
    private String name;
    private String surname;

    public BloodType getBloodType() {
        return bloodType;
    }

    public void setBloodType(BloodType bloodType) {
        this.bloodType = bloodType;
    }

    public String getCountry() {
        return country;
    }

    public void setCountry(String country) {
        this.country = country;
    }

    public int getNumDonations() {
        return numDonations;
    }

    public void setNumDonations(int numDonations) {
        this.numDonations = numDonations;
    }

    public List<String> getAchivements() {
        return achivements;
    }

    public void setAchivements(List<String> achivements) {
        this.achivements = achivements;
    }
}
