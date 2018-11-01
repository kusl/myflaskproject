create extension if not exists "pgcrypto";
create schema if not exists mcny;
create table person (
    id uuid,
    legal_name varchar(400)
)