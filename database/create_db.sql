create extension if not exists "pgcrypto";
create schema if not exists mcny;

create table if not exists mcny.users (
    id uuid default gen_random_uuid(),
    legal_name varchar(400)
);

create table if not exists mcny.videos (
    id uuid default gen_random_uuid(),
    video_time timestamp without time zone default (now() at time zone 'utc'),
    payload jsonb
);
