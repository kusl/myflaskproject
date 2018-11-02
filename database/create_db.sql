create extension if not exists "pgcrypto";
create schema if not exists mcny;

create table mcny.person (
    id uuid default gen_random_uuid(),
    legal_name varchar(400)
);

create table mcny.videos (
    id uuid,
    timestamp without time zone default (now() at time zone 'utc'),
    payload jsonb
);
