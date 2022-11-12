CREATE TABLE "USERS" (
  "id" integer PRIMARY KEY AUTOINCREMENT,
  "createdAt" timestamp DEFAULT current_timestamp,
  "updatedAt" timestamp DEFAULT current_timestamp,
  "email" TEXT UNIQUE NOT NULL,
  "password" TEXT NOT NULL,
  "userName" TEXT UNIQUE NOT NULL
);

CREATE TABLE "SUBS" (
  "id" integer PRIMARY KEY AUTOINCREMENT,
  "userName" TEXT,
  "createdAt" timestamp DEFAULT current_timestamp,
  "updatedAt" timestamp DEFAULT current_timestamp,
  "name" TEXT UNIQUE NOT NULL,
  "title" TEXT UNIQUE NOT NULL,
  "description" TEXT,
  "imageUrn" TEXT,
  "bannerUrn" TEXT,
  FOREIGN KEY("userName") REFERENCES USERS(userName)
);

CREATE TABLE "POSTS" (
  "id" integer PRIMARY KEY AUTOINCREMENT,
  "userName" TEXT,
  "subName" TEXT,
  "createdAt" timestamp DEFAULT current_timestamp,
  "updatedAt" timestamp DEFAULT current_timestamp,
  "title" TEXT UNIQUE NOT NULL,
  "body" TEXT NOT NULL,
  FOREIGN KEY(userName) REFERENCES USERS(userName),
  FOREIGN KEY(subName) REFERENCES SUBS(name)
);

CREATE TABLE "VOTES" (
  "id" integer PRIMARY KEY AUTOINCREMENT,
  "userName" TEXT,
  "postID" integer,
  "createdAt" timestamp DEFAULT current_timestamp,
  "updatedAt" timestamp DEFAULT current_timestamp,
  "value" integer DEFAULT 0,
  FOREIGN KEY(userName) REFERENCES USERS(userName),
  FOREIGN KEY(postID) REFERENCES POSTS(id)
);

CREATE TABLE "COMMENTS" (
  "id" integer PRIMARY KEY AUTOINCREMENT,
  "userName" TEXT,
  "postID" integer,
  "createdAt" timestamp DEFAULT current_timestamp,
  "updatedAt" timestamp DEFAULT current_timestamp,
  "body" integer NOT NULL,
  FOREIGN KEY(userName) REFERENCES USERS(userName),
  FOREIGN KEY(postID) REFERENCES POSTS(id)
);