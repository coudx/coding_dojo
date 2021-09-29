package com.caresoft.clinicapp;

import java.util.Date;
import java.util.ArrayList;
import java.util.HashSet;
public class Physician extends User implements PHICompliantUser, PHIAdminCompliant {

    private HashSet<Patient> patients;
    private ArrayList<String> securityIncidents;

    // ... you see other existing member variables. ...

    // TO DO: Constructor

    public Physician() {
        patients = new HashSet<Patient>();
        securityIncidents = new ArrayList<String>();
    }

    public void prescribeRXTo(Patient patient, Integer rxNumber) {
        patient.currentPrescriptionsByRX.add(rxNumber);
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

// TO DO: Setters & Getters
    public HashSet<Patient> getPatients() {
        return patients;
    }

    public void setPatients(HashSet<Patient> patients) {
        this.patients = patients;
    }

    public ArrayList<String> getSecurityIncidents() {
        return securityIncidents;
    }

    public void setSecurityIncidents(ArrayList<String> securityIncidents) {
        this.securityIncidents = securityIncidents;
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
