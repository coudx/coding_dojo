package com.abstract_art;

public class Sculpture extends Art {

	private String material;
	
	public Sculpture(String t, String m) {
		super(t);
		material = m;
	}
	
	@Override
	void vewArt() {
		// TODO Auto-generated method stub
		System.out.println(String.format("Title: %s\n Author: %s\n Description: %s\n PaintType: %s", getTitle(), getAuthor(), getDescription(), getMaterial()));
	}
	public String getMaterial() {
		return material;
	}
	public void setMaterial(String material) {
		this.material = material;
	}


}
