package com.zoo_keeper;

public class Mammal {
	private int energyLevel;
	
	public Mammal() {
		energyLevel = 100;
	}
	
	public int displayEnergy() {
		int energy = getEnergy();
		System.out.println("Energy: " + energy);
		return energy;
	}
	
	
	public int getEnergy() {
		return energyLevel;
	}
	
	public void setEnergy(int e) {
		energyLevel = e;
	}
}
