package com.zoo_keeper;

public class Gorilla extends Mammal {
	public Gorilla() {
		super();
	}
	
	public void throwSomething() {
		System.out.println("The Gorilla has thrown something");
		setEnergy(getEnergy()-5);
	}
	
	public void eatBananas() {
		System.out.println("The Gorilla has been satisfied");
		setEnergy(getEnergy()+10);
	}
	
	public void climb() {
		System.out.println("The Gorilla has climb a tree");
		setEnergy(getEnergy()-10);
	}
	
	
}
