package com.caresoft.clinicapp;

import java.util.ArrayList;
import java.util.Date;

public class Patient extends User implements PHICompliantUser{

    private String firstName;
    private String lastName;
    // .. other personal identifying information .. //

    Physician primaryCarePhysician;
    ArrayList<Integer> currentPrescriptionsByRX;
    int providerCode;
    int memberNumber;
    PatientRecord medicalHistory;

    // TO DO: Constructor

    public Patient(String firstName, String lastName) {
        setFirstName(firstName);
        setLastName(lastName);
        currentPrescriptionsByRX = new ArrayList<Integer>();
        medicalHistory = new PatientRecord(new ArrayList<String>());
    }

    public boolean requestAppointment(Date date, Physician doctor) {
        boolean successfullyAdded = false;
        // you see existing code to find and schedule an appointment
        // (Leave as is for the assignment, no need to implement anything here.)
        return successfullyAdded;
    }
    void addChartNotes(String notes) {
        this.medicalHistory.getCharts().add(notes);
    }

// TO DO: Setters & Getters
    public String getFirstName() {
        return firstName;
    }

    public void setFirstName(String firstName) {
        this.firstName = firstName;
    }

    public String getLastName() {
        return lastName;
    }

    public void setLastName(String lastName) {
        this.lastName = lastName;
    }

    @Override
    public boolean assignPin(int pin) {
        if (String.valueOf(pin).length() == 4 && pin != 1234 && pin != 4321){
            setPin(pin);
            return true;
        }
        System.out.println("Must be a valid, exactly 4-digit long pin, and must not be 1234 or 4321");
        return false;
    }

    @Override
    public boolean isAuthorized(Integer confirmedAuthID) {
        if (getId() == confirmedAuthID){
            return true;
        }
        return false;
    }
}
