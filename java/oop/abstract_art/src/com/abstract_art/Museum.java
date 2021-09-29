package com.abstract_art;
import java.util.ArrayList;
public class Museum {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		ArrayList<Art> museum = new ArrayList<Art>();
		Painting a = new Painting("paint A", "oil");
		Painting b = new Painting("paint B", "watercolor");
		Painting c = new Painting("paint C", "acrylic");
		Sculpture d = new Sculpture("sculpture D", "Marble");
		Sculpture e = new Sculpture("sculpture E", "Bronze");
		museum.add(a);
		museum.add(b);
		museum.add(c);
		museum.add(d);
		museum.add(e);
	}

}
