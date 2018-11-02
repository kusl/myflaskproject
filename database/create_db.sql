create extension if not exists "pgcrypto";
create schema if not exists mcny;
create table person (
    id uuid default gen_random_uuid(),
    legal_name varchar(400)
)
create table videos (
    id uuid,
    timestamp without time zone default (now() at time zone 'utc'),
    payload jsonb
)