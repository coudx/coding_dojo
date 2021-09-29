package com.abstract_art;

public class Painting extends Art {

	private String paintType;
	
	public Painting(String t, String pt) {
		super(t);
		paintType = pt;
	}
	@Override
	void vewArt() {
		// TODO Auto-generated method stub
		System.out.println(String.format("Title: %s\n Author: %s\n Description: %s\n PaintType: %s", getTitle(), getAuthor(), getDescription(), getPaintType()));
	}
	public String getPaintType() {
		return paintType;
	}
	public void setPaintType(String paintType) {
		this.paintType = paintType;
	}

}
