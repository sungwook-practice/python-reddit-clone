# 개요
데이터베이스 설정

# 데이터베이스 설치
도커를 이용하여 데이터베이스를 설치합니다.
```shell
# volume 생성
docker volume create mariadb-data

# 도커 컨테이너 실행
docker run -d  \
-p 3306:3306  \
--name mariadb \
-e MARIADB_ROOT_PASSWORD=password \
-e TZ=Asia/Seoul \
-v mariadb-data:/var/lib/mysql \
mariadb:10.3.30 --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci
```

# 스키마
```mariadb
CREATE DATABASE reddit CHARACTER SET utf8mb4 collate utf8mb4_general_ci;
```

# 테이블
```mariadb
CREATE TABLE `USERS` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `createdAt` timestamp DEFAULT (now()),
  `updatedAt` timestamp DEFAULT (now()),
  `email` varchar(255) UNIQUE NOT NULL,
  `password` varchar(255) NOT NULL,
  `userName` varchar(255) UNIQUE NOT NULL
);

CREATE TABLE `SUBS` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `userName` varchar(255),
  `createdAt` timestamp DEFAULT (now()),
  `updatedAt` timestamp DEFAULT (now()),
  `name` varchar(255) UNIQUE NOT NULL,
  `title` varchar(255) UNIQUE NOT NULL,
  `description` varchar(255),
  `imageUrn` varchar(255),
  `bannerUrn` varchar(255)
);

CREATE TABLE `POSTS` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `userName` varchar(255),
  `subName` varchar(255),
  `createdAt` timestamp DEFAULT (now()),
  `updatedAt` timestamp DEFAULT (now()),
  `title` varchar(255) UNIQUE NOT NULL,
  `body` varchar(255) NOT NULL
);

CREATE TABLE `VOTES` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `userName` varchar(255),
  `postID` int,
  `createdAt` timestamp DEFAULT (now()),
  `updatedAt` timestamp DEFAULT (now()),
  `value` int DEFAULT 0
);

CREATE TABLE `COMMENTS` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `userName` varchar(255),
  `postID` int,
  `createdAt` timestamp DEFAULT (now()),
  `updatedAt` timestamp DEFAULT (now()),
  `body` int NOT NULL
);

ALTER TABLE `SUBS` ADD FOREIGN KEY (`userName`) REFERENCES `USERS` (`userName`);

ALTER TABLE `POSTS` ADD FOREIGN KEY (`userName`) REFERENCES `USERS` (`userName`);

ALTER TABLE `POSTS` ADD FOREIGN KEY (`subName`) REFERENCES `SUBS` (`name`);

ALTER TABLE `VOTES` ADD FOREIGN KEY (`userName`) REFERENCES `USERS` (`userName`);

ALTER TABLE `VOTES` ADD FOREIGN KEY (`postID`) REFERENCES `POSTS` (`id`);

ALTER TABLE `COMMENTS` ADD FOREIGN KEY (`userName`) REFERENCES `USERS` (`userName`);

ALTER TABLE `COMMENTS` ADD FOREIGN KEY (`postID`) REFERENCES `POSTS` (`id`);
```