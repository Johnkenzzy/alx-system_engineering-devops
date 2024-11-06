#!/usr/bin/env ruby

string_input = ARGV[0]

if string_input =~ /from:([^\]]+)\].*to:([^\]]+)\].*flags:([^\]]+)/
  sender = $1
  receiver = $2
  flags = $3
  puts "#{sender},#{receiver},#{flags}"
else
  puts ""
end
