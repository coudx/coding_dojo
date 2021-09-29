package com.abstract_art;

//inside of Art.java
public abstract class Art {
// TODO: implement Art class
	private String title;
	private String author;
	private String description;
	
	public Art() {
		title = "";
		author = "";
		description = "";
	}
	
	public Art(String t) {
		title = t;
	}
	
	abstract void vewArt();

	public String getTitle() {
		return title;
	}

	public void setTitle(String title) {
		this.title = title;
	}

	public String getAuthor() {
		return author;
	}

	public void setAuthor(String author) {
		this.author = author;
	}

	public String getDescription() {
		return description;
	}

	public void setDescription(String description) {
		this.description = description;
	}
	
}
