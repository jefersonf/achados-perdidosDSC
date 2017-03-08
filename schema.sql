drop table if exists entries;
create table entries (
  id integer primary key autoincrement,
  name text not null,
  'text' text not null,
  status text not null,
  category text not null
);

drop table if exists tokens;
create table tokens (
  id integer primary key autoincrement,
  token text not null,
  status text not null
);
