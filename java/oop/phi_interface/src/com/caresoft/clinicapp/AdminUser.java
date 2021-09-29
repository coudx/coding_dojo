package com.caresoft.clinicapp;

import java.util.ArrayList;
import java.util.Date;
public class AdminUser extends User implements PHICompliantUser, PHIAdminCompliant{
    private Integer employeeID;
    private String role;
    private ArrayList<String> securityIncidents;

    public AdminUser() {
        securityIncidents = new ArrayList<String>();
    }

    public void newIncident(String notes) {
        String report = String.format(
                "Datetime Submitted: %s \n,  Reported By ID: %s\n Notes: %s \n",
                new Date(), this.id, notes
        );
        securityIncidents.add(report);
    }
    public void authIncident() {
        String report = String.format(
                "Datetime Submitted: %s \n,  ID: %s\n Notes: %s \n",
                new Date(), this.id, "AUTHORIZATION ATTEMPT FAILED FOR THIS USER"
        );
        securityIncidents.add(report);
    }

    public ArrayList<String> getSecurityIncidents() {
        return securityIncidents;
    }

    @Override
    public boolean assignPin(int pin) {
        if (String.valueOf(pin).length() > 5) {
            setPin(pin);
            return true;
        }
        System.out.println("Pin must be 6 digits or more.");
        return false;
    }

    @Override
    public boolean isAuthorized(Integer confirmedAuthID) {
        if (getId() == confirmedAuthID) {
            return true;
        }
        authIncident();
        return false;
    }

    @Override
    public ArrayList<String> reportSecurityIncidents() {
        return getSecurityIncidents();
    }
}
