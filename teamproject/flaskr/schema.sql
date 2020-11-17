DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS post;
DROP TABLE IF EXISTS dailypass;
DROP TABLE IF EXISTS quarantine;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE post (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  author_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  title TEXT NOT NULL,
  body TEXT NOT NULL,
  FOREIGN KEY (author_id) REFERENCES user (id)
);

CREATE TABLE "dailypass" (
	id	INTEGER,
	username	TEXT NOT NULL,
	symptoms	BOOL,
	date DATE,
	visittime	INTEGER,
	building	TEXT,
	room	TEXT,
	PRIMARY KEY(id AUTOINCREMENT)
);

CREATE TABLE "quarantine" (
	"id"	INTEGER,
	"username"	TEXT NOT NULL,
	"date"	INTEGER,
	"is_quarantine"	BOOL,
	PRIMARY KEY("id" AUTOINCREMENT)
);