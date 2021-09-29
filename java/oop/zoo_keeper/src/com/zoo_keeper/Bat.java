package com.zoo_keeper;

public class Bat extends Mammal {
	public Bat() {
		super();
		setEnergy(300);
	}
	
	public void fly() {
		System.out.println("Aww Aww Aww");
		setEnergy(getEnergy()-50);
	}
	
	public void eatHumans() {
		System.out.println("So~ well");
		setEnergy(getEnergy()+25);
	}
	
	public void attackTown() {
		System.out.println("Town on fire");
		setEnergy(getEnergy()-100);
	}
}
